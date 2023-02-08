import aiohttp_jinja2


@aiohttp_jinja2.template("index.html")
async def index(request):
    """A function that will return the html file."""
    return {"title": "Writing the first application on aiohttp"}
