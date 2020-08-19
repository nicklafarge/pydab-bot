from flask_api import FlaskAPI
from config.env import app_env
from app.utils.slackhelper import SlackHelper
from flask import request, jsonify


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')

    @app.route("/", methods=["GET"])
    def home():
        """This route renders a hello world text."""
        # rendering text
        return 'Hello World'

    @app.route("/dabbot/", methods=["POST"])
    def dabbot():
        """Webhook for slack"""
        print(request.data)
        # rendering text
        return dict(
            challenge=request.data['challenge']
        )

    return app
