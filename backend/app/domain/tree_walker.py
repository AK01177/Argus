import os

from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern


def get_files_to_parse(rep_path):
    gitignore_path = os.path.join(rep_path, ".gitignore")
    patterns = []

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            patterns = f.read().splitlines()

    patterns.append(".git/")

    spec = PathSpec.from_lines(GitWildMatchPattern, patterns)
    valid_files = []

    for root, dirs, files in os.walk(rep_path):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, rep_path)

            if not spec.match_file(relative_path):
                valid_files.append(full_path)

    return valid_files
