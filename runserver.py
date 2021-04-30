"""
This script runs the Projet_portail_automatique application using a development server.
"""

from os import environ
from Projet_portail_automatique import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
