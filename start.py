import os
from http.server import CGIHTTPRequestHandler, HTTPServer
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin', '/htbin']  # this is the default
server = HTTPServer(('0.0.0.0', 8123), handler)
server.serve_forever()
