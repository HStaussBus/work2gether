#!/usr/bin/env python3
"""
Simple HTTP server to serve the matrix visualization HTML application.
Serves static files and handles basic HTTP requests for deployment.
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Set the port (default to 5000 for Replit deployment)
PORT = int(os.environ.get('PORT', 5000))

# Set the directory to serve files from (current directory)
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler with proper MIME types and routing."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add CORS headers for better compatibility
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        
        # Security headers to ensure HTTPS and prevent mixed content
        self.send_header('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-XSS-Protection', '1; mode=block')
        self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'unsafe-inline' 'self'; style-src 'unsafe-inline' 'self'; img-src 'self' data:; connect-src 'self'; upgrade-insecure-requests;")
        
        super().end_headers()
    
    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        
        # Handle favicon.ico request
        if self.path == '/favicon.ico':
            self.send_response(204)  # No Content
            self.end_headers()
            return
        
        # Check if file exists
        file_path = DIRECTORY + self.path
        if os.path.isfile(file_path):
            return super().do_GET()
        else:
            # For missing files, serve index.html (SPA behavior)
            if not self.path.startswith('/static') and not '.' in os.path.basename(self.path):
                self.path = '/index.html'
                return super().do_GET()
            # Return 404 for actual missing files
            self.send_error(404, "File not found")
    
    def log_message(self, format, *args):
        # Custom logging format
        print(f"[{self.date_time_string()}] {format % args}")

def start_server():
    """Start the HTTP server."""
    try:
        # Change to the correct directory
        os.chdir(DIRECTORY)
        
        # Create the server with proper error handling for deployment
        httpd = socketserver.TCPServer(("0.0.0.0", PORT), CustomHTTPRequestHandler)
        httpd.allow_reuse_address = True
        
        print(f"Matrix Visualization Server starting...")
        print(f"Serving directory: {DIRECTORY}")
        print(f"Server running at http://0.0.0.0:{PORT}/")
        print(f"Access your application at the provided URL")
        print("Press Ctrl+C to stop the server")
        
        # Start serving
        httpd.serve_forever()
        
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"Error starting server: {e}")
            print("Attempting to find and stop conflicting process...")
            # Try a different port as fallback
            try_alternate_port()
        else:
            print(f"Server error: {e}")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def try_alternate_port():
    """Try starting server on alternate ports."""
    alternate_ports = [5001, 5002, 5003, 8000, 8080]
    global PORT
    
    for port in alternate_ports:
        try:
            PORT = port
            httpd = socketserver.TCPServer(("0.0.0.0", PORT), CustomHTTPRequestHandler)
            httpd.allow_reuse_address = True
            print(f"Started server on alternate port {PORT}")
            httpd.serve_forever()
            break
        except OSError:
            continue
        except KeyboardInterrupt:
            print("\nServer stopped by user")
            sys.exit(0)
    else:
        print("Could not start server on any available port")
        sys.exit(1)

if __name__ == "__main__":
    start_server()