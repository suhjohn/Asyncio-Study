from sanic import Sanic
from sanic.response import text

app = Sanic()

#
# # Can denote HTTP method with the methods argument
# @app.route('/post', methods=['POST'])
# async def post_handler(request):
#     return text(f"POST request - {request.json}")
#
# @app.route('/get', methods=['GET'])
# async def get_handler(request):
#     return text(f'GET request - {request.args}')
#
#
# #------

# Optional host argument.
@app.route('/get-host', methods=['GET'], host='0.0.0.0:8000')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))

# if the host header doesn't match example.com, this route will be used
@app.route('/get-host', methods=['GET'])
async def get_handler(request):
    return text('GET request in default - {}'.format(request.args))

# Method decorators instead of route

@app.post('/post')
async def post_handler(request):
    return text(f"POST request - {request.json}")

@app.get('/get')
async def get_handler(request):
    return text(f'GET request - {request.args}')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
