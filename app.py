from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_info():
    email = "ovedheo@gmail.com"
    current_datetime = datetime.datetime.now(datetime.UTC) + "Z"
    github_url = "https://github.com/oreva12/Public-Api.git"

    return jsonify({
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)