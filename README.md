# AI Agent

A toy implementation of an AI coding agent that demonstrates how LLM function calling works. This project uses Google's Gemini API to create an agent that can interact with a local filesystem and execute Python code.

## ⚠️ SECURITY WARNING

**This is a toy project for educational purposes only. DO NOT use this in production or give it access to sensitive files/directories.**

This agent has the ability to:
- Read any file in the working directory
- Write/overwrite files
- Execute Python code

Even professional tools like Cursor, Zed's Agentic Mode, or Claude Code aren't perfectly secure. This toy implementation has minimal security controls and should be treated as a learning exercise only.

**Use at your own risk and only in isolated, non-critical environments.**

## Features

The agent can perform the following operations within a sandboxed working directory:

- **List files and directories** - Browse the filesystem structure
- **Read file contents** - View the contents of any file
- **Execute Python files** - Run Python scripts with optional arguments
- **Write files** - Create new files or overwrite existing ones

## Prerequisites

- Python 3.14 or higher
- **Your own Google Gemini API key** (free tier available)
- [uv](https://docs.astral.sh/uv/) package manager (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-agent
```

2. Install dependencies:
```bash
uv sync
```

3. **Get your own API key** from [Google AI Studio](https://aistudio.google.com/app/apikey) (you'll need to sign in with a Google account)

4. Create a `.env` file in the project root with your API key:
```bash
GEMINI_API_KEY=your_api_key_here
```

**Important:** Replace `your_api_key_here` with your actual API key. This project does not include an API key - you must provide your own.

## Usage

Run the agent with a prompt:

```bash
python main.py "your prompt here"
```

Enable verbose output to see token usage and function call details:

```bash
python main.py "your prompt here" --verbose
```

### Example Commands

```bash
# List files in the working directory
python main.py "What files are in the calculator directory?"

# Read and explain code
python main.py "Read the main.py file in calculator and explain what it does"

# Execute a Python file
python main.py "Run the tests.py file in calculator"

# Create or modify files
python main.py "Create a new file called hello.py that prints 'Hello, World!'"
```

## Architecture

### Main Components

- **main.py** - Entry point that handles CLI arguments and coordinates the agent
- **prompts.py** - System prompt that defines the agent's behavior
- **functions/** - Directory containing function implementations:
  - `call_function.py` - Function dispatcher and registry
  - `get_file_content.py` - Read file contents
  - `get_files_info.py` - List directory contents
  - `run_python_file.py` - Execute Python scripts
  - `write_file.py` - Create/overwrite files

### Working Directory

The agent operates within the `./calculator` directory by default. This is hardcoded in `functions/call_function.py` as a basic security measure to prevent access to the entire filesystem.

To change the working directory, modify this line in `call_function.py`:
```python
args["working_directory"] = "./calculator"
```

## How It Works

1. User provides a prompt via command line
2. The prompt is sent to Gemini with available function definitions
3. Gemini decides which functions to call based on the prompt
4. The agent executes the requested functions
5. Results are returned to the user (and optionally shown in verbose mode)

## Limitations

- Only works with Python files for code execution
- Working directory must be manually configured
- No persistent conversation history
- Minimal error handling
- No sandboxing beyond working directory restriction
- Single-turn interaction (no multi-turn conversations)

## Educational Purpose

This project demonstrates:
- How to use Google Gemini's function calling API
- Basic LLM agent architecture
- File system operations via LLM
- Command-line interface for AI agents

## License

This is an educational project. Use responsibly.

## Contributing

This is a toy project for learning purposes. Feel free to fork and experiment, but remember the security implications of any agentic system.