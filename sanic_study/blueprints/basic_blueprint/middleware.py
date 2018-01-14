from my_blueprint import bp
from sanic.response import text


@bp.middleware
async def print_on_request(request):
    print("I am a spy")


@bp.middleware('request')
async def halt_request(request):
    return text('I halted the request')


@bp.middleware('response')
async def halt_response(request, response):
    return text('I halted the response')
