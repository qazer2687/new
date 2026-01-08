#!/usr/bin/env python3
import sys
import shutil
import subprocess
from pathlib import Path

# This takes two arguments, the first is the template
# directory to use and the second is the project name.
if len(sys.argv) < 3:
  sys.exit("Usage: new <template-type> <project-name>")

template_type, project_name = sys.argv[1:3]
code_dir = Path.home() / "Code"
template_dir = code_dir / "templates" / template_type
project_dir = code_dir / project_name

# Check whether the template directory exists.
if not template_dir.is_dir():
  sys.exit(f"Template type '{template_type}' does not exist.")

# Check whether the project directory exists.
if project_dir.exists():
  sys.exit(f"A project with the name '{project_name}' already exists.")

# Copy the contents of the template directory to the new project folder.
shutil.copytree(template_dir, project_dir)

# Run direnv allow and suppress the output.
subprocess.run(["direnv", "allow"], cwd=project_dir, capture_output=True)