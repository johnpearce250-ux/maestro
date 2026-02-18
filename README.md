# Text Processing Project

A simple Python project for Software Development Basics class that demonstrates fundamental programming concepts including functions, string manipulation, and data processing.

## Overview

This project provides basic text processing utilities including text sanitization, word counting, and report generation. It's designed as an educational example to practice function definition, parameter passing, and return values.

## Features

- **Text Sanitization**: Clean and normalize text by removing leading/trailing whitespace and converting to lowercase
- **Word Counting**: Count the number of words in processed text
- **Report Formatting**: Generate formatted output with word count statistics

## Functions

### `sanitize(text)`
Cleans the input text by stripping whitespace and converting to lowercase.

**Parameters:**
- `text` (str): The input text to sanitize

**Returns:**
- (str): A stripped and lowercased version of the text

**Example:**
```python
sanitize("   Hello there, John! How are you today?   ")
# Returns: "hello there, john! how are you today?"
```

### `word_count(text)`
Counts the number of words in the provided text.

**Parameters:**
- `text` (str): The input text to analyze

**Returns:**
- (int): The number of words in the text

**Example:**
```python
word_count("hello there john how are you today")
# Returns: 7
```

### `format_report(count)`
Generates a formatted string reporting the word count.

**Parameters:**
- `count` (int): The number of words to report

**Returns:**
- (str): A formatted report string

**Example:**
```python
format_report(7)
# Returns: "The text contains 7 words."
```

## Usage

Run the program with:

```bash
python main.py
```

### Example Output

```
The text contains 7 words.
```

## Learning Objectives

This project demonstrates:
- Function definition and organization
- String methods (`.strip()`, `.lower()`, `.split()`)
- Function parameters and return values
- Main function pattern with `if __name__ == '__main__':`
- Basic text processing and data manipulation

## Requirements

- Python 3.x

## Author

Created for Software Development Basics class
