from flask import Flask


def create_app():
    app = Flask(__name__)

    # Configuration files
    app.config.from_object('config')

    # Blueprints
    from frontend.views import frontend_bp

    app.register_blueprint(frontend_bp)

    return app