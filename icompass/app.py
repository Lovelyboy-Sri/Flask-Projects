from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_sanitized(input_string):
    sanitized = not re.search(r"[;\\'\"]|\\-", input_string)
    return sanitized

@app.route('/v1/sanitized/input/', methods=['POST'])
def check_sanitization():
    try:
        data = request.get_json()
        input_string = data.get('input')

        if input_string is None:
            return jsonify({"error": "Input not provided"}), 400

        sanitized = is_sanitized(input_string)

        if sanitized:
            result = {"result": "sanitized"}
        else:
            result = {"result": "unsanitized"}

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
