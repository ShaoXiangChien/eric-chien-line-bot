import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage, MessageEvent, TextMessage

app = Flask(__name__)

line_bot_api = LineBotApi('mozgQGxP0txg0rmKQCgthq0VsKbr5KqzAG4fhO155bbC4yg6cHi1LqZVBXs0JZeTXmhgwPyn7VFwPteHP6+BSmo91qiOXS1SNJvyxYjSWzHo44wSnlUJ7A3Eh+GoC3VSWG4tfjFDoF/2VoFby61L2AdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('e166c647ee962df3a0e77a663344d0f7')
line_bot_api.push_message('U2d4cd006f276c9f77ff776ab9ac36677', TextSendMessage(text='你可以開始了'))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text="Welcome! Eric is a awesome guy.")
    line_bot_api.reply_message(event.reply_token,message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)