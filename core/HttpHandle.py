from http.server import SimpleHTTPRequestHandler


class HttpHandle(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = './templates/form.html'
        file = self.read_html_template(self.path)
        self.send_response(200, "OK")
        self.end_headers()
        self.wfile.write(bytes(file, "utf-8"))

    def read_html_template(self, path):
        try:
            with open(path) as f:
                file = f.read()
        except Exception as e:
            file = e
        return file
