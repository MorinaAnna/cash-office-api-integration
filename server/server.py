from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def info():
    login = request.args.get('login')
    if not login:
        return Response(
            json.dumps({"error": "Параметр 'login' обов'язковий"}, ensure_ascii=False),
            mimetype='application/json'
        )

    result = {
        "login": login,
        "name": "Моріна Анна",
        "course": "2",
        "group": "ІС-33"
    }

    return Response(
        json.dumps(result, ensure_ascii=False, indent=2),
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)
