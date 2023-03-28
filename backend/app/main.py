from fastapi import FastAPI, BackgroundTasks, Request
from app.utilities.backgrounTask import write_notification, write_log
from app.business.infra.controller.api_v1.ApiControllerV1 import apiv1
from app.business.infra.controller.api_v1.ApiControllerV2 import apiv2
import uvicorn

app = FastAPI(title="", openapi_url="", root_path="/api/v1")
app.mount("/api/v1", apiv1)
app.mount("/api/v2", apiv2)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notifiaction")
    return {"message": "Notification sent in the background"}

@app.post("/send-notification/{email}")
async def send_notification_data(email: str, background_tasks: BackgroundTasks):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}

@app.get("/app")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}

@app.get("/")
def index():
    return {"greet": "Helo"}


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
