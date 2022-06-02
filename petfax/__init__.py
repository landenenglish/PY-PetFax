from flask import Flask 

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    # import pet.py
    from . import pet
    app.register_blueprint(pet.bp)
    app.register_blueprint(pet.facts)


    return app
