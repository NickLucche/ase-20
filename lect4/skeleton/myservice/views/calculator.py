from flakon import JsonBlueprint
from flask import request

calculator = JsonBlueprint('calculator', __name__, url_prefix = '/calc')

@calculator.route('/sum/')
def sum():
    print(request.args)
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    print(m, n)
    for _ in range(abs(n)):
        m += (1 if n>0 else -1)
    return {'result': m}

@calculator.route('/div/<int:m>/<int:n>')
def divide(m, n):
    print(m, n)
    m, n = int(m), int(n)
    counter = 0
    if n == 0:
        raise ZeroDivisionError()
    is_negative = m*n < 0
    n, m = abs(n), abs(m)
    while m >= n:
        m -= n
        counter += 1

    return {'result':-counter} if is_negative else {'result': counter} 