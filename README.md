# Slint Python Template

A template for a Python application that's using Slint for the user interface.

## About

This template helps you get started developing a Python application with Slint as toolkit
for the user interface. It demonstrates the integration between the `.slint` UI markup and
Python code, how to trigger react to callbacks, get and set properties and use basic widgets.

## Prerequisites

In order to use this template and build a Python application, you need to install a few tools:

 * [Python 3](https://python.org/)
 * [uv](https://docs.astral.sh/uv/)

## Usage

1. Download and extract the [ZIP archive of this repository](https://github.com/slint-ui/slint-python-template/archive/refs/heads/main.zip).
2. Rename the extracted directory and change into it:
    ```
    mv slint-python-template-main my-project
    cd my-project
    ```
3. Run the application binary
    ```
    uv run main.py
    ```

We recommend using an IDE for development, along with our [LSP-based IDE integration for `.slint` files](https://github.com/slint-ui/slint/blob/master/tools/lsp/README.md). You can also load this project directly in [Visual Studio Code](https://code.visualstudio.com) and install our [Slint extension](https://marketplace.visualstudio.com/items?itemName=Slint.slint).

## Next Steps

We hope that this template helps you get started and you enjoy exploring making user interfaces with Slint. To learn more
about the Slint APIs and the `.slint` markup language check out our [online documentation](https://docs.slint.dev/latest/docs/python/slint).