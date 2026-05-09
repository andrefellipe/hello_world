from nox_poetry import session

# Define the Python versions we want to support
PYTHON_VERSIONS = ["3.10", "3.11", "3.12"]


@session(python=PYTHON_VERSIONS)
def tests(session):
    """Run the test suite across multiple Python versions."""
    # Install the package and test dependencies via Poetry
    session.install(".", "pytest", "pytest-cov")

    # Run the tests
    session.run("pytest", "--cov=hello_world", "--cov-report=term-missing")
