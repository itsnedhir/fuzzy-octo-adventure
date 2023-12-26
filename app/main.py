from flask import jsonify

from app.api import create_app

app = create_app()


@app.route("/status")
def index():
    message = "Status OK"
    return jsonify(message=message), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
