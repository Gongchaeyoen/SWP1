from cgi import parse_qs
import matplotlib.pyplot as plt
from template2 import html

def application(environ, start_response):

        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]

        sum, mul = 0, 0

        try:
                a,b = int(a), int(b)

                sum = a+b
                mul= a*b

        except ValueError:
                sum='Please chech the input value'
                mul='Please chech the input value'

        response_body = html % {

                'sum': sum,
                'mul' : mul
        }

        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])

        return [response_body]

