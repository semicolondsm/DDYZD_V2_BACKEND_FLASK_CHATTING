from firebase_admin import credentials
from firebase_admin import messaging
from firebase_admin import datetime
from app import logger
import firebase_admin
import os


cred = credentials.Certificate('ddyzd-firebase-adminsdk.json')
default_app = firebase_admin.initialize_app(cred)


async def fcm_alarm(sender, msg, token, room_id, user_type):
    try:
        aps = messaging.APNSPayload(messaging.Aps(sound="default"))
        message = messaging.Message(
            notification=messaging.Notification(
                title=sender,
                body=msg  
            ),
            data={"room_id": str(room_id), "user_type": user_type},
            apns=messaging.APNSConfig(payload=aps),
            token=token
        )
        messaging.send(message)
    except Exception as e:
        logger.info(e)