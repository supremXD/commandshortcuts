import os
import socket
import http.server
import socketserver
import threading


def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_local = s.getsockname()[0]
    s.close()
    print(f"Your local IP is: {ip_local}, access by: \033[92mhttp://{ip_local}:8080\033[0m")


class AutoCloseHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path_local = self.translate_path(self.path)
        if os.path.isfile(path_local):
            try:
                print(f"\033[94mServing file: {self.path}\033[0m")
                super().do_GET()
                print(f"\033[91mDownload completed: {self.path}. Closing server...\033[0m")
                threading.Thread(target=self.server.shutdown, daemon=True).start()
            except Exception as e:
                print(f"\033[91mError sending file {self.path}: {e}\033[0m")
        else:
            super().do_GET()


def server():
    print("")
    ip()
    print("")
    print("\033[93mStarting server. Press Ctrl+C to stop manually.\033[0m\n")

    PORT = 8080
    Handler = AutoCloseHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            print(f"\033[97mServing on port {PORT}...\033[0m\n")
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\033[91mServer stopped manually.\033[0m")
        finally:
            httpd.server_close()

    print("\033[92mServer closed automatically after a completed file download.\033[0m")
    exit()


if __name__ == "__main__":
    server()