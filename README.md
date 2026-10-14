# Password Strength Checker

A Python cybersecurity project that evaluates basic password characteristics and provides feedback about potential weaknesses.

## Features

- Scores passwords against five criteria:
  - Minimum length of 12 characters
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters
- Warns when a password matches a small list of common passwords.
- Detects characters repeated five or more times.
- Provides feedback about missing password criteria.
- Handles empty input.
- Includes automated unit tests using Python's `unittest` framework.

## Technologies Used

- Python
- unittest

## How to Run

Make sure Python is installed on your computer.

Run the password checker:

```bash
python password_checker.py
```

Run the automated tests:

```bash
python -m unittest test_password_checker.py
```

## What I Learned

While building this project, I practised:

- Writing and calling Python functions
- Using conditional statements and loops
- Working with strings, lists and Boolean values
- Returning multiple values from a function
- Handling invalid user input
- Writing and running automated unit tests

## Limitations

This project uses a basic scoring system for educational purposes. A high score does not guarantee that a password is secure. The common-password list is limited, and the program does not check for breached passwords or password reuse.

## Future Improvements

- Expand the common-password list.
- Add more automated tests for edge cases.
- Improve password-strength analysis.
- Explore checking passwords against a reputable breach-checking service using a privacy-preserving method.
