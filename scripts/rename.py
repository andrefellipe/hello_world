import os
import sys
from pathlib import Path

if len(sys.argv) != 3:
    print(
        "Usage: poetry run python scripts/rename.py "
        "<snake_case_name> <kebab-case-name>"
    )
    sys.exit(1)

snake_name = sys.argv[1]
kebab_name = sys.argv[2]

# Directories to safely ignore
ignore_dirs = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "mutants",
}

print("🔍 Scanning codebase for 'hello_world' and 'hello-world-andrefellipe'...")

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        if file.endswith((".py", ".toml", ".md", ".yml", ".yaml", "Makefile")):
            filepath = Path(root) / file
            try:
                content = filepath.read_text(encoding="utf-8")
                if "hello_world" in content or "hello-world-andrefellipe" in content:
                    content = content.replace("hello_world", snake_name)
                    content = content.replace("hello-world-andrefellipe", kebab_name)
                    filepath.write_text(content, encoding="utf-8")
                    print(f"  📝 Updated: {filepath}")
            except UnicodeDecodeError:
                pass

# Rename the core source directory
src_dir = Path("src/hello_world")
if src_dir.exists():
    src_dir.rename(Path(f"src/{snake_name}"))
    print(f"  📁 Renamed directory: src/hello_world -> src/{snake_name}")

print(f"\n✅ Template successfully reconfigured for: {kebab_name}")
print(
    "⚠️  Note: Remember to delete this script (rm -rf scripts/) "
    "before committing your new project."
)
