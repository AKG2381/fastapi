import time
from fastapi import FastAPI, BackgroundTasks, Depends

app = FastAPI()

# def write_notifications(email: str, message: str = ''):
#     with open('26_log.txt', 'w') as email_file:
#         content = "notification for %s : %s" % (email, message)
#         time.sleep(5)  # Simulate a delay
#         email_file.write(content)

# @app.post('/send_notification/{email}', status_code=202)
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notifications, email=email, message='some notification')
#     return {'message': 'Notification sent in the background'}


def write_log(message : str):
    with open('26_log.txt', mode='a') as log:
        log.write(message)

def get_query(backgound_tasks : BackgroundTasks, q : str | None = None):
    if q:
        message = f'found query : {q}\n'
        backgound_tasks.add_task(write_log, message)
    return q


@app.post('/send-notification/{email}', status_code=202)
async def send_notification(email : str , 
                            background_tasks : BackgroundTasks, 
                            q : str = Depends(get_query)):
    message = f'messag to {email}\n'
    background_tasks.add_task(write_log, message)
    return {'message': 'message sent', 'query' : q}
