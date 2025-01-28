from flask import render_template


def configure_routes(app):
    @app.route("/")
    def index():
        return "<h1>Bem-vindo ao Flask!</h1>"
