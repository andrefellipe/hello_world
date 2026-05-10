#!/bin/bash

OUTPUT="codebase_snapshot.txt"

echo "Dumping folder structure and code to $OUTPUT..."

# 1. Capture the structural tree (ignoring noisy folders)
echo "==========================================" >$OUTPUT
echo "FOLDER STRUCTURE" >>$OUTPUT
echo "==========================================" >>$OUTPUT
tree -a -I '.venv|.git|__pycache__|.pytest_cache|.mypy_cache|.ruff_cache|.nox|mutants|dist' >>$OUTPUT
echo -e "\n\n" >>$OUTPUT

# 2. Capture the actual code (Python files, configs, Makefiles, workflows)
echo "==========================================" >>$OUTPUT
echo "SOURCE CODE" >>$OUTPUT
echo "==========================================" >>$OUTPUT

# Find relevant files, exclude noisy directories, sort them, and append their contents
find . -type f \
  \( -name "*.py" -o -name "*.toml" -o -name "*.cfg" -o -name "Makefile" -o -name "*.yml" -o -name "*.yaml" \) \
  -not -path "*/\.venv/*" \
  -not -path "*/\.git/*" \
  -not -path "*/\.nox/*" \
  -not -path "*/__pycache__/*" \
  -not -path "*/\.pytest_cache/*" \
  -not -path "*/\.mypy_cache/*" \
  -not -path "*/\.ruff_cache/*" \
  -not -path "*/mutants/*" | sort | while read -r file; do

  echo -e "\n\n---> FILE: $file <---" >>$OUTPUT
  cat "$file" >>$OUTPUT
done

echo "Done! You can now upload $OUTPUT."
