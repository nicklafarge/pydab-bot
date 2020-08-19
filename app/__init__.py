from flask_api import FlaskAPI
from config.env import app_env
from app.utils.slackhelper import SlackHelper
from flask import request, jsonify
from app import dabber


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

        post_json = dict()

        data = request.data

        # Respond to webhook challenge appropriately
        if 'challenge' in request.data:
            post_json['challenge'] = data['challenge']

        if 'event' in request.data:
            dabber.dab(data['event'])

        # rendering text
        return post_json

    return app
