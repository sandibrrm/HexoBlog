# test_hexoblog.py
"""
Tests for HexoBlog module.
"""

import unittest
from hexoblog import HexoBlog

class TestHexoBlog(unittest.TestCase):
    """Test cases for HexoBlog class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HexoBlog()
        self.assertIsInstance(instance, HexoBlog)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HexoBlog()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
