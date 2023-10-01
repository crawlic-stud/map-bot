import uvicorn

import api
from config import app, API_HOST, API_PORT


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=API_HOST,
        port=API_PORT,
        forwarded_allow_ips="*",
    )
