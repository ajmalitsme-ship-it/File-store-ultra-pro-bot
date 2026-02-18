from flask import Flask
from web.routes import web
from config import PORT

app = Flask(__name__)
app.register_blueprint(web)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
