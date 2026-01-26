import sys
import json
import hashlib
import html
import zipfile
import os

# XML Templates
ASSESSMENT_META_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<quiz identifier="text2qti_assessment_{hash}" xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{title}</title>
  <description></description>
  <shuffle_answers>true</shuffle_answers>
  <scoring_policy>keep_highest</scoring_policy>
  <hide_results></hide_results>
  <quiz_type>assignment</quiz_type>
  <points_possible>{points}</points_possible>
  <require_lockdown_browser>false</require_lockdown_browser>
  <require_lockdown_browser_for_results>false</require_lockdown_browser_for_results>
  <require_lockdown_browser_monitor>false</require_lockdown_browser_monitor>
  <lockdown_browser_monitor_data/>
  <show_correct_answers>true</show_correct_answers>
  <anonymous_submissions>false</anonymous_submissions>
  <could_be_locked>false</could_be_locked>
  <allowed_attempts>1</allowed_attempts>
  <one_question_at_a_time>false</one_question_at_a_time>
  <cant_go_back>false</cant_go_back>
  <available>false</available>
  <one_time_results>false</one_time_results>
  <show_correct_answers_last_attempt>false</show_correct_answers_last_attempt>
  <only_visible_to_overrides>false</only_visible_to_overrides>
  <module_locked>false</module_locked>
  <assignment identifier="text2qti_assignment_{hash}">
    <title>{title}</title>
    <due_at/>
    <lock_at/>
    <unlock_at/>
    <module_locked>false</module_locked>
    <workflow_state>unpublished</workflow_state>
    <assignment_overrides>
    </assignment_overrides>
    <quiz_identifierref>assessment_{hash}</quiz_identifierref>
    <allowed_extensions></allowed_extensions>
    <has_group_category>false</has_group_category>
    <points_possible>{points}</points_possible>
    <grading_type>points</grading_type>
    <all_day>false</all_day>
    <submission_types>online_quiz</submission_types>
    <position>1</position>
    <turnitin_enabled>false</turnitin_enabled>
    <vericite_enabled>false</vericite_enabled>
    <peer_review_count>0</peer_review_count>
    <peer_reviews>false</peer_reviews>
    <automatic_peer_reviews>false</automatic_peer_reviews>
    <anonymous_peer_reviews>false</anonymous_peer_reviews>
    <grade_group_students_individually>false</grade_group_students_individually>
    <freeze_on_copy>false</freeze_on_copy>
    <omit_from_final_grade>false</omit_from_final_grade>
    <intra_group_peer_reviews>false</intra_group_peer_reviews>
    <only_visible_to_overrides>false</only_visible_to_overrides>
    <post_to_sis>false</post_to_sis>
    <moderated_grading>false</moderated_grading>
    <grader_count>0</grader_count>
    <grader_comments_visible_to_graders>true</grader_comments_visible_to_graders>
    <anonymous_grading>false</anonymous_grading>
    <graders_anonymous_to_graders>false</graders_anonymous_to_graders>
    <grader_names_visible_to_final_grader>true</grader_names_visible_to_final_grader>
    <anonymous_instructor_annotations>false</anonymous_instructor_annotations>
    <post_policy>
      <post_manually>false</post_manually>
    </post_policy>
  </assignment>
  <assignment_group_identifierref>assignment_group_{hash}</assignment_group_identifierref>
  <assignment_overrides>
  </assignment_overrides>
</quiz>"""

ASSESSMENT_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">
  <assessment ident="text2qti_assessment_{hash}" title="{title}">
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>1</fieldentry>
      </qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">"""

ASSESSMENT_FOOTER = """    </section>
  </assessment>
</questestinterop>"""

ITEM_TEMPLATE = """      <item ident="text2qti_question_{question_id}" title="Question">
        <itemmetadata>
          <qtimetadata>
            <qtimetadatafield>
              <fieldlabel>question_type</fieldlabel>
              <fieldentry>multiple_choice_question</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>points_possible</fieldlabel>
              <fieldentry>1</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>original_answer_ids</fieldlabel>
              <fieldentry>{original_answer_ids}</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>text2qti_question_ref_{question_id}</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;p&gt;{question_text}&lt;/p&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
{choices}
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">{correct_choice_id}</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>"""

CHOICE_TEMPLATE = """              <response_label ident="{choice_id}">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;{choice_text}&lt;/p&gt;</mattext>
                </material>
              </response_label>"""

def generate_id(content):
    """Generates a unique ID based on content."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 json2qti.py quiz.json")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found")
        sys.exit(1)

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
            quiz_data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {input_file}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {input_file}: {e}")
        sys.exit(1)

    # Calculate hash of input file for unique quiz ID
    json_hash = generate_id(content)
    
    # Check for wrapper object with title
    # Structure: {"Quiz Title": {"Question 1": [...]}}
    if len(quiz_data) == 1 and isinstance(list(quiz_data.values())[0], dict):
        title = list(quiz_data.keys())[0]
        quiz_data = quiz_data[title]
    else:
        # Fallback: Use filename as title (without extension)
        title = os.path.splitext(os.path.basename(input_file))[0]
    
    # Start building assessment XML
    assessment_xml_parts = [ASSESSMENT_HEADER.format(hash=json_hash, title=html.escape(title))]
    
    total_points = 0
    
    for question_text, answers in quiz_data.items():
        if not isinstance(answers, list) or not answers:
            print(f"Warning: Skipping question '{question_text}' - answers must be a non-empty list")
            continue
            
        total_points += 1
        
        # Unique ID for the question
        question_id = generate_id(question_text + json_hash)
        
        # Process answers
        choice_xml_parts = []
        original_answer_ids = []
        correct_choice_id = None
        
        for i, answer_text in enumerate(answers):
            # Unique ID for the answer
            choice_id = "text2qti_choice_" + generate_id(question_text + str(answer_text) + str(i) + json_hash)
            original_answer_ids.append(choice_id)
            
            # First answer is correct
            if i == 0:
                correct_choice_id = choice_id
            
            choice_xml_parts.append(CHOICE_TEMPLATE.format(
                choice_id=choice_id,
                choice_text=html.escape(str(answer_text))
            ))
            
        item_xml = ITEM_TEMPLATE.format(
            question_id=question_id,
            original_answer_ids=",".join(original_answer_ids),
            question_text=html.escape(question_text),
            choices="\n".join(choice_xml_parts),
            correct_choice_id=correct_choice_id
        )
        assessment_xml_parts.append(item_xml)

    assessment_xml_parts.append(ASSESSMENT_FOOTER)
    assessment_xml = "\n".join(assessment_xml_parts)
    
    # Build assessment_meta XML
    assessment_meta_xml = ASSESSMENT_META_TEMPLATE.format(
        hash=json_hash,
        title=html.escape(title),
        points=total_points
    )

    # Create Zip File
    output_filename = title + ".zip"
    quiz_root = f"assessment_{json_hash}"
    
    try:
        with zipfile.ZipFile(output_filename, 'w') as zf:
            zf.writestr(f"{quiz_root}/assessment_meta.xml", assessment_meta_xml)
            zf.writestr(f"{quiz_root}/assessment_{json_hash}.xml", assessment_xml)
        print(f"Successfully created {output_filename}")
    except Exception as e:
        print(f"Error writing zip file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
