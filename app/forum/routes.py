from app.forum import views


def setup_routes(app):
    """Set up the paths that will lead to the main page."""
    app.router.add_get("/", views.index)
