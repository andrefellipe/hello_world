def say_hello(name: str | None = None) -> str:
    """Returns a greeting string."""
    actual_name = name or "World"
    return f"Hello, {actual_name}!"
