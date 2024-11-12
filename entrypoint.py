import uvicorn

from api.app import app
from config import config

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=config.HOST,
        port=config.PORT,
    )
