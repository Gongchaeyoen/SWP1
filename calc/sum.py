from cgi import parse_qs
from template2 import html

def application(environ, start_response):

        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]
	
	sum, mul = 0,0
	
	if '' in [a,b]:
		sum = "No input value found"
		mul = "No input value found"	
	else:
		try:	
		
			a,b = int(a), int(b)
			sum = a+b
			mul = a*b
		
		except ValueError:
			sum = "Please enter only numbers"	
			mul = "Please enter only numbers"
			
        response_body = html % {

                'sum': sum,
                'mul': mul 
        }

        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])

        return [response_body]

