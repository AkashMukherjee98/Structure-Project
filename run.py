from flask import Flask
from apps import routes
from apps.routes import app
import traceback



if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port="5001")