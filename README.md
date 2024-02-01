# Typespeed_Analyzer

TypeSpeed Analyzer is a Python script designed to help users assess their typing speed and accuracy by analyzing typing test results from MonkeyType, a popular typing practice platform. The script calculates and presents valuable metrics, including Words Per Minute (WPM) per 100 words typed despite test length.

# MonkeyType WPM Calculator

This Python script calculates the average Words Per Minute (WPM) from a MonkeyType typing test results CSV file. MonkeyType is a popular typing test platform.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [CSV File Format](#csv-file-format)
- [License](#license)

## Introduction

MonkeyType is a fun and educational platform to improve your typing skills by typing quotes from various sources. This repository contains a Python script that can analyze MonkeyType typing test results stored in a CSV file and calculate the average WPM for every 100 words.

## Requirements

To use this MonkeyType WPM Calculator, you'll need:

- Python 3.6 or higher installed on your system.

## Usage

1. Clone this repository to your local machine or download the script `calculate_wpm.py`.

2. Make sure you have Python 3.6 or higher installed.

3. Create a CSV file containing MonkeyType typing test results in the specified format (see [CSV File Format](#csv-file-format)).

4. Modify the script if needed by specifying the correct path to your CSV file.

5. Run the script:

   ```bash
   python calculate_wpm.py
   ```
## CSV File Format
The CSV file should have the following format:

```
testId|correct|wpm|totalTyped|testDuration|testDurationReal|quoteLength|errors|errorsTotal|quoteLengthText|quoteLengthShort|quoteLengthTextShort|quoteLengthLong|quoteLengthTextLong|quoteType|wordType|wordTypeShort|wordTypeLong|englishLetter|accent|version|textLength|date
```

- `correct`: Boolean indicating if the test was completed correctly (true or false).
- `wpm`: Words Per Minute.
- `totalTyped`: Total characters typed.
- `testDuration`: Duration of the test in milliseconds.
- `testDurationReal`: Real test duration in milliseconds.
- `quoteLength`: Total length of the quote.
- `errors`: Number of errors made during the test.
- `errorsTotal`: Total errors made.
- `quoteLengthText`: Length of the quote text.
- `quoteLengthShort`: Short quote length.
- `quoteLengthTextShort`: Short quote text length.
- `quoteLengthLong`: Long quote length.
- `quoteLengthTextLong`: Long quote text length.
- `quoteType`: Type of quote.
- `wordType`: Type of word.
- `wordTypeShort`: Short word type.
- `wordTypeLong`: Long word type.
- `englishLetter`: Boolean indicating if the text contains English letters.
- `accent`: Accent used.
- `version`: Version of MonkeyType.
- `textLength`: Length of the text.
- `date`: Date timestamp.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

