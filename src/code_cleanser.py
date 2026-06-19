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
        with open(self.file_path, 'r') as file:
            tree = ast.parse(file.read())
            cleaned_code = ast.unparse(tree)
            # Ensure trailing newline is preserved
            if not cleaned_code.endswith('\n'):
                cleaned_code += '\n'
            return cleaned_code

    def get_changes(self, original_code: str, cleaned_code: str) -> List[str]:
        changes = []
        original_lines = original_code.splitlines()
        cleaned_lines = cleaned_code.splitlines()
        for i in range(max(len(original_lines), len(cleaned_lines))):
            if i >= len(original_lines):
                changes.append(f'+ {cleaned_lines[i]}')
            elif i >= len(cleaned_lines):
                changes.append(f'- {original_lines[i]}')
            elif original_lines[i] != cleaned_lines[i]:
                changes.append(f'- {original_lines[i]}')
                changes.append(f'+ {cleaned_lines[i]}')
        return changes

def main():
    parser = argparse.ArgumentParser(description='Code Cleanser')
    parser.add_argument('file_path', help='Path to the file or directory to clean')
    args = parser.parse_args()
    cleaner = CodeCleaner(args.file_path)
    original_code = open(args.file_path, 'r').read()
    cleaned_code = cleaner.clean_code()
    changes = cleaner.get_changes(original_code, cleaned_code)
    print('Cleaned Code:')
    print(cleaned_code)
    print('Changes:')
    for change in changes:
        print(change)

if __name__ == '__main__':
    main()
