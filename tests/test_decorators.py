from src.decorators import log


def test_log_console_output_no_error(capsys):
    '''Тест вывода в консоль для случая, когда функция не вызовет ошибку и нет записи в файл'''

    @log(filename=None)
    def test_func():
        return 10

    test_func()
    captured = capsys.readouterr()
    assert "test_func ok" in captured.out

def test_log_file_output_no_error(capsys):
    '''Тест вывода в консоль для случая, когда функция не вызовет ошибку и нет записи в файл'''

    @log(filename='filename.txt')
    def test_func():
        return 10

    test_func()
    captured = capsys.readouterr()
    assert captured.out == ""
