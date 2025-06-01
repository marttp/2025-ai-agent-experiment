# AutoGen Chat Application

A simple chat application built with AutoGen, enabling AI-powered conversations.

## Prerequisites

- Python 3.8+
- UV package manager (https://github.com/astral-sh/uv)
- OpenAI API key

## Installation

1. Clone this repository
2. Install the required packages:

```bash
uv add "autogen-agentchat"
uv add "autogen-ext[openai]"
```

## Configuration

1. Create a `.env` file in the project root
2. Add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Start the chat application with:

```bash
UV_ENV_FILE=.env uv run ./chat/chat.py
```

## Features

- AI-powered chat interface
- Easy setup with UV package manager
- Environment-based configuration