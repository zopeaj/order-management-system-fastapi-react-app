from fastapi import FastAPI

apiv1 = FastAPI()

@apiv1.get("/hello-version1")
def index():
    return {"Name": "Kaustub demo"}
