# # Processing data:
# # For example, let's say you receive a file that must
# go through a slow process, you can return a response
# of "Accepted" (HTTP 202) and process it in the background.

from fastapi import BackgroundTasks
from typing import Optional

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)

def get_query(background_tasks: BackgroundTasks, q: Optional[str] = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q

