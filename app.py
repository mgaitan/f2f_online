import bottle
import subprocess
from bottle import route, request, run, redirect


#2. Define needed routes here
@route('/')
def index():
    return "it works!"


@route('/api')
def f2f():

    if (request.method == 'POST' and
            request.headers.get('X-Requested-With') == 'XMLHttpRequest'):



        return 'This is an AJAX request'
    else:
        redirect('/')


# wsgi hook
def application(environ, start_response):
    return bottle.default_app().wsgi(environ, start_response)



#4. Main method for local developement
if __name__ == "__main__":
    bottle.debug(True)
    run(reloader=True)
