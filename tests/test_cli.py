# tests/test_cli.py

from typer.testing import CliRunner

from bbarwik_ai_tools import __version__
from bbarwik_ai_tools.cli import app

runner = CliRunner()


def test_main_app():
    """Test that running the app with no command prints 'Hello World'."""
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Hello World" in result.stdout


def test_help_command():
    """Test the --help option."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout
    assert "A simple CLI that prints Hello World." in result.stdout


def test_version():
    """Test the --version option."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout
