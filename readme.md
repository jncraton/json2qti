# json2qti

Build LMS quizzes from simple json.

## Format

The JSON representation is as minimal as possible to allow for token-efficient generation and processing by LLMs. All questions are multiple choice. Questions are keys in an object. Answers are provided as a list of values. The first answer is always the correct choice. Generated quizzes will have answer shuffling enabled.

Here's an example:

```json
{
  "Basic Addition": {
    "What is 1+1?": ["2", "2", "2", "2"],
    "What is 1+2?": ["2", "2", "2", "2"]
  }
}
```

## Usage

```sh
python3 json2qti.py quiz.json # Produces quiz.zip QTI file
```

## Dependencies

This project has no dependencies beyond the Python standard library. The entire package is in a single file json2qti.py.
