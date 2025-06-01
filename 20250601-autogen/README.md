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
uv add "autogen-ext[openai,redis,docker]"
```

or if you familiar with `uv` already

```bash
uv sync
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

## Docker executor

If you use docker desktop, you can use docker executor without setting DOCKER_HOST environment variable.

Otherwise, you need to set DOCKER_HOST environment variable.

Example for Colima

```bash
export DOCKER_HOST=unix:///Users/xxxxxxxxxxx/.colima/default/docker.sock
UV_ENV_FILE=.env uv run ./agent/agent.py
```

## Features

- AI-powered chat interface
- Easy setup with UV package manager
- Environment-based configuration

# My used resources

- https://youtu.be/VukcfLpuDJY?si=Tm7pYZb9H5J2sM6h
- https://www.dataleadsfuture.com/build-autogen-agents-with-qwen3-structured-output-thinking-mode/