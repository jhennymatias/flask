from app import app


@app.route("/index")
@app.route("/")
def index():
    return "Hello Word"

@app.route("/test/<name>")

def test(name):
    return "Olá, %s!" % name