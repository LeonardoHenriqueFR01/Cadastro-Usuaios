from app import create_app
from app.routes import configure_routes

app = create_app()
configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
