#!/usr/bin/env python3
"""
Flask-based web server for better Replit deployment compatibility.
"""

from flask import Flask, send_from_directory, send_file
import os

app = Flask(__name__)

# Get port from environment variable
PORT = int(os.environ.get('PORT', 5000))

@app.route('/')
def index():
    """Serve the main HTML file."""
    return send_file('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files."""
    try:
        return send_from_directory('.', filename)
    except:
        # Fallback for SPA routing
        return send_file('index.html')

@app.route('/Dataset.csv')
def serve_csv():
    """Serve the CSV data file."""
    return send_file('Dataset.csv', mimetype='text/csv')

if __name__ == '__main__':
    print(f"Starting Flask server on port {PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=False)