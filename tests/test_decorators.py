from src.decorators import log


def test_log_call_decorator(capsys):

    @log(filename=None)
    def test_func():
        return 10

    test_func()
    captured = capsys.readouterr()
    assert "test_func ok" in captured.out
