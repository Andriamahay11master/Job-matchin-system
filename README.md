# Job-matching-system

AI resume and job matching prototype that compares resumes and job descriptions to suggest candidate-job fits.

## Overview

- Small prototype demonstrating parsing and matching of resumes to job postings.
- Includes simple preprocessing, a matcher component, and unit tests.

## Quickstart

1. Create and activate a Python virtual environment:

   Windows:

   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

2. (Optional) Install dependencies if your project provides a `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main app (if applicable) or run the tests:

   ```bash
   python app.py
   pytest
   ```

## Project Structure

- `app.py`  optional top-level runner
- `back/`  core modules and tests:
  - `preprocessing.py`  text preprocessing helpers
  - `matcher.py`  main matching logic
  - `evaluation.py`  evaluation helpers
  - `test_preprocessing.py`, `test_matcher.py`  unit tests
- `data/`  example job and resume text files

## Usage

Place job descriptions under `data/jobs/` and resumes under `data/resumes/`. Use the functions in `back/matcher.py` to run matching between documents. The tests in `back/` provide examples of how the modules are used.

## Running Tests

Run from the repository root:

```bash
pytest
```

## Notes

- This repository is a prototype; adapt preprocessing and matching logic for production use.
- If you want, I can add a `requirements.txt` and a short example script showing matcher usage.

