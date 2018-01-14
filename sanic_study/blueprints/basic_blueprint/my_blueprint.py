from sanic.response import json, text
from sanic import Blueprint

bp = Blueprint('my_blueprint')

@bp.route('/')
async def bp_root(request):
    return json({'my': 'blueprint'})

@bp.route('/post')
async def post(request):
    return json({'post':'index'})

@bp.middleware
async def print_on_request(request):
    print("I am a spy")


@bp.middleware('request')
async def halt_request(request):
    return text('I halted the request')


@bp.middleware('response')
async def halt_response(request, response):
    return text('I halted the response')
