from hello_world import say_hello


def test_say_hello_default() -> None:
    assert say_hello() == "Hello, World!"


def test_say_hello_custom() -> None:
    assert say_hello("Andre") == "Hello, Andre!"
