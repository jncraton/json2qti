import sys

assessment_meta = """
<?xml version="1.0" encoding="UTF-8"?>
<quiz identifier="text2qti_assessment_8aea25305e6f1efa2ee6679da6ee3d2e84f194810f9b7951b3f6590f415b9f9a" xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
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
  <assignment identifier="text2qti_assignment_8aea25305e6f1efa2ee6679da6ee3d2e84f194810f9b7951b3f6590f415b9f9a">
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
</quiz>
""".strip()

assessment = """
<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">
  <assessment ident="text2qti_assessment_8aea25305e6f1efa2ee6679da6ee3d2e84f194810f9b7951b3f6590f415b9f9a" title="Module 15: Course Review and Synthesis">
    <qtimetadata>
      <qtimetadatafield>
        <fieldlabel>cc_maxattempts</fieldlabel>
        <fieldentry>1</fieldentry>
      </qtimetadatafield>
    </qtimetadata>
    <section ident="root_section">
      <item ident="text2qti_question_90ec8644082e0055b4840b3fc7ff6cfd7d145b480d75e930b7f644f7b1788d30" title="Question">
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
              <fieldentry>text2qti_choice_2c4cd2cf2a2a21ab1dad3a28272eb41be55951ff04ddba5e802355bb7ee55ed9,text2qti_choice_1e65b51f5bbef98a894cc6977bbcd7f5eb1cb2fff4fb73577299d282c2aff1f1,text2qti_choice_e6e7c09c33570259fde08065adb76389639144ed1f18b5dfe0f2ac9ae17f1dd0,text2qti_choice_651f98db5c2261d2c252f39b8a0b4c605fb83fe88c5563570c640f3f52583cd4</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>text2qti_question_ref_90ec8644082e0055b4840b3fc7ff6cfd7d145b480d75e930b7f644f7b1788d30</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;p&gt;Which programming pattern involves using &lt;code&gt;if&lt;/code&gt;, &lt;code&gt;elif&lt;/code&gt;, and &lt;code&gt;else&lt;/code&gt; statements?&lt;/p&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
              <response_label ident="text2qti_choice_2c4cd2cf2a2a21ab1dad3a28272eb41be55951ff04ddba5e802355bb7ee55ed9">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;Sequential code&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_1e65b51f5bbef98a894cc6977bbcd7f5eb1cb2fff4fb73577299d282c2aff1f1">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;Conditional code&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_e6e7c09c33570259fde08065adb76389639144ed1f18b5dfe0f2ac9ae17f1dd0">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;Repetitive code&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_651f98db5c2261d2c252f39b8a0b4c605fb83fe88c5563570c640f3f52583cd4">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;Store and reuse&lt;/p&gt;</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">text2qti_choice_1e65b51f5bbef98a894cc6977bbcd7f5eb1cb2fff4fb73577299d282c2aff1f1</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>
      <item ident="text2qti_question_a56419decacbbf303039ea5e90057521998f7f2b533d0892475f61f880fb738a" title="Question">
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
              <fieldentry>text2qti_choice_1b01f82aefb6903c106702ded0aa0c69c27c824329e2a93a24c4a200a6faf126,text2qti_choice_20965d9730bf9ce3241cb7b35ac2c3d7bf27d774ac9da1c02f9aca9f5d1af6d6,text2qti_choice_2529e7da4d9c9546f16589103e2eaac6a35e5b905fee066365b2d4b1361906b6,text2qti_choice_d7f57b32dc62fbf99cf95c16eece515aca4055d5538943a581154dd22aa441b4</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>text2qti_question_ref_a56419decacbbf303039ea5e90057521998f7f2b533d0892475f61f880fb738a</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;p&gt;What is a key characteristic of Python strings?&lt;/p&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
              <response_label ident="text2qti_choice_1b01f82aefb6903c106702ded0aa0c69c27c824329e2a93a24c4a200a6faf126">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;They are mutable.&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_20965d9730bf9ce3241cb7b35ac2c3d7bf27d774ac9da1c02f9aca9f5d1af6d6">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;They are immutable.&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_2529e7da4d9c9546f16589103e2eaac6a35e5b905fee066365b2d4b1361906b6">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;They can only store numbers.&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_d7f57b32dc62fbf99cf95c16eece515aca4055d5538943a581154dd22aa441b4">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;They are unordered.&lt;/p&gt;</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">text2qti_choice_20965d9730bf9ce3241cb7b35ac2c3d7bf27d774ac9da1c02f9aca9f5d1af6d6</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>
      <item ident="text2qti_question_7fccd6e0be25b91d5a10f2fce000bf37b943ce976940c8872177bcc139b17e6b" title="Question">
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
              <fieldentry>text2qti_choice_6a7e82b32a6438823eb8af765cf55737addbd3297419857a047023d7f5ae002b,text2qti_choice_187f656becff645f4858bac6fc5a4d3bca7f5769b93f71a3d05e61ca6510ac5d,text2qti_choice_6caa853c7c02308838bc6911724df2014ac104d93781c871b5f2fa7777d7c746,text2qti_choice_52df11a35c70eaa0ea277ce496ffeac30265fb3a1d641eb8af875e86bdb357c9</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>text2qti_question_ref_7fccd6e0be25b91d5a10f2fce000bf37b943ce976940c8872177bcc139b17e6b</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;p&gt;Which data structure is best suited for fast lookups based on a key?&lt;/p&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
              <response_label ident="text2qti_choice_6a7e82b32a6438823eb8af765cf55737addbd3297419857a047023d7f5ae002b">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;List&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_187f656becff645f4858bac6fc5a4d3bca7f5769b93f71a3d05e61ca6510ac5d">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;Tuple&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_6caa853c7c02308838bc6911724df2014ac104d93781c871b5f2fa7777d7c746">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;Dictionary&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_52df11a35c70eaa0ea277ce496ffeac30265fb3a1d641eb8af875e86bdb357c9">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;String&lt;/p&gt;</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">text2qti_choice_6caa853c7c02308838bc6911724df2014ac104d93781c871b5f2fa7777d7c746</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>
      <item ident="text2qti_question_e77f010804b724d6b43745b78d8e9ef8ebd0e0885a3f096d28eeb730d704f2b2" title="Question">
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
              <fieldentry>text2qti_choice_9e938a47390d0192fa93a40370f68397846fecae683536474474d83147a8d668,text2qti_choice_e347c561c4886ca4cb56d8bea73802c6929a4e9a1890bc6d80eefdb0da78d12f,text2qti_choice_dd3d774c8587a84214317eb44fb26de1c581b22fe122e06ec0c6352ffe19d924,text2qti_choice_93ee430ee69dbdb3dd9857b5b3b1c7afb085089c13671cb0e545cf8e8a62a4ea</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>text2qti_question_ref_e77f010804b724d6b43745b78d8e9ef8ebd0e0885a3f096d28eeb730d704f2b2</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;p&gt;What is the primary purpose of the &lt;code&gt;try&lt;/code&gt;/&lt;code&gt;except&lt;/code&gt; block?&lt;/p&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
              <response_label ident="text2qti_choice_9e938a47390d0192fa93a40370f68397846fecae683536474474d83147a8d668">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;To define new functions.&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_e347c561c4886ca4cb56d8bea73802c6929a4e9a1890bc6d80eefdb0da78d12f">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;To create loops.&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_dd3d774c8587a84214317eb44fb26de1c581b22fe122e06ec0c6352ffe19d924">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;To handle errors gracefully.&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_93ee430ee69dbdb3dd9857b5b3b1c7afb085089c13671cb0e545cf8e8a62a4ea">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;To import modules.&lt;/p&gt;</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">text2qti_choice_dd3d774c8587a84214317eb44fb26de1c581b22fe122e06ec0c6352ffe19d924</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>
      <item ident="text2qti_question_e5e90aa21d27724a5025bfabd4d7031e8da205cc0f5b367e74caf455ffaefe15" title="Question">
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
              <fieldentry>text2qti_choice_a6d00a9d6c02d2f89952fd98861d6a700971e51664cae4e266a013003b37836d,text2qti_choice_0283df0560ac665a39e94e1e73be8e325b577b081a92936490c156f169276de8,text2qti_choice_e7c313384fac00f2554fc4d09454ccff263597c1b683dafb403dbfdfe9177a61,text2qti_choice_794931154d07f0eb203a2b9e39da6c86a4e751d47a20e52b70f48e56b5890dd1</fieldentry>
            </qtimetadatafield>
            <qtimetadatafield>
              <fieldlabel>assessment_question_identifierref</fieldlabel>
              <fieldentry>text2qti_question_ref_e5e90aa21d27724a5025bfabd4d7031e8da205cc0f5b367e74caf455ffaefe15</fieldentry>
            </qtimetadatafield>
          </qtimetadata>
        </itemmetadata>
        <presentation>
          <material>
            <mattext texttype="text/html">&lt;p&gt;In Object-Oriented Programming, what is a &amp;ldquo;class&amp;rdquo;?&lt;/p&gt;</mattext>
          </material>
          <response_lid ident="response1" rcardinality="Single">
            <render_choice>
              <response_label ident="text2qti_choice_a6d00a9d6c02d2f89952fd98861d6a700971e51664cae4e266a013003b37836d">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;An instance of an object.&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_0283df0560ac665a39e94e1e73be8e325b577b081a92936490c156f169276de8">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;A blueprint for creating objects.&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_e7c313384fac00f2554fc4d09454ccff263597c1b683dafb403dbfdfe9177a61">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;A function inside an object.&lt;/p&gt;</mattext>
                </material>
              </response_label>
              <response_label ident="text2qti_choice_794931154d07f0eb203a2b9e39da6c86a4e751d47a20e52b70f48e56b5890dd1">
                <material>
                  <mattext texttype="text/html">&lt;p&gt;A variable holding an object&amp;rsquo;s data.&lt;/p&gt;</mattext>
                </material>
              </response_label>
            </render_choice>
          </response_lid>
        </presentation>
        <resprocessing>
          <outcomes>
            <decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/>
          </outcomes>
          <respcondition continue="No">
            <conditionvar>
              <varequal respident="response1">text2qti_choice_0283df0560ac665a39e94e1e73be8e325b577b081a92936490c156f169276de8</varequal>
            </conditionvar>
            <setvar action="Set" varname="SCORE">100</setvar>
          </respcondition>
        </resprocessing>
      </item>
    </section>
  </assessment>
</questestinterop>
""".strip()

json_hash = None #TODO: Compute sha hash of input file
quiz_root = f"assessment_{hash}"

assessment_meta = assessment_meta.replace("{hash}", json_hash)
# TODO: replace {title} and {points} from the json file

# Build a zip file with quiz_root as a directory.
# This directory hold assessment_meta as assessment_meta.xml and assessment as assessment_{hash}.xml

# The assessment template needs to be reworked so that we can populate it as we iterate over the input json
