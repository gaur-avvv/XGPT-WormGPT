#!/usr/bin/env python3
"""
XGPT-WormGPT: A chatbot with multiple modes including Worm GPT mode
"""

import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional


class XGPTChat:
    """Main chatbot class with multiple modes"""
    
    MODES = {
        'standard': 'Standard GPT mode - helpful and informative',
        'worm': 'Worm GPT mode - focused on security research and penetration testing',
        'creative': 'Creative mode - more imaginative and creative responses'
    }
    
    def __init__(self, config_path: str = 'config.json'):
        """Initialize the chatbot"""
        self.config = self._load_config(config_path)
        self.current_mode = self.config.get('default_mode', 'standard')
        self.history: List[Dict[str, str]] = []
        self.session_id = datetime.now().strftime('%Y%m%d_%H%M%S')
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from file"""
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Invalid JSON in {config_path}, using defaults")
        return self._get_default_config()
    
    def _get_default_config(self) -> Dict:
        """Get default configuration"""
        return {
            'default_mode': 'standard',
            'enable_history': True,
            'max_history': 100,
            'worm_mode_settings': {
                'focus_areas': [
                    'penetration testing',
                    'security research',
                    'vulnerability analysis',
                    'ethical hacking'
                ],
                'disclaimer': True
            }
        }
    
    def set_mode(self, mode: str) -> bool:
        """Change the current mode"""
        if mode in self.MODES:
            self.current_mode = mode
            return True
        return False
    
    def get_mode(self) -> str:
        """Get the current mode"""
        return self.current_mode
    
    def get_mode_description(self) -> str:
        """Get description of current mode"""
        return self.MODES.get(self.current_mode, 'Unknown mode')
    
    def _get_worm_mode_response(self, user_input: str) -> str:
        """Generate response in Worm GPT mode"""
        response_prefix = "[Worm GPT Mode] "
        
        # Show disclaimer on first use
        if self.config.get('worm_mode_settings', {}).get('disclaimer', True):
            disclaimer = (
                "DISCLAIMER: This mode is for educational and ethical security research only. "
                "Unauthorized access to computer systems is illegal.\n\n"
            )
        else:
            disclaimer = ""
        
        # Analyze input for security-related keywords
        security_keywords = [
            'vulnerability', 'exploit', 'penetration', 'security', 'hack',
            'assessment', 'audit', 'test', 'scan', 'reconnaissance'
        ]
        
        input_lower = user_input.lower()
        is_security_related = any(keyword in input_lower for keyword in security_keywords)
        
        if is_security_related:
            response = (
                f"{disclaimer}{response_prefix}I can assist with security research and "
                f"ethical penetration testing. Here's how I can help:\n\n"
                f"1. Vulnerability Assessment Guidance\n"
                f"2. Security Testing Methodologies\n"
                f"3. Common Attack Vectors and Defenses\n"
                f"4. Best Practices for Ethical Hacking\n\n"
                f"Your query: '{user_input}'\n\n"
                f"For specific security research tasks, ensure you have proper authorization "
                f"and are operating within legal and ethical boundaries."
            )
        else:
            response = (
                f"{response_prefix}Worm GPT mode is optimized for security research topics. "
                f"Your query doesn't appear to be security-related. Consider:\n"
                f"- Switching to 'standard' mode for general queries\n"
                f"- Rephrasing your question to focus on security aspects\n\n"
                f"Focus areas for Worm GPT mode:\n"
            )
            for area in self.config.get('worm_mode_settings', {}).get('focus_areas', []):
                response += f"- {area}\n"
        
        return response
    
    def _get_standard_response(self, user_input: str) -> str:
        """Generate response in standard mode"""
        response = (
            f"[Standard Mode] Received your input: '{user_input}'\n\n"
            f"I'm here to help with general questions and tasks. "
            f"How can I assist you today?"
        )
        return response
    
    def _get_creative_response(self, user_input: str) -> str:
        """Generate response in creative mode"""
        response = (
            f"[Creative Mode] Interesting! Let me think creatively about: '{user_input}'\n\n"
            f"In creative mode, I explore ideas from unique angles and perspectives. "
            f"What aspect would you like to explore?"
        )
        return response
    
    def chat(self, user_input: str) -> str:
        """Process user input and generate response"""
        if not user_input.strip():
            return "Please provide a valid input."
        
        # Generate response based on current mode
        if self.current_mode == 'worm':
            response = self._get_worm_mode_response(user_input)
        elif self.current_mode == 'creative':
            response = self._get_creative_response(user_input)
        else:
            response = self._get_standard_response(user_input)
        
        # Store in history if enabled
        if self.config.get('enable_history', True):
            self.history.append({
                'timestamp': datetime.now().isoformat(),
                'mode': self.current_mode,
                'input': user_input,
                'response': response
            })
            
            # Trim history if needed
            max_history = self.config.get('max_history', 100)
            if len(self.history) > max_history:
                self.history = self.history[-max_history:]
        
        return response
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get chat history"""
        return self.history
    
    def clear_history(self):
        """Clear chat history"""
        self.history = []
    
    def save_history(self, filename: Optional[str] = None):
        """Save chat history to file"""
        if not filename:
            filename = f"chat_history_{self.session_id}.json"
        
        with open(filename, 'w') as f:
            json.dump({
                'session_id': self.session_id,
                'mode': self.current_mode,
                'history': self.history
            }, f, indent=2)
        
        return filename


def main():
    """Main entry point for interactive mode"""
    print("=" * 60)
    print("XGPT-WormGPT Chat Interface")
    print("=" * 60)
    print()
    
    # Initialize chatbot
    bot = XGPTChat()
    
    print(f"Current mode: {bot.get_mode()} - {bot.get_mode_description()}")
    print()
    print("Available commands:")
    print("  /mode <mode>  - Change mode (standard, worm, creative)")
    print("  /modes        - List available modes")
    print("  /history      - Show chat history")
    print("  /clear        - Clear chat history")
    print("  /save         - Save chat history")
    print("  /quit         - Exit the chat")
    print("=" * 60)
    print()
    
    while True:
        try:
            user_input = input(f"[{bot.get_mode()}] You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.startswith('/'):
                command_parts = user_input[1:].split(maxsplit=1)
                command = command_parts[0].lower()
                args = command_parts[1] if len(command_parts) > 1 else None
                
                if command == 'quit':
                    print("Goodbye!")
                    break
                elif command == 'mode':
                    if args and bot.set_mode(args.lower()):
                        print(f"✓ Switched to {args} mode: {bot.get_mode_description()}")
                    else:
                        print(f"✗ Invalid mode. Available modes: {', '.join(bot.MODES.keys())}")
                elif command == 'modes':
                    print("Available modes:")
                    for mode, description in bot.MODES.items():
                        marker = "→" if mode == bot.get_mode() else " "
                        print(f"  {marker} {mode}: {description}")
                elif command == 'history':
                    history = bot.get_history()
                    if history:
                        print(f"\nChat History ({len(history)} messages):")
                        for i, entry in enumerate(history[-10:], 1):  # Show last 10
                            print(f"\n{i}. [{entry['mode']}] {entry['timestamp']}")
                            print(f"   You: {entry['input'][:50]}...")
                    else:
                        print("No chat history.")
                elif command == 'clear':
                    bot.clear_history()
                    print("✓ Chat history cleared.")
                elif command == 'save':
                    filename = bot.save_history()
                    print(f"✓ Chat history saved to {filename}")
                else:
                    print(f"✗ Unknown command: {command}")
                
                continue
            
            # Process regular chat input
            response = bot.chat(user_input)
            print(f"\nBot: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nInterrupted. Use /quit to exit properly.")
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
