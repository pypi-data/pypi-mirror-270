# Dev Assistant

Welcome to the [Dev Assistant](https://devassistant.tonet.dev) project.

## What is it?

[Dev Assistant](https://devassistant.tonet.dev) is a *GPTs*, a ([tailored version of ChatGPT](https://openai.com/chatgpt#do-more-with-gpts)) that can assist developers by executing tasks directly in our development environment. GPTs are a new way for anyone to create a tailored version of ChatGPT to be more helpful in their daily life, at specific tasks, at work, or at home. For more information about GPTs, please refer to [OpenAI's blog post](https://openai.com/blog/introducing-gpts).

This repository contains the Dev Assistant CLI, a Python package that serves as the core component of the project. It receives instructions from Dev Assistant GPT, executes them locally, and sends the response back.

## Features

Dev Assistant CLI is designed to streamline your development process by offering a range of functionalities:

- **File Management**: Create, read, update, and delete files. List the contents of a directory. You can manage your files without leaving your conversation with Dev Assistant GPT.

- **Git Version Control**: Initialize a Git repository, add changes to the staging area, commit changes, and push changes to a remote repository. Get the status of the Git repository. You can manage your Git repositories directly through Dev Assistant GPT.

- **Terminal Commands Execution**: Execute commands directly in the terminal. You can run any command in your terminal directly from Dev Assistant GPT.

## Requirements

- 📓 Python 3.10+
- 📓 Pip and Poetry
- 💸 ChatGPT Plus subscription _(for custom GPTs access)_
- ⭐ [Dev Assistant account](https://devassistant.tonet.dev)

## Installation

- Create a Dev Assistant account at [devassistant.tonet.dev](https://devassistant.tonet.dev)
- Generate a token at [https://devassistant.tonet.dev/user/api-tokens](https://devassistant.tonet.dev/user/api-tokens) for Dev Assistant GPT and save it. You will need it later.
- Install the local client:
  - [Install Python](https://www.python.org/downloads/)
  - Run `pip install dev-assistant-client` in your terminal

## Usage

Once installed, just run the following:

```bash
dev-assistant
```

If the CLI is not already authenticated, it will open a browser window where you will be provided with a token. Copy the token including the pipe, and return to the terminal.

If everything runs well, you will see the Dev Assistant CLI presentation and a unique _CLIENT ID_, like this:

```

        ╭─────╮   Dev Assistant
        │ >_< │   v0.2.46
        ╰─────╯   https://devassistant.tonet.dev

›       Connecting...           Connected!
›       CLIENT ID:              6a35a11c-f34e-4e30-be46-a9ac4d0f5ac7
›       WebSockets...           Connected!
›       Private channel...      Connected!
›       Ready!  Listening for instructions...
›       

```

You can stop the client just doing a `CRTL+C` in the terminal at any time.

## Commands

Go to [Dev Assistant GPT](https://chat.openai.com/g/g-Qa01WfuKG-dev-assistant) and start a conversation. You can ask for help with the commands, or just let Dev Assistant GPT discover it by itself. It will ask you to login if you are not already logged in.

You can now ask Dev Assistant GPT to do things like:

- Create a new file called `my-file.txt` on my Desktop
- Read a file called `other-file.yml`
- Update a file
- Delete a file
- List the contents of a directory
- Initialize a Git repository
- Add changes to the staging area
- Commit changes
- Push changes to a remote repository
- Get the status of the Git repository
- Execute a command in the terminal
... and more!

## Versioning

To update the version of the package, follow these steps:

1. Commit your changes with a descriptive message.
2. Create a git tag with the format `vX.Y.Z` where `X.Y.Z` is the new version number.
3. Push your changes and the new tag to the repository.

The GitHub Actions workflow will automatically deploy the new version to PyPi when a new tag is detected.

## Contributing

We welcome contributions! If you have an idea for an improvement or have found a bug, please open an issue. Feel free to fork the repository and submit a pull request if you'd like to contribute code. Please follow the code style and conventions used in the existing codebase.

## Development

- Fork the repository
- Clone your fork
- Go to the project folder
- Install Dev Assistant Client in local mode with `pip install -e .` or `poetry install`
- Run `dev-assistant` in your terminal to start the CLI. You can use poetry to run the CLI with `poetry run dev-assistant`
- Make your changes
- Test your changes
- Commit your changes
- Push your changes
- Open a pull request
- 🎉

## License

The Dev Assistant Local Client is open-source software, licensed under the [MIT license](LICENSE).

## Support

If you encounter any problems or have any questions, don't hesitate to open an issue on GitHub. We're here to help!

## Acknowledgements

A big thank you to all contributors and users for your support! We couldn't do it without you.

## Authors

- [Luciano T.](https://github.com/lucianotonet)
- [ChatGPT](https://chat.openai.com/)
- [Cursor.so](https://cursor.so/)
