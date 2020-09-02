from server.database import DB


class URLS:
    def __init__(self):
        self.urls_collection = DB().db["urls"]

    async def count_ex_urls(self, slug):
        return self.urls_collection.count({"slug": slug})

    async def insert_urls(self, slug, org_url):
        if await self.count_ex_urls(slug) > 0:
            return False
        else:
            self.urls_collection.insert_one({
                "slug": slug,
                "org_url": org_url
            })
            return True

    async def find_url(self, slug):
        return self.urls_collection.find_one({"slug": slug})

    async def find_all_urls(self):
        return self.urls_collection.find({})
