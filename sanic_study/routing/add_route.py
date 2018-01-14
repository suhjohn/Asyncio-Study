from sanic import Sanic
from sanic.response import text

app = Sanic()


async def handler1(request):
    return text("OK")


async def handler2(request, name):
    return text(f'Folder - {name}')


async def person_handler(request, name):
    return text(f"Person - {name}")


app.add_route(handler1, '/test')
app.add_route(handler2, '/folder/<name>')
app.add_route(person_handler, '/person/<name:[a-zA-Z]+>', methods=['GET'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
