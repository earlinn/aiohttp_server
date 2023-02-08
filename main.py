from aiohttp import web
import jinja2
import aiohttp_jinja2


def setup_routes(application):
    """Setting url paths for the entire application."""
    from app.forum.routes import setup_routes as setup_forum_routes

    setup_forum_routes(application)


def setup_external_libraries(application: web.Application) -> None:
    """
    Specify that html templates should be searched in the templates folder.
    """
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))


def setup_app(application):
    """Configuring the application."""
    setup_external_libraries(application)
    setup_routes(application)


app = web.Application()  # Create web server

if __name__ == "__main__":
    setup_app(app)
    web.run_app(app)
