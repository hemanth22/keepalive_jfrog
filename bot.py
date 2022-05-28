import telepot
import os
token = os.environ.get("TELE_CHANNEL")
receiver_id = os.environ.get("CHATTER_ID") # https://api.telegram.org/bot<TOKEN>/getUpdates
bot = telepot.Bot(token)
bot.sendMessage(receiver_id, 'keepalive_jfrog: Job Completed Notification.') # send a activation message to telegram receiver id
