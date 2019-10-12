from flask import Flask, render_template, jsonify
import minedock

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/new/<name>')
def new(name):
    port = minedock.new_minecraft(name) 
    response = {
            "port": port,
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
