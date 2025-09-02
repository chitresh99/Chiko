# Chiko

A lightweight AI-powered Python coding assistant.
Chiko takes a prompt and generates **raw Python code** using OpenRouter models, writing it directly to a file (`output.py`).

## Features

* Generates runnable Python code based on your prompt.
* Ensures output is **Python only** and **without markdown or extra explanations**.
* Simple and minimal setup using `.env` for API keys.
* Can be easily modified for different OpenRouter models.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/chitresh99/Chiko.git
cd Chiko
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_api_key_here
```

4. Modify `prompt` in `main.py` with your desired code request.

## Usage

```bash
python main.py
```

* The generated code will be saved to `output.py`.
* Once completed, you’ll see `Succesfull` printed in the terminal.

## Disclaimer

**Use with caution:**

* Chiko generates **raw Python code** based on AI suggestions.
* You are fully responsible for reviewing and running the generated code.
* The developer is **not responsible** for any errors, security risks, or unintended behavior resulting from running the code.
* Always inspect the code before executing it on your system.