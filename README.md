# XGPT-WormGPT

A versatile chatbot application with multiple modes, including the specialized **Worm GPT mode** for security research and ethical hacking discussions.

## Features

- 🤖 **Multiple Chat Modes**:
  - **Standard Mode**: General-purpose helpful assistant
  - **Worm GPT Mode**: Focused on security research, penetration testing, and ethical hacking
  - **Creative Mode**: More imaginative and creative responses

- 📝 **Chat History**: Automatic conversation tracking and export
- ⚙️ **Configurable**: JSON-based configuration system
- 🔒 **Ethical Focus**: Built-in disclaimers for security-related topics

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gaur-avvv/XGPT-WormGPT.git
cd XGPT-WormGPT
```

2. Ensure Python 3.6+ is installed:
```bash
python3 --version
```

3. (Optional) Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Run the chatbot in interactive mode:

```bash
python3 xgpt.py
```

### Available Commands

Once in the chat interface, you can use these commands:

- `/mode <mode>` - Switch between modes (standard, worm, creative)
- `/modes` - List all available modes
- `/history` - View recent chat history
- `/clear` - Clear chat history
- `/save` - Save chat history to a file
- `/quit` - Exit the application

### Examples

#### Starting a Worm GPT Mode Session

```bash
$ python3 xgpt.py
[standard] You: /mode worm
✓ Switched to worm mode: Worm GPT mode - focused on security research and penetration testing

[worm] You: vulnerability assessment
Bot: [Worm GPT Mode] DISCLAIMER: This mode is for educational and ethical security research only...
```

#### Using Standard Mode

```bash
[standard] You: What can you help me with?
Bot: [Standard Mode] Received your input: 'What can you help me with?'

I'm here to help with general questions and tasks. How can I assist you today?
```

## Worm GPT Mode

The Worm GPT mode is specifically designed for:

- 🔍 Penetration Testing guidance
- 🛡️ Security Research discussions
- 🔐 Vulnerability Analysis education
- ⚖️ Ethical Hacking best practices
- 🌐 Network Security concepts
- 🌍 Web Application Security

**Important**: Worm GPT mode includes ethical disclaimers and emphasizes legal, authorized security research only.

## Configuration

Edit `config.json` to customize the chatbot behavior:

```json
{
  "default_mode": "standard",
  "enable_history": true,
  "max_history": 100,
  "worm_mode_settings": {
    "focus_areas": [
      "penetration testing",
      "security research",
      "vulnerability analysis",
      "ethical hacking"
    ],
    "disclaimer": true
  }
}
```

### Configuration Options

- `default_mode`: Starting mode (standard, worm, or creative)
- `enable_history`: Whether to track conversation history
- `max_history`: Maximum number of messages to keep
- `worm_mode_settings.focus_areas`: List of security topics
- `worm_mode_settings.disclaimer`: Show ethical usage disclaimer

## Python API Usage

You can also use XGPT-WormGPT programmatically:

```python
from xgpt import XGPTChat

# Initialize the chatbot
bot = XGPTChat()

# Switch to Worm GPT mode
bot.set_mode('worm')

# Send a message
response = bot.chat("Tell me about penetration testing")
print(response)

# Get chat history
history = bot.get_history()

# Save history
bot.save_history('my_session.json')
```

## Legal and Ethical Notice

⚠️ **IMPORTANT**: This tool is intended for **educational purposes** and **authorized security research** only. Users must:

- Obtain proper authorization before conducting any security testing
- Comply with all applicable laws and regulations
- Use the tool ethically and responsibly
- Respect privacy and confidentiality

Unauthorized access to computer systems is illegal and punishable by law.

## License

This project is provided as-is for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Disclaimer

The developers of XGPT-WormGPT are not responsible for any misuse of this tool. Users are solely responsible for ensuring their use complies with all applicable laws and regulations.