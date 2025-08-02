#!/usr/bin/env python3
"""
Simple run script for Replit deployment.
Ensures the web server starts properly for deployment.
"""

import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and start the server
from server import start_server

if __name__ == "__main__":
    print("Starting Matrix Visualization Application...")
    start_server()