# -*- coding: utf-8 -*-

"""
    Zen, a simple web framework.
"""


class Zen:
    def __call__(self, environ, start_response):
        response_body = b'Hello, World'
        status = '200 OK'
        headers = [('HELLO', 'WORLD')]
        start_response(status, headers)
        return [response_body]


app = Zen()
