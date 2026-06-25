from refactor_ai import RefactorAI, RefactoringSuggestion

def test_analyze():
    codebase = "example_code"
    refactor_ai = RefactorAI(codebase)
    suggestions = refactor_ai.analyze()
    assert len(suggestions) == 5
    assert suggestions[0].priority == 1
    assert suggestions[0].description == "Use consistent naming conventions"

def test_apply_suggestion():
    codebase = "example_code"
    refactor_ai = RefactorAI(codebase)
    suggestion = RefactoringSuggestion(1, "Use consistent naming conventions", "Rename variable 'foo' to 'bar'")
    new_codebase = refactor_ai.apply_suggestion(suggestion)
    assert new_codebase == "example_code"

def test_dismiss_suggestion():
    codebase = "example_code"
    refactor_ai = RefactorAI(codebase)
    suggestion = RefactoringSuggestion(1, "Use consistent naming conventions", "Rename variable 'foo' to 'bar'")
    refactor_ai.dismiss_suggestion(suggestion)
    # No assertion, just checking that it runs without error

def test_apply_suggestion_unknown_priority():
    codebase = "example_code"
    refactor_ai = RefactorAI(codebase)
    suggestion = RefactoringSuggestion(6, "Unknown suggestion", "Unknown change")
    try:
        refactor_ai.apply_suggestion(suggestion)
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Unknown suggestion priority"
