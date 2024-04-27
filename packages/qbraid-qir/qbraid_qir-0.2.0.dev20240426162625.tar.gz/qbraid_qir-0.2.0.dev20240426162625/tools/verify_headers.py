# Copyright (C) 2023 qBraid
#
# This file is part of the qBraid-SDK
#
# The qBraid-SDK is free software released under the GNU General Public License v3
# or later. You can redistribute and/or modify it under the terms of the GPL v3.
# See the LICENSE file in the project root or <https://www.gnu.org/licenses/gpl-3.0.html>.
#
# THERE IS NO WARRANTY for the qBraid-SDK, as per Section 15 of the GPL v3.

# pylint: skip-file

"""
Script to verify qBraid copyright file headers

"""
import os
import sys

# ANSI escape codes
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

header = """# Copyright (C) 2024 qBraid
#
# This file is part of the qBraid-SDK
#
# The qBraid-SDK is free software released under the GNU General Public License v3
# or later. You can redistribute and/or modify it under the terms of the GPL v3.
# See the LICENSE file in the project root or <https://www.gnu.org/licenses/gpl-3.0.html>.
#
# THERE IS NO WARRANTY for the qBraid-SDK, as per Section 15 of the GPL v3.
"""

header_2023 = header.replace("2024", "2023")

skip_files = []

failed_headers = []
fixed_headers = []


def should_skip(file_path: str, content: str) -> bool:
    if file_path in skip_files:
        return True

    if os.path.basename(file_path) == "__init__.py":
        return not content.strip()

    skip_header_tag = "# qbraid: skip-header"
    line_number = 0

    for line in content.splitlines():
        line_number += 1
        if 5 <= line_number <= 30 and skip_header_tag in line:
            return True
        if line_number > 30:
            break

    return False


def replace_or_add_header(file_path: str, fix: bool = False) -> None:
    with open(file_path, "r", encoding="ISO-8859-1") as f:
        content = f.read()

    if (
        content.startswith(header)
        or content.startswith(header_2023)
        or should_skip(file_path, content)
    ):
        return

    if not fix:
        failed_headers.append(file_path)
        return

    lines = content.splitlines()

    comment_lines = []
    first_skipped_line = None
    for index, line in enumerate(lines):
        if line.startswith("#"):
            comment_lines.append(line)
        else:
            first_skipped_line = index
            break

    new_content_lines = [header.rstrip("\r\n")] + lines[first_skipped_line:]
    new_content = "\n".join(new_content_lines) + "\n"

    with open(file_path, "w", encoding="ISO-8859-1") as f:
        f.write(new_content)

    fixed_headers.append(file_path)


def process_files_in_directory(directory: str, fix: bool = False) -> int:
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                replace_or_add_header(file_path, fix)
                count += 1
    return count


def display_help() -> None:
    help_message = """
    Usage: python verify_headers.py SRC [OPTIONS] ...

    This script checks for copyright headers at the specified path.
    If no flags are passed, it will indicate which files would be
    modified without actually making any changes.
    
    Options:
    --help      Display this help message and exit.
    --fix       Adds/modifies file headers as necessary.
    """
    print(help_message)
    sys.exit(0)


if __name__ == "__main__":
    if "--help" in sys.argv:
        display_help()

    # Check if at least two arguments are provided and the first argument is not a flag
    if len(sys.argv) < 2 or sys.argv[1].startswith("--"):
        print("Usage: python verify_headers.py SRC [OPTIONS] ...")
        sys.exit(1)

    script_directory = os.path.dirname(os.path.abspath(__file__))
    project_directory = os.path.abspath(os.path.join(script_directory, ".."))
    skip_files = [os.path.join(project_directory, file_path) for file_path in skip_files]

    fix = "--fix" in sys.argv
    files_and_dirs = [arg for arg in sys.argv[1:] if arg != "--fix"]

    checked = 0
    for item in files_and_dirs:
        full_path = os.path.join(project_directory, item)
        if os.path.isdir(full_path):
            checked += process_files_in_directory(full_path, fix)
        elif os.path.isfile(full_path) and full_path.endswith(".py"):
            replace_or_add_header(full_path, fix)
            checked += 1
        else:
            failed_headers.append(full_path)
            print(f"Directory not found: {full_path}")

    if not fix:
        if failed_headers:
            for file in failed_headers:
                print(f"failed {os.path.relpath(file)}")
            num_failed = len(failed_headers)
            s1, s2 = ("", "s") if num_failed == 1 else ("s", "")
            sys.stderr.write(f"\n{num_failed} file header{s1} need{s2} updating.\n")
            sys.exit(1)
        else:
            print("All file header checks passed!")

    else:
        for file in fixed_headers:
            print(f"fixed {os.path.relpath(file)}")
        num_fixed = len(fixed_headers)
        num_ok = checked - num_fixed
        s_fixed = "" if num_fixed == 1 else "s"
        s_ok = "" if num_ok == 1 else "s"
        print("\nAll done! ✨ 🚀 ✨")
        print(f"{num_fixed} header{s_fixed} fixed, {num_ok} header{s_ok} left unchanged.")
