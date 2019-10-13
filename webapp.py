from flask import Flask, render_template, jsonify, session
from tinydb import TinyDB, Query
import minedock

app = Flask(__name__)
app.secret_key = b'qzcjqznh+6C<F9I'

db = TinyDB('servers.db')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/new/<name>/<op>/')
def new(name, op):
    if not "quota" in session:
        session["quota"] = 0

    elif int(session["quota"]) > 1:
        return jsonify({ "status": "error", "message": "too much servers" })

    Server = Query()
    if not len(db.search(Server.name == name)) == 0:
        return jsonify({ "status": "error", "message": "name already taken"})

    port = minedock.new_minecraft(name, op) 
    db.insert({ "name": name, "op": op, "port": port})

    response = {
            "status": "ok",
            "name": name,
            "port": port
    }

    session["quota"] += 1
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
