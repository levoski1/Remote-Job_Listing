from flask import abort
from app import create_app
app = create_app()


@app.route('/not_found', strict_slashes=False)
def not_found():
    abort(404)

@app.route('/unauthorized', strict_slashes=False)
def unauthorize():
    abort(401)

@app.route('/method', strict_slashes=False)
def method():
    abort(405)

@app.route('/forbidden', strict_slashes=False)
def forbidden():
    abort(403)

@app.route('/internal', strict_slashes=False)
def internal():
    abort(500)



if __name__ == '__main__':
    app.run(debug=True)