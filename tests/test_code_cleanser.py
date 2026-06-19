import pytest
from code_cleanser import CodeCleaner

def test_clean_code(tmp_path):
    file_path = tmp_path / 'test.py'
    with open(file_path, 'w') as file:
        file.write('def test():\n    pass\n')
    cleaner = CodeCleaner(str(file_path))
    cleaned_code = cleaner.clean_code()
    assert cleaned_code == 'def test():\n    pass\n'

def test_get_changes(tmp_path):
    file_path = tmp_path / 'test.py'
    with open(file_path, 'w') as file:
        file.write('def test():\n    pass\n')
    cleaner = CodeCleaner(str(file_path))
    original_code = 'def test():\n    pass\n'
    cleaned_code = 'def test():\n    pass\n'
    changes = cleaner.get_changes(original_code, cleaned_code)
    assert changes == []

def test_get_changes_with_diff(tmp_path):
    file_path = tmp_path / 'test.py'
    with open(file_path, 'w') as file:
        file.write('def test():\n    pass\n')
    cleaner = CodeCleaner(str(file_path))
    original_code = 'def test():\n    pass\n'
    cleaned_code = 'def test():\n    print("Hello")\n'
    changes = cleaner.get_changes(original_code, cleaned_code)
    assert changes == ['-     pass', '+     print("Hello")']

def test_main(tmp_path, capsys):
    file_path = tmp_path / 'test.py'
    with open(file_path, 'w') as file:
        file.write('def test():\n    pass\n')
    import sys
    sys.argv = ['code_cleanser.py', str(file_path)]
    from code_cleanser import main
    main()
    captured = capsys.readouterr()
    assert 'Cleaned Code:' in captured.out
    assert 'Changes:' in captured.out
