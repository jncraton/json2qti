import json
import os
import zipfile
import subprocess
import pytest

def test_code_formatting():
    """Test that code blocks are properly formatted and escaped in QTI."""
    file_path = os.path.join(os.path.dirname(__file__), "code_quiz.json")
        
    subprocess.run(["python3", "json2qti.py", file_path], check=True)
    
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    expected_zip = f"{base_name}.zip"
    
    try:
        assert os.path.exists(expected_zip)
        
        with zipfile.ZipFile(expected_zip, 'r') as zf:
            file_list = zf.namelist()
            assessment_file = [f for f in file_list if f.endswith(".xml") and "assessment_meta" not in f][0]
            content = zf.read(assessment_file).decode("utf-8")
            
            # Verify code formatting
            # `print('hello')` -> <code>print('hello')</code>
            # Note: The single quotes might be escaped or not depending on html.escape implementation,
            # but < and > MUST be escaped in XML/HTML content unless they are part of tags we inserted.
            
            # We expect the `...` to be replaced by <code>...</code>
            # And inner < > to be &lt; &gt;
            
            # Check for question text
            # Original: What does `print('hello')` do?
            # Expected: What does <code>print(&#x27;hello&#x27;)</code> do? (or similar escaping)
            assert "<code>print(" in content
            
            # Check for answer text
            # Original: `<script>` tag
            # Expected: <code>&lt;script&gt;</code> tag
            assert "<code>&lt;script&gt;</code>" in content
            
            # Ensure the raw <script> didn't make it in (would be invalid/dangerous)
            assert "<script>" not in content

            # Verify multiline code formatting
            # ```\ndef foo():\n    pass\n``` -> <pre><code>\ndef foo():\n    pass\n</code></pre>
            assert "<pre><code>" in content
            assert "def foo():" in content
    finally:
         if os.path.exists(expected_zip):
            os.remove(expected_zip)
