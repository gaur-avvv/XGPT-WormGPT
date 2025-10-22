#!/usr/bin/env python3
"""
Demo script showcasing XGPT-WormGPT functionality
"""

from xgpt import XGPTChat


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60 + "\n")


def demo_basic_usage():
    """Demonstrate basic chatbot usage"""
    print_section("Demo 1: Basic Usage")
    
    bot = XGPTChat()
    print(f"Initialized chatbot in '{bot.get_mode()}' mode")
    print(f"Description: {bot.get_mode_description()}\n")
    
    response = bot.chat("Hello, how can you help me?")
    print(f"User: Hello, how can you help me?")
    print(f"Bot: {response[:200]}...\n")


def demo_worm_mode():
    """Demonstrate Worm GPT mode"""
    print_section("Demo 2: Worm GPT Mode")
    
    bot = XGPTChat()
    bot.set_mode('worm')
    print(f"Switched to '{bot.get_mode()}' mode")
    print(f"Description: {bot.get_mode_description()}\n")
    
    # Security-related query
    query = "vulnerability assessment methodology"
    response = bot.chat(query)
    print(f"User: {query}")
    print(f"Bot: {response[:300]}...\n")


def demo_mode_switching():
    """Demonstrate switching between modes"""
    print_section("Demo 3: Mode Switching")
    
    bot = XGPTChat()
    
    modes = ['standard', 'worm', 'creative']
    
    for mode in modes:
        success = bot.set_mode(mode)
        if success:
            print(f"✓ Switched to '{mode}' mode")
            print(f"  Description: {bot.get_mode_description()}")
        else:
            print(f"✗ Failed to switch to '{mode}' mode")
    
    print()


def demo_history():
    """Demonstrate chat history functionality"""
    print_section("Demo 4: Chat History")
    
    bot = XGPTChat()
    
    # Generate some chat history
    queries = [
        "Hello",
        "What is security testing?",
        "Explain penetration testing"
    ]
    
    for query in queries:
        bot.chat(query)
        print(f"Added to history: {query}")
    
    print(f"\nTotal messages in history: {len(bot.get_history())}")
    
    # Save history
    filename = bot.save_history('/tmp/demo_history.json')
    print(f"History saved to: {filename}\n")


def demo_worm_mode_features():
    """Demonstrate Worm GPT mode specific features"""
    print_section("Demo 5: Worm GPT Mode Features")
    
    bot = XGPTChat()
    bot.set_mode('worm')
    
    test_queries = [
        "penetration testing tools",
        "weather today",  # Non-security query
        "vulnerability scanning techniques"
    ]
    
    for query in test_queries:
        print(f"User: {query}")
        response = bot.chat(query)
        # Print first 150 chars
        print(f"Bot: {response[:150]}...")
        print()


def demo_configuration():
    """Demonstrate configuration options"""
    print_section("Demo 6: Configuration")
    
    bot = XGPTChat()
    
    print("Current configuration:")
    print(f"  Default mode: {bot.config.get('default_mode')}")
    print(f"  History enabled: {bot.config.get('enable_history')}")
    print(f"  Max history: {bot.config.get('max_history')}")
    
    worm_settings = bot.config.get('worm_mode_settings', {})
    print(f"  Worm mode disclaimer: {worm_settings.get('disclaimer')}")
    print(f"  Focus areas: {len(worm_settings.get('focus_areas', []))}")
    print()


def main():
    """Run all demos"""
    print("=" * 60)
    print(" XGPT-WormGPT Demo Script")
    print("=" * 60)
    print()
    print("This script demonstrates the key features of XGPT-WormGPT")
    print()
    
    try:
        demo_basic_usage()
        demo_worm_mode()
        demo_mode_switching()
        demo_history()
        demo_worm_mode_features()
        demo_configuration()
        
        print_section("Demo Complete")
        print("All demos completed successfully!")
        print("Try running 'python3 xgpt.py' for interactive mode.\n")
        
    except Exception as e:
        print(f"\nError during demo: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
