# test_polygonsdk.py
"""
Tests for PolygonSDK module.
"""

import unittest
from polygonsdk import PolygonSDK

class TestPolygonSDK(unittest.TestCase):
    """Test cases for PolygonSDK class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PolygonSDK()
        self.assertIsInstance(instance, PolygonSDK)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PolygonSDK()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
