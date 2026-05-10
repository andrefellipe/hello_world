"""Property-based tests for the hello_world package."""

from hypothesis import given
from hypothesis import strategies as st

from hello_world.core import say_hello


@given(st.text())
def test_say_hello_never_crashes_with_any_string(name: str) -> None:
    """
    Ensure say_hello never crashes, regardless of what string is passed.

    Hypothesis will generate hundreds of crazy strings (emojis, null bytes,
    massive lengths) and inject them into the 'name' parameter automatically.
    """
    result = say_hello(name)

    # 1. It should always return a string
    assert isinstance(result, str)

    # 2. The string should always start with "Hello, "
    assert result.startswith("Hello, ")

    # 3. If the string isn't empty, the name should be in the output
    if name:
        assert name in result
