# Contributing to Python-AI-Utils

First off, thank you for considering contributing to Python-AI-Utils! It's people like you that make this project a great tool.

## How Can I Contribute?

### Reporting Bugs

This is one of the simplest ways to contribute. If you find a bug, please report it by opening an issue on GitHub. Please include as much detail as possible, including:

- A clear and descriptive title.
- A description of the steps to reproduce the bug.
- The expected behavior and what you observed instead.
- Your environment details (OS, Python version, etc.).

### Suggesting Enhancements

If you have an idea for a new feature or an improvement to an existing one, please open an issue to discuss it. This allows us to coordinate and ensure your idea fits with the project's goals.

### Pull Requests

The most direct way to contribute is by submitting a pull request. Here's how to do it:

1.  **Fork the repository** and create your branch from `main`.
2.  **Set up your environment**: It's recommended to use a virtual environment.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
3.  **Make your changes**: Add your new feature or fix the bug.
4.  **Add tests**: If you're adding a new feature, please include tests for it. If you're fixing a bug, add a test that catches the bug.
5.  **Ensure all tests pass**: Run the test suite to make sure you haven't broken anything.
    ```bash
    pytest
    ```
6.  **Update the documentation**: If your changes affect the documentation, please update it accordingly. This includes the `README.md` and any relevant docstrings.
7.  **Submit the pull request**: Push your changes to your fork and submit a pull request to the `main` branch of the `Python-AI-Utils` repository.

When you submit a pull request, please provide a clear description of the changes you've made and why you've made them.

## Styleguides

We use `black` for code formatting and `flake8` for linting. Please make sure your code adheres to these standards before submitting a pull request.

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior.
