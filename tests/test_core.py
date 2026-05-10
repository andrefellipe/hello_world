import hello_world.core


def test_say_hello_default() -> None:
    assert hello_world.core.say_hello() == "Hello, World!"


def test_say_hello_custom() -> None:
    assert hello_world.core.say_hello("Andre") == "Hello, Andre!"
