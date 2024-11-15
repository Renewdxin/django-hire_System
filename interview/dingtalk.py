from dingtalkchatbot.chatbot import DingtalkChatbot
from django.conf import settings

def send(message, at_mobiles=[]):
    webhook = settings.DINGTALK_WEB_HOOK