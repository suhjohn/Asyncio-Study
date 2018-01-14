from sanic import Sanic
from my_blueprint import bp

app = Sanic()
app.blueprint(bp)

app.run(host='0.0.0.0', port=8000, debug=True)
