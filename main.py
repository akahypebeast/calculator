"""CLI entry point and Flask web server for the calculator."""

import argparse

from flask import Flask, render_template_string, request, jsonify

from calculator.logic import add, subtract, multiply, divide

app = Flask(__name__)

with open("static/index.html", "r", encoding="utf-8") as _f:
    _HTML = _f.read()


@app.route("/")
def index():
    """Serve the calculator UI."""
    return render_template_string(_HTML)


@app.route("/calculate", methods=["POST"])
def calculate():
    """Handle calculation requests from the browser."""
    data = request.get_json()
    a = float(data["a"])
    b = float(data["b"])
    op = data["op"]

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if op not in operations:
        return jsonify({"error": "Unknown operation"}), 400

    try:
        result = operations[op](a, b)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


def cli():
    """Simple CLI interface for the calculator."""
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument(
        "op",
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation",
    )
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    try:
        result = operations[args.op](args.a, args.b)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "web":
        app.run(debug=True)
    else:
        cli()
