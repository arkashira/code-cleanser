import json
from dataclasses import dataclass
from typing import List

@dataclass
class RefactoringSuggestion:
    priority: int
    description: str
    proposed_change: str

class RefactorAI:
    def __init__(self, codebase: str):
        self.codebase = codebase

    def analyze(self) -> List[RefactoringSuggestion]:
        # Simple analysis for demonstration purposes
        suggestions = [
            RefactoringSuggestion(1, "Use consistent naming conventions", "Rename variable 'foo' to 'bar'"),
            RefactoringSuggestion(2, "Remove unused imports", "Remove import 'unused_module'"),
            RefactoringSuggestion(3, "Simplify conditional statements", "Replace 'if-else' with 'ternary operator'"),
            RefactoringSuggestion(4, "Use type hints", "Add type hint for function 'example_function'"),
            RefactoringSuggestion(5, "Avoid duplicated code", "Extract method 'duplicated_code'"),
        ]
        return suggestions

    def apply_suggestion(self, suggestion: RefactoringSuggestion) -> str:
        # Simple application of suggestion for demonstration purposes
        if suggestion.priority == 1:
            return self.codebase.replace("foo", "bar")
        elif suggestion.priority == 2:
            return self.codebase.replace("import unused_module", "")
        elif suggestion.priority == 3:
            return self.codebase.replace("if-else", "ternary operator")
        elif suggestion.priority == 4:
            return self.codebase.replace("def example_function", "def example_function -> None")
        elif suggestion.priority == 5:
            return self.codebase.replace("duplicated_code", "extracted_method")
        else:
            raise ValueError("Unknown suggestion priority")

    def dismiss_suggestion(self, suggestion: RefactoringSuggestion) -> None:
        # Simple dismissal of suggestion for demonstration purposes
        print(f"Suggestion {suggestion.priority} dismissed")
