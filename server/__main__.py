import logging
import asyncio
from aiohttp import web
from server.webserver import web_server


async def main():
    runner = web.AppRunner(await web_server())
    await runner.setup()
    await web.TCPSite(runner, "localhost", 8080).start()
    logging.info("Server started: http://localhost:8080")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        loop.run_forever()
    except KeyboardInterrupt:
        logging.error("Keyboard Interruption! Server Shutdown")
    finally:
        loop.close()
        logging.info("Server Shutdown!")
