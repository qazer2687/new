#!/usr/bin/env python3
import sys
import shutil
import subprocess
from pathlib import Path

# This takes two arguments, the first is the template
# directory to use and the second is the project name.
if len(sys.argv) < 4:
  sys.exit("Usage: new <template> <project-name> <directory")

template, project, directory = sys.argv[1:4]

templateDirectory = Path("./templates");
projectLocation = Path(directory);

if not templateDirectory.is_dir():
  sys.exit(f"Template directory does not exist.")
elif not Path(templateDirectory / template).is_dir():
  sys.exit(f"Template '{template}' does not exist.")

if projectLocation.exists():
  sys.exit(f"A project with the name '{project}' already exists.")

shutil.copytree(templateDirectory / template, projectLocation)

subprocess.run(["direnv", "allow"], cwd=projectLocation, capture_output=True)