# Contributing to Hello World

   We love your input! Here is how to set up your local environment to contribute.

   ## Local Development Setup
   1. Install Poetry if you haven't already.
   2. Clone the repository and install dependencies:
      `poetry install`
   3. Install the pre-commit hooks to automatically format your code:
      `poetry run pre-commit install`

   ## Testing
   Before submitting a Pull Request, ensure all tests pass across all Python versions using Nox:
   `poetry run nox`
