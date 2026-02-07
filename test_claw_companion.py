#!/usr/bin/env python3
"""
Tests for claw-companion

Run: python3 -m pytest test_claw_companion.py -v
"""

import unittest
from claw_companion import hello


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


if __name__ == "__main__":
    unittest.main()
