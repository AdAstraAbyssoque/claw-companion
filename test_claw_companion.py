#!/usr/bin/env python3
"""
Tests for claw-companion

Run: python3 -m pytest test_claw_companion.py -v
"""

import unittest
from claw_companion import hello, version, who_am_i, greeting, random_wisdom


class TestClawCompanion(unittest.TestCase):
    """Test cases for Claw Companion."""
    
    def test_hello_returns_string(self):
        """Test that hello() returns a string."""
        result = hello()
        self.assertIsInstance(result, str)
    
    def test_hello_contains_claw(self):
        """Test that hello() contains 'Claw'."""
        result = hello()
        self.assertIn("Claw", result)
    
    def test_version_returns_string(self):
        """Test that version() returns a string."""
        result = version()
        self.assertIsInstance(result, str)
    
    def test_version_contains_v(self):
        """Test that version() contains 'v'."""
        result = version()
        self.assertIn("v", result)
    
    def test_who_am_i_returns_string(self):
        """Test that who_am_i() returns a string."""
        result = who_am_i()
        self.assertIsInstance(result, str)
    
    def test_who_am_i_contains_claw(self):
        """Test that who_am_i() contains 'Claw'."""
        result = who_am_i()
        self.assertIn("Claw", result)
    
    def test_greeting_returns_string(self):
        """Test that greeting() returns a string."""
        result = greeting()
        self.assertIsInstance(result, str)
    
    def test_greeting_with_name(self):
        """Test greeting with custom name."""
        result = greeting("Astra")
        self.assertIn("Astra", result)
    
    def test_random_wisdom_returns_string(self):
        """Test that random_wisdom() returns a string."""
        result = random_wisdom()
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()
