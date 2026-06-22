import pytest
from code_cleanser import CodeCleanser, Refactoring

def test_get_diff_view():
    code_cleanser = CodeCleanser()
    refactoring = Refactoring("original code", "refactored code")
    code_cleanser.add_refactoring(refactoring)
    diff_view = code_cleanser.get_diff_view(0)
    assert diff_view.startswith("- original code")
    assert diff_view.endswith("+ refactored code")

def test_get_static_analysis_score():
    code_cleanser = CodeCleanser()
    refactoring = Refactoring("original code", "if condition: refactored code")
    code_cleanser.add_refactoring(refactoring)
    score = code_cleanser.get_static_analysis_score(0)
    assert score == 1

def test_update_preview():
    code_cleanser = CodeCleanser()
    refactoring = Refactoring("original code", "refactored code")
    code_cleanser.add_refactoring(refactoring)
    code_cleanser.update_preview(0)
    # This test is a placeholder, as the update_preview method is not fully implemented

def test_get_diff_view_index_out_of_range():
    code_cleanser = CodeCleanser()
    refactoring = Refactoring("original code", "refactored code")
    code_cleanser.add_refactoring(refactoring)
    with pytest.raises(IndexError):
        code_cleanser.get_diff_view(1)

def test_get_static_analysis_score_index_out_of_range():
    code_cleanser = CodeCleanser()
    refactoring = Refactoring("original code", "refactored code")
    code_cleanser.add_refactoring(refactoring)
    with pytest.raises(IndexError):
        code_cleanser.get_static_analysis_score(1)
