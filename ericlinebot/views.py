from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

import json
import time
import random
 
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

starting_card = json.load(open('./flexMessages/starting_card.json','r',encoding='utf-8'))
work_experience = json.load(open('./flexMessages/work_experience.json', 'r', encoding='utf-8'))
education = json.load(open('./flexMessages/education.json', 'r', encoding='utf-8'))
skill_set = json.load(open('./flexMessages/skill_set.json', 'r', encoding='utf-8'))
portfolio = json.load(open('./flexMessages/portfolio.json', 'r', encoding='utf-8'))
responses = ["Don't count on it", "My reply is no", "My sources say no", "Very doubtful", "As I see it, yes", "Most likely", "Signs point to yes", "Outlook good", "It is certain", "It is decidedly so", "Without a doubt", "Better not tell you now", "Concentrate and ask again"]

line_bot_api.push_message('U2d4cd006f276c9f77ff776ab9ac36677', FlexSendMessage('profile',starting_card))

@csrf_exempt
def callback(request):
 
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
 
        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if event.message.text == "Work Experience":
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('work experience', work_experience))
                elif event.message.text == "Education":
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('education', education))
                elif event.message.text == "Skill Set":
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('skill set', skill_set))
                elif event.message.text == "Personal Portfolio":
                    line_bot_api.reply_message(event.reply_token, FlexSendMessage('personal portfolio', portfolio))
                else:
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(text=random.choice(responses))
                    )
                time.sleep(2)
                line_bot_api.push_message('U2d4cd006f276c9f77ff776ab9ac36677', FlexSendMessage('profile',starting_card))
        return HttpResponse()
    else:
        return HttpResponseBadRequest()