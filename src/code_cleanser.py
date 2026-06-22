import json
from dataclasses import dataclass
from difflib import Differ
from typing import List

@dataclass
class Refactoring:
    original_code: str
    refactored_code: str

class CodeCleanser:
    def __init__(self):
        self.refactorings = []

    def add_refactoring(self, refactoring: Refactoring):
        self.refactorings.append(refactoring)

    def get_diff_view(self, index: int) -> str:
        if index < 0 or index >= len(self.refactorings):
            raise IndexError("Index out of range")
        original_code = self.refactorings[index].original_code
        refactored_code = self.refactorings[index].refactored_code
        differ = Differ()
        diff = differ.compare(original_code.splitlines(), refactored_code.splitlines())
        return "\n".join(diff)

    def get_static_analysis_score(self, index: int) -> int:
        if index < 0 or index >= len(self.refactorings):
            raise IndexError("Index out of range")
        # Simple cyclomatic complexity calculation: count the number of conditional statements
        refactored_code = self.refactorings[index].refactored_code
        score = refactored_code.count("if") + refactored_code.count("elif") + refactored_code.count("else")
        return score

    def update_preview(self, index: int) -> None:
        # This method is a placeholder for updating the preview in real time
        pass
