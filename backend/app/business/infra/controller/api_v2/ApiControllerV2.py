from fastapi import FastAPI
from sys

apiv2 = FastAPI()

@apiv2.get("/hello-version2")
def index():
    return {"Platform-Name": sys.platform}
