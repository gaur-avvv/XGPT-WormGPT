#!/usr/bin/env python3
"""
Test suite for XGPT-WormGPT
"""

import os
import sys
import json
from xgpt import XGPTChat


def test_initialization():
    """Test chatbot initialization"""
    print("Testing initialization... ", end="")
    bot = XGPTChat()
    assert bot.current_mode == 'standard'
    assert len(bot.history) == 0
    print("✓")


def test_mode_switching():
    """Test mode switching functionality"""
    print("Testing mode switching... ", end="")
    bot = XGPTChat()
    
    # Test valid mode switches
    assert bot.set_mode('worm') == True
    assert bot.get_mode() == 'worm'
    
    assert bot.set_mode('creative') == True
    assert bot.get_mode() == 'creative'
    
    assert bot.set_mode('standard') == True
    assert bot.get_mode() == 'standard'
    
    # Test invalid mode
    assert bot.set_mode('invalid') == False
    assert bot.get_mode() == 'standard'  # Should remain unchanged
    
    print("✓")


def test_worm_mode_responses():
    """Test Worm GPT mode responses"""
    print("Testing Worm GPT mode... ", end="")
    bot = XGPTChat()
    bot.set_mode('worm')
    
    # Security-related query
    response = bot.chat("vulnerability assessment")
    assert "[Worm GPT Mode]" in response
    assert "DISCLAIMER" in response
    
    # Non-security query
    response = bot.chat("weather today")
    assert "[Worm GPT Mode]" in response
    assert "security research topics" in response or "security-related" in response
    
    print("✓")


def test_standard_mode():
    """Test standard mode responses"""
    print("Testing standard mode... ", end="")
    bot = XGPTChat()
    bot.set_mode('standard')
    
    response = bot.chat("Hello")
    assert "[Standard Mode]" in response
    
    print("✓")


def test_creative_mode():
    """Test creative mode responses"""
    print("Testing creative mode... ", end="")
    bot = XGPTChat()
    bot.set_mode('creative')
    
    response = bot.chat("Tell me a story")
    assert "[Creative Mode]" in response
    
    print("✓")


def test_history():
    """Test chat history functionality"""
    print("Testing chat history... ", end="")
    bot = XGPTChat()
    
    # Initially empty
    assert len(bot.get_history()) == 0
    
    # Add some messages
    bot.chat("Message 1")
    bot.chat("Message 2")
    bot.chat("Message 3")
    
    assert len(bot.get_history()) == 3
    
    # Clear history
    bot.clear_history()
    assert len(bot.get_history()) == 0
    
    print("✓")


def test_history_saving():
    """Test saving history to file"""
    print("Testing history saving... ", end="")
    bot = XGPTChat()
    
    bot.chat("Test message")
    
    # Save to temp file
    filename = '/tmp/test_history.json'
    bot.save_history(filename)
    
    # Verify file exists and contains valid JSON
    assert os.path.exists(filename)
    
    with open(filename, 'r') as f:
        data = json.load(f)
        assert 'session_id' in data
        assert 'history' in data
        assert len(data['history']) == 1
    
    # Clean up
    os.remove(filename)
    
    print("✓")


def test_configuration():
    """Test configuration loading"""
    print("Testing configuration... ", end="")
    bot = XGPTChat()
    
    # Check default config values
    assert 'default_mode' in bot.config
    assert 'enable_history' in bot.config
    assert 'worm_mode_settings' in bot.config
    
    print("✓")


def test_empty_input():
    """Test handling of empty input"""
    print("Testing empty input handling... ", end="")
    bot = XGPTChat()
    
    response = bot.chat("")
    assert "valid input" in response
    
    response = bot.chat("   ")
    assert "valid input" in response
    
    print("✓")


def test_mode_descriptions():
    """Test mode descriptions"""
    print("Testing mode descriptions... ", end="")
    bot = XGPTChat()
    
    for mode in ['standard', 'worm', 'creative']:
        bot.set_mode(mode)
        description = bot.get_mode_description()
        assert len(description) > 0
        assert isinstance(description, str)
    
    print("✓")


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Running XGPT-WormGPT Test Suite")
    print("=" * 60)
    print()
    
    tests = [
        test_initialization,
        test_mode_switching,
        test_worm_mode_responses,
        test_standard_mode,
        test_creative_mode,
        test_history,
        test_history_saving,
        test_configuration,
        test_empty_input,
        test_mode_descriptions
    ]
    
    failed = 0
    
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ FAILED")
            print(f"  Error: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ ERROR")
            print(f"  Error: {e}")
            failed += 1
    
    print()
    print("=" * 60)
    if failed == 0:
        print("All tests passed! ✓")
    else:
        print(f"{failed} test(s) failed")
        sys.exit(1)
    print("=" * 60)


if __name__ == '__main__':
    run_all_tests()
