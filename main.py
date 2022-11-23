# import http.server
# import socketserver
#
# PORT = 8080
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

from http.server import HTTPServer, CGIHTTPRequestHandler
port = 8000
server_data = ('localhost', port)

server = HTTPServer(server_data, CGIHTTPRequestHandler)
print("serving at port", port)
server.serve_forever()
