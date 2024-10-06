from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import config



db = SQLAlchemy()

def create_app():
    '''Creating an app'''
    app = Flask(__name__)
    # # This loads the cofiguration from the external file `config.py`
    app.config.from_object(config)

    db.init_app(app)

    #Register blueprint
    from app.jobs.routes import jobs_bp
    app.register_blueprint(jobs_bp)


    # error handler

    @app.errorhandler(404)
    def not_found(error):
        '''Error 404 not found'''
        return jsonify({"Error": "Sorry Not Found"}), 404

    @app.errorhandler(401)
    def unauthorized(error):
        ''' Unathorized '''
        return jsonify({'Error': 'Not authorized'}), 401

    @app.errorhandler(403)
    def forbidden(error):
        ''' forbidden '''
        return jsonify({'Error': 'Forbidden'}), 403

    @app.errorhandler(405)
    def method_not_found(error):
        ''' method not found '''
        return jsonify({'Error': 'Method Not found'}), 405

    @app.errorhandler(500)
    def internal_error(error):
        ''' server Error '''
        return jsonify({'Error': 'internal error'}), 500
    
    
    return app

