import pytest
from code_cleanser import CodeCleaner

def test_clean_code(tmp_path):
    file_path = tmp_path / "test.py"
    file_path.write_text("print('Hello World')")
    cleaner = CodeCleaner(str(file_path))
    cleaned_code = cleaner.clean_code()
    assert cleaned_code == "print('Hello World')"

def test_get_changes(tmp_path):
    file_path = tmp_path / "test.py"
    file_path.write_text("print('Hello World')\nprint('Goodbye World')")
    cleaner = CodeCleaner(str(file_path))
    original_code = file_path.read_text()
    cleaned_code = cleaner.clean_code()
    changes = cleaner.get_changes(original_code, cleaned_code)
    assert changes == ""

def test_clean_code_invalid_syntax(tmp_path):
    file_path = tmp_path / "test.py"
    file_path.write_text("print('Hello World'\n")
    cleaner = CodeCleaner(str(file_path))
    with pytest.raises(ValueError):
        cleaner.clean_code()

def test_clean_code_file_not_found():
    cleaner = CodeCleaner("non_existent_file.py")
    with pytest.raises(ValueError):
        cleaner.clean_code()

def test_main(tmp_path, capsys):
    file_path = tmp_path / "test.py"
    file_path.write_text("print('Hello World')")
    import sys
    sys.argv = ["code_cleanser.py", str(file_path)]
    from code_cleanser import main
    main()
    captured = capsys.readouterr()
    assert "Cleaned Code:" in captured.out
    assert "Changes:" in captured.out

def test_main_invalid_syntax(tmp_path, capsys):
    file_path = tmp_path / "test.py"
    file_path.write_text("print('Hello World'\n")
    import sys
    sys.argv = ["code_cleanser.py", str(file_path)]
    from code_cleanser import main
    main()
    captured = capsys.readouterr()
    assert "Error: Invalid syntax" in captured.out
