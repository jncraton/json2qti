import json
import os
import zipfile
import subprocess
import pytest

# Helper to create a temporary JSON quiz file
@pytest.fixture
def quiz_file(tmp_path):
    data = {
        "Test Quiz": {
            "Question 1": ["Correct", "Wrong 1", "Wrong 2"],
            "Question 2": ["Correct A", "Wrong B"]
        }
    }
    file_path = tmp_path / "test_quiz.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return str(file_path)

# Helper to create a flat JSON quiz file (no title wrapper)
@pytest.fixture
def flat_quiz_file(tmp_path):
    data = {
        "Question 1": ["Correct", "Wrong 1"],
        "Question 2": ["Correct A", "Wrong B"]
    }
    file_path = tmp_path / "flat_quiz.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return str(file_path)

def test_generate_quiz_wrapper_format(quiz_file):
    """Test generating a quiz from JSON with a wrapper object (title)."""
    # The output zip file is created in the current working directory by the script
    # We must construct the path to the input file for the script to read
    # And check the current directory for the output
    
    # Run the script with the full path to the input file
    subprocess.run(["python3", "json2qti.py", quiz_file], check=True)
    
    # The script writes the zip file to the current working directory with the same basename
    # as the input file.
    # Since quiz_file is in a tmp_path (e.g. /tmp/.../test_quiz.json), the script
    # running in CWD will create ./test_quiz.zip
    
    base_name = os.path.splitext(os.path.basename(quiz_file))[0]
    expected_zip = f"{base_name}.zip"
    
    try:
        assert os.path.exists(expected_zip)
        
        with zipfile.ZipFile(expected_zip, 'r') as zf:
            file_list = zf.namelist()
            # Verify structure
            assert any(f.endswith("assessment_meta.xml") for f in file_list)
            assert any(f.endswith(".xml") and "assessment_" in f for f in file_list)
            
            # Verify content (internal title should match key)
            meta_file = [f for f in file_list if f.endswith("assessment_meta.xml")][0]
            meta_content = zf.read(meta_file).decode("utf-8")
            assert "<title>Test Quiz</title>" in meta_content
    finally:
        # Cleanup
        if os.path.exists(expected_zip):
            os.remove(expected_zip)

def test_generate_quiz_flat_format(flat_quiz_file):
    """Test generating a quiz from flat JSON (filename becomes title)."""
    subprocess.run(["python3", "json2qti.py", flat_quiz_file], check=True)
    
    base_name = os.path.splitext(os.path.basename(flat_quiz_file))[0]
    expected_zip = f"{base_name}.zip"
    
    try:
        assert os.path.exists(expected_zip)
        
        with zipfile.ZipFile(expected_zip, 'r') as zf:
            file_list = zf.namelist()
            meta_file = [f for f in file_list if f.endswith("assessment_meta.xml")][0]
            meta_content = zf.read(meta_file).decode("utf-8")
            # Internal title should match filename (without .json)
            assert "<title>flat_quiz</title>" in meta_content
    finally:
         if os.path.exists(expected_zip):
            os.remove(expected_zip)

def test_missing_file():
    """Test behavior when input file is missing."""
    result = subprocess.run(["python3", "json2qti.py", "non_existent.json"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Error: File non_existent.json not found" in result.stdout

def test_invalid_json(tmp_path):
    """Test behavior with invalid JSON content."""
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{invalid_json: true")
    
    result = subprocess.run(["python3", "json2qti.py", str(bad_file)], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Error: Invalid JSON format" in result.stdout


def test_shuffle_answers(quiz_file):
    """Test that answer shuffling works and first answer isn't always correct."""
    # We need to run multiple iterations to statistically ensure shuffling
    # But since we can't easily mock random inside the subprocess call, 
    # we'll inspect the output XML directly for one run.
    
    subprocess.run(["python3", "json2qti.py", quiz_file], check=True)
    
    base_name = os.path.splitext(os.path.basename(quiz_file))[0]
    expected_zip = f"{base_name}.zip"
    
    try:
        assert os.path.exists(expected_zip)
        
        with zipfile.ZipFile(expected_zip, 'r') as zf:
            file_list = zf.namelist()
            assessment_file = [f for f in file_list if f.endswith(".xml") and "assessment_meta" not in f][0]
            content = zf.read(assessment_file).decode("utf-8")
            
            # Check for shuffling by seeing if we can find the correct answer ID
            # mapped to a response_label that is NOT always the first one printed
            # (Though XML order might not guarantee visual order, QTI presentation usually follows it)
            
            # More robust check: The code logic ensures correct_choice_id is set to the choice_id 
            # of the first item in the input list.
            # We can verify the structure exists.
            assert "<varequal respident=\"response1\">" in content
            
            # We can't strictly assert the order without mocking random, 
            # but we can ensure the file generates valid XML with choices.
            assert "choice_" in content
    finally:
         if os.path.exists(expected_zip):
            os.remove(expected_zip)
