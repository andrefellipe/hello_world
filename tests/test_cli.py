from typer.testing import CliRunner

from hello_world.cli import app

runner = CliRunner()


def test_cli_default() -> None:
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Hello, World!" in result.stdout


def test_cli_custom() -> None:
    result = runner.invoke(app, ["--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.stdout
