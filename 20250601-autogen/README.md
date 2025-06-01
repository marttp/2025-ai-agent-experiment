# AutoGen Chat Application

A simple chat application built with AutoGen, enabling AI-powered conversations.

## Prerequisites

- Python 3.12+
- UV package manager (https://github.com/astral-sh/uv)
- [Optional] OpenAI API key (Because I used Ollama)

## Installation

1. Clone this repository
2. Install the required packages:

```bash
uv add "autogen-agentchat"
uv add "autogen-ext[openai]"
```

## Configuration

Add your OpenAI API key and other environment variables to the `.env` file based on your experiment.

## Usage

Start the chat application with:

Note: Update the path depending on your goal

Example

```bash
UV_ENV_FILE=.env uv run ./agent/chat_agent.py
```

## Features

- AI-powered chat interface
- Easy setup with UV package manager
- Environment-based configuration