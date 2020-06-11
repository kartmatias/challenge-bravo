from app import app


@app.route('/')
def index():
    return "Bravo Currency Conversion API - v 1.0"
