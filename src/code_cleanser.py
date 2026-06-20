import argparse
import ast
import dataclasses
import json
import os
from typing import List

@dataclasses.dataclass
class CodeCleaner:
    file_path: str

    def clean_code(self) -> str:
        try:
            with open(self.file_path, 'r') as file:
                tree = ast.parse(file.read())
                cleaned_code = ast.unparse(tree)
                return cleaned_code
        except FileNotFoundError:
            raise ValueError(f"File {self.file_path} not found")
        except SyntaxError:
            raise ValueError(f"Invalid syntax in file {self.file_path}")

    def get_changes(self, original_code: str, cleaned_code: str) -> str:
        changes = []
        for line in original_code.splitlines():
            if line not in cleaned_code.splitlines():
                changes.append(f"- {line}")
        for line in cleaned_code.splitlines():
            if line not in original_code.splitlines():
                changes.append(f"+ {line}")
        return "\n".join(changes)

def main():
    parser = argparse.ArgumentParser(description="Code Cleanser")
    parser.add_argument("file_path", help="Path to the file or directory to clean")
    args = parser.parse_args()
    cleaner = CodeCleaner(args.file_path)
    try:
        original_code = open(args.file_path, 'r').read()
        cleaned_code = cleaner.clean_code()
        changes = cleaner.get_changes(original_code, cleaned_code)
        print("Cleaned Code:")
        print(cleaned_code)
        print("\nChanges:")
        print(changes)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
