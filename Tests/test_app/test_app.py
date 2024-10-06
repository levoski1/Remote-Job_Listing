from flask import abort
from app import create_app
app = create_app()


@app.route('/not_found/')
def not_found():
    abort(404)

@app.route('/unauthorized/')
def unauthorize():
    abort(401)

@app.route('/method/')
def method():
    abort(405)

@app.route('/forbidden/')
def forbidden():
    abort(403)

@app.route('/internal/')
def internal():
    abort(500)



if __name__ == '__main__':
    app.run(debug=True)