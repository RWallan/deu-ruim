# Deu Ruim ![LICENCE](https://img.shields.io/github/license/RWallan/deu-ruim)

<p align="center">
    <img src="https://github.com/user-attachments/assets/cf40c5b8-33f2-4a69-b0f8-5f7a90efb715" width="500">
</p>


<p align="center">
    <a href="#basic-usage">Basic Usage</a> •
    <a href="#configuration">Configuration</a> •
    <a href="#contributing">Contributing</a> •
    <a href="#alternatives">Alternatives</a> •
    <a href="#license">License</a>
</p>

`Deu Ruim` is a command line interface (CLI) made to help beginners to fix your console commands using LLM.

*This project is inspired by [The Fuck](https://github.com/nvbn/thefuck).*

## Configuration

You'll need to have [Ollama](https://ollama.com/) preinstalled on your machine to run the CLI and the [qwen2.5-coder](https://ollama.com/library/qwen2.5-coder) model installed.

### A fast course about Ollama

To install ollama, run:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

> [!NOTE]
> If you use Windows or Mac, please, access the [Ollama download page directly](https://ollama.com/download).

After that, you'll need to pull the `qwen2.5-coder` model:

```bash
ollama run qwen2.5-coder
```

After that, you'll need to configure some environment variables in your terminal:

```
OLLAMA_API_KEY=<YOUR_API_KEY>
OLLAMA_API_URL=<YOUR_API_BASE_URL>
```

> [!TIP]
> To generate your public API key, use `ollama serve`

## Basic usage

Simply run:

```bash
deu-ruim <command>
```

And wait the magic happens.

### Examples

```bash
deu-ruim sl

Run ls [Y/n]: 
```

```bash
deu-ruim "git brnch"

Run git branch [Y/n]:
```

> [!WARNING]
> The performance and speed depends on from which model you're using.

## Roadmap

I'm working to transform the project model agnostic and bring some life saviors, for example, having to put quotation marks on commands with spaces.

You can follow the changelog in `changelog.d` directory. I'll create a documentation with changelogs too, to make it easier to follow 😊.

See Contributing session if you want to help the project advance faster.

## Contributing

Thank you for your interest in contributing to the `Deu Ruim` project!

### Reporting bugs

If you discover a bug, first check the [GitHub issues](https://github.com/RWallan/deu-ruim/issues) page to see if issues have already been reported.

Please use the "Bug Report" template and provide detailed information about the problem, including steps to reproduce it.
Suggesting Features

If you want to suggest a new feature or improvement, first check the [GitHub issues](https://github.com/RWallan/deu-ruim/issues) page to ensure a similar suggestion hasn't already been made.

### Contributing Code

Before submitting code changes, check if there are similar [pull requests](https://github.com/RWallan/deu-ruim/pulls) already open. This will prevent duplicate efforts. Please follow these guidelines:

**Requirements for Merging a Pull Request**

The requirements to accept a pull request are as follows:

* Adhere to project coding standards, formatting, and linting rules. Make sure you check the guidelines for each component.
* Write comprehensive tests and ensure all tests pass.
* Maintain or improve test coverage.
* Generate changelog with [towncrier](https://github.com/twisted/towncrier).

## Alternatives

Some powerful alternatives with unique features:

- [The Fuck](https://github.com/nvbn/thefuck), a powerful tool that corrects errors in previous console commands.

- [Warp](https://www.warp.dev/), a terminal combined with AI.

## License

This project is licensed under the MIT license.
