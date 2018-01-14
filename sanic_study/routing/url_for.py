from sanic import Sanic
from sanic.response import text, redirect

"""
url_for generates URLs based on the handler method name.
"""

app = Sanic()


@app.route('/')
async def index(request):
    """
    Redirects the client who enters
    /
    to
    /posts/5
    :param request:
    :return:
    """
    # Generates a URL for the endpoint "post_handler"
    # url = /posts/5
    url = app.url_for('post_handler', post_id=5)
    return redirect(url)

@app.route('/params')
async def index_with_params(request):
    """
    Redirects the client who enters
    /params
    to
    /posts/5?arg_one=one&arg_two=two
    :param request:
    :return:
    """
    url = app.url_for('post_handler', post_id=5, arg_one='one', arg_two='two')
    return redirect(url)

@app.route('/posts/<post_id>')
async def post_handler(reuqest, post_id):
    return text(f'Post - {post_id}')


# Can include special arguments
# _anchor, _external, _scheme, _method, _server

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
