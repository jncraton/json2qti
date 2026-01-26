# json2qti

[![PyPI version](https://badge.fury.io/py/json2qti.svg)](https://badge.fury.io/py/json2qti)
[![Lint](https://github.com/jncraton/json2qti/actions/workflows/lint.yml/badge.svg)](https://github.com/jncraton/json2qti/actions/workflows/lint.yml)
[![Test](https://github.com/jncraton/json2qti/actions/workflows/test.yml/badge.svg)](https://github.com/jncraton/json2qti/actions/workflows/test.yml)

Convert JSON files into QTI import packages.

json2qti converts token-efficient JSON quiz data into QTI v1.2 packages compatible with Canvas, Blackboard, Moodle, and Brightspace.

## Features

- LLM Optimized: Token-efficient JSON format.
- Zero Dependencies: Uses only the Python standard library.
- Universal Compatibility: Generates standard QTI v1.2 packages.

## JSON Format

1. Quiz Title: Top-level key.
2. Questions: Keys inside the object.
3. Answers: List of strings. The first answer is the correct one (shuffled in the output).

```json
{
  "Basic Math Quiz": {
    "What is 1+1?": ["2", "3", "4", "5"],
    "What is 1+2?": ["3", "4", "5", "6"]
  }
}
```

<details>
<summary>Code Formatting</summary>

Include code snippets using markdown syntax:

*   Inline Code: Wrap text in single backticks (`).
*   Block Code: Wrap text in triple backticks (```).

```json
{
  "Python Quiz": {
    "What does `print('hello')` output?": [
      "`hello` to stdout",
      "`hello` to stderr",
      "Nothing"
    ],
    "What does this function do?\n```\ndef add(a, b):\n    return a + b\n```": [
      "Returns the sum of two numbers",
      "Returns the product of two numbers",
      "Prints the numbers"
    ]
  }
}
```
</details>

## Usage

### Using pipx

```sh
pipx run json2qti quiz.json
```

<details>
<summary>Manual Execution</summary>

```sh
python3 json2qti.py quiz.json
# Creates quiz.zip ready for LMS import
```
</details>
