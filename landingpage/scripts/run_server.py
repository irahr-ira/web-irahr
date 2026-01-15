import http.server
import socketserver
import os
import sys

# Configuration
PORT = 8000
DIRECTORY = "."

def run_server():
    # Change to root directory if we are in scripts/
    if os.path.basename(os.getcwd()) == 'scripts':
        os.chdir('..')

    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving at http://localhost:{PORT}")
            print("Press Ctrl+C to stop.")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error: {e}")
        print(f"Port {PORT} might be in use.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nStopping server.")
        sys.exit(0)

if __name__ == "__main__":
    run_server()
