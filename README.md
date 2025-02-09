<h1 align="center">ChatGpt Telegram Bot 🌌</h1>

<p align="center">
  <em>ChatGptBot: An AI-powered Telegram bot script for generating text-based responses using OpenAI</em>
</p>

<p align="center">
  <a href="https://github.com/abirxdhack/ChatGptBot/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/abirxdhack/ChatGptBot?style=social"></a>
  <a href="https://github.com/abirxdhack/ChatGptBot/network/members"><img alt="GitHub forks" src="https://img.shields.io/github/forks/abirxdhack/ChatGptBot?style=social"></a>
  <a href="https://github.com/abirxdhack/ChatGptBot/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/abirxdhack/ChatGptBot"></a>
  <a href="https://github.com/abirxdhack/ChatGptBot/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/abirxdhack/ChatGptBot"></a>
  <a href="https://github.com/abirxdhack/ChatGptBot/pulls"><img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/abirxdhack/ChatGptBot"></a>
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pyrogram">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/abirxdhack/ChatGptBot">
</p>

<hr>

## 🌟 Features

- 🍪 **Text Prompt Response**: Accepts text prompts and generates text.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.9 or higher.
- `pyrogram`, `openai` libraries.
- A Telegram bot token (you can get one from [@BotFather](https://t.me/BotFather) on Telegram).
- API ID and Hash: You can get these by creating an application on [my.telegram.org](https://my.telegram.org).
- To Get `GPT_API_KEY` Open [GPT_API_KEY](https://platform.openai.com/settings/organization/api-keys).

## Installation

To install `pyrogram`, `openai` run the following command:

```bash
pip install pyrogram openai
```

**Note: If you previously installed `pyrofork`, uninstall it before installing `pyrogram`.**

## Configuration

1. Open the `config.py` file in your favorite text editor.
2. Replace the placeholders for `API_ID`, `API_HASH`, `GPT_API_KEY`, and `BOT_TOKEN` with your actual values:
   - **`API_ID`**: Your API ID from [my.telegram.org](https://my.telegram.org).
   - **`API_HASH`**: Your API Hash from [my.telegram.org](https://my.telegram.org).
   - **`GPT_API_KEY`**: To get Google API key [Click Here](https://platform.openai.com/settings/organization/api-keys).
   - **`BOT_TOKEN`**: The token you obtained from [@BotFather](https://t.me/BotFather).

## Deploy the Bot

```sh
git clone https://github.com/abirxdhack/ChatGptBot
cd ChatGptBot
python main.py
```

## Usage 🛠️

The bot supports the following commands:

- `/gpt <prompt>`: Generates a response based on a provided text prompt.
- `.gpt <prompt>`: Generates a response based on a provided text prompt.
- `/gpt4 <prompt>`: Generates a response based on a provided text prompt.
- `.gpt4 <prompt>`: Generates a response based on a provided text prompt.

## Author 📝

- Name: Abir Arafat Chawdhury
- Telegram: [@abirxdhackz](https://t.me/abirxdhackz)

