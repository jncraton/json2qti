# json2qti

[![PyPI version](https://badge.fury.io/py/json2qti.svg)](https://badge.fury.io/py/json2qti)
[![Lint](https://github.com/jncraton/json2qti/actions/workflows/lint.yml/badge.svg)](https://github.com/jncraton/json2qti/actions/workflows/lint.yml)
[![Test](https://github.com/jncraton/json2qti/actions/workflows/test.yml/badge.svg)](https://github.com/jncraton/json2qti/actions/workflows/test.yml)

**Instantly convert simple JSON files into QTI import packages for your LMS.**

`json2qti` is a lightweight, zero-dependency tool designed to bridge the gap between AI-generated content and Learning Management Systems (Canvas, Blackboard, Moodle, Brightspace, etc.).

## 🚀 Why json2qti?

- **LLM Optimized:** The input JSON format is designed to be extremely token-efficient, making it perfect for generating quizzes with ChatGPT, Claude, or other LLMs.
- **Zero Dependencies:** Runs entirely on the Python standard library. No complex environment setup required.
- **Universal Compatibility:** Generates standard QTI v1.2 packages compatible with major LMS platforms.

## 📄 JSON Format

The input format is minimal by design.
1.  **Quiz Title:** The top-level key.
2.  **Questions:** Keys inside the object.
3.  **Answers:** A list of strings. **The first answer is always the correct one.** (Don't worry, `json2qti` shuffles them in the output file).

```json
{
  "Basic Math Quiz": {
    "What is 1+1?": ["2", "3", "4", "5"],
    "What is 1+2?": ["3", "4", "5", "6"]
  }
}
```

### Code Formatting
You can include inline code snippets by wrapping them in backticks (\`). This is useful for programming questions.

```json
{
  "Python Quiz": {
    "What does `print('hello')` output?": [
      "`hello` to stdout",
      "`hello` to stderr",
      "Nothing"
    ],
    "Which operator checks for equality?": [
      "`==`",
      "`=`",
      "`!=`"
    ]
  }
}
```

## 💻 Usage

### Quick Run (Recommended)
You can run it directly using `pipx` without installing anything globally:

```sh
pipx run json2qti quiz.json
```

### Manual Execution
Since the tool is a single file, you can also just download `json2qti.py` and run it:

```sh
python3 json2qti.py quiz.json
# Creates quiz.zip ready for LMS import
```

## 🛠️ Development

This project includes a test suite to ensure reliability. Tests are located in the `tests/` directory.

```sh
make test
```

## 📦 Dependencies

Just Python 3.
