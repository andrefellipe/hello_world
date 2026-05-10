"""Core business logic for the hello_world package."""


def say_hello(name: str | None = None) -> str:
    """Generate a friendly greeting string.

    Args:
        name: The name of the person to greet. Defaults to None.

    Returns:
        A formatted greeting string.
    """
    actual_name = name or "World"
    return f"Hello, {actual_name}!"
