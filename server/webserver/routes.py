import secrets
from aiohttp import web
from server.database.urls import URLS

routes = web.RouteTableDef()


@routes.get("/")
async def root_handler(request):
    url_collection_results = await URLS().find_all_urls()
    documents = []

    for document in url_collection_results:
        if document:
            documents.append({
                "slug": document["slug"],
                "org_url": document["org_url"]
            })
        else:
            documents.append("None")

    json_res = {
        "urls": documents
    }

    return web.json_response(json_res)


@routes.post("/create_url/{org_url}")
async def create_urls(request):
    org_url = request.match_info["org_url"]
    slug = secrets.token_hex(2)

    if await URLS().insert_urls(slug, org_url):
        return web.json_response({
            "status": True,
            "slug": slug,
            "org_url": org_url
        })
    else:
        raise web.HTTPError


@routes.get("/{slug}")
async def redirect_handler(request):
    slug = request.match_info["slug"]
    org_url = await URLS().find_url(slug)
    if org_url:
        if str(org_url["org_url"])[0:4] != "http":
            raise web.HTTPFound(f"https://{org_url['org_url']}")
        else:
            raise web.HTTPFound(str(org_url["org_url"]))
