# coding:utf-8

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,VideoSendMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('vEb134DjvH4ysAh3GcTXwfE2KreIH1EMWEUqeBW0yoEqY1vAEtOI9qNzlqiH78WhK0r6cHYLXWvt1N14gwQMyXK77VdWVBw2Szflwt36M4gzzDFvmybi7uUTDg4G271cJkMeifAegSRqWz0sK/QdCgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('f017e0b208dc1759fee4ad4fa86a7f95')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
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

countt = 0
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    global countt
    Listentext = event.message.text
    Listentext = Listentext.lower()
    helptable="請輸入關鍵字來獲得更多訊息：\n-> 觀看自介影片:video\n-> 查看我的個人網頁:myweb\n-> 查看我的Github:github\n\n更詳盡的自我介紹請輸入:aboutme"
    if countt == 0:
        message = TextSendMessage(text=("Hello, 大家好～～\n我是廖莉祺(Claire Liao)\n"+helptable))
        
        line_bot_api.reply_message(event.reply_token, message)
        countt = 1
    elif countt==1:
        if Listentext=="video":
            message = VideoSendMessage(
                type="video",
                original_content_url='https://www.csie.ntu.edu.tw/~b04902046/profile_web_1.mp4',
                preview_image_url='https://www.csie.ntu.edu.tw/~b04902046/cx617.jpg'
            )
            line_bot_api.reply_message(event.reply_token, message)

        elif "myweb" == Listentext:
            message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
            thumbnail_image_url='https://xiao617.github.io/csx_linker/cx617.jpg',
            title='Myweb',
            text='View my web!',
            actions=[
                URITemplateAction(
                    label='view my web',
                    uri='https://www.csie.ntu.edu.tw/~b04902046/'
                )
                ]
            )
        )
            line_bot_api.reply_message(event.reply_token, message)
        elif "github" == Listentext:
            message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
            thumbnail_image_url='https://avatars0.githubusercontent.com/u/9919?s=280&v=4',
            title='My Github',
            text='All my work is on github!',
            actions=[
                URITemplateAction(
                    label='view my github',
                    uri='https://github.com/xiao617'
                )
                ]
            )
        )
            line_bot_api.reply_message(event.reply_token, message)
        elif "aboutme" == Listentext:
            message = TextSendMessage(text="hello,我是廖莉祺\n目前就讀台大資工\n(你可以問我研究相關的問題\n或是輸入:返回)")
        
            line_bot_api.reply_message(event.reply_token, message)
            countt = 2
        elif "123" == Listentext:
            hint = "我會唸詩還會說笑話啊"
            message = TextSendMessage(text=hint)
            stickerr = StickerSendMessage(
                    package_id='1',
                    sticker_id='2'
            )
            line_bot_api.reply_message(event.reply_token, (message,stickerr))
            countt = 3
        else:
            message = TextSendMessage(text=helptable)
            line_bot_api.reply_message(event.reply_token, message)
    elif countt==2:
        if "返回" in Listentext:
            message = TextSendMessage(text=helptable)
            line_bot_api.reply_message(event.reply_token, message)
            countt = 1
        elif "研究細節" in Listentext:
            myresearch = "computer vision:\n我主要是做Motion recognition\n以及360 image detection\nrobotics:\n是做機器人的控制\n特別是使用pepper\n\n如果你想知道我的研究經歷\n歡迎跟我聊，\n或是輸入:返回"
            message = TextSendMessage(text=myresearch)
            line_bot_api.reply_message(event.reply_token, message)
        elif "研究經歷" in Listentext:
            myresearch = "我目前是在台大傅立成教授的智慧機器人實驗室以及中研院劉庭祿教授的電腦視覺實驗室\n\n2017/2~now:智慧機器人實驗室\n2018/1~now:電腦視覺實驗室\n\n輸入:返回\n或是使用help"
            message = TextSendMessage(text=myresearch)
            line_bot_api.reply_message(event.reply_token, message)
        elif ("research" in Listentext) or ("Research" in Listentext) or ("研究" in Listentext) or ("專題" in Listentext):
            myresearch = "我的專題領域是:\n-> computer vision &\n-> robotics\n如果你想進一步了解\n可以跟我聊聊研究細節\n(如果你不知道該說什麼\n也可以使用help)"
            message = TextSendMessage(text=myresearch)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            researchtable = "這部分你可以跟我聊聊：\n\t1.研究\n\t2.研究細節\n\t3.研究經歷\n\n或是輸入:返回"
            message = TextSendMessage(text=researchtable)
            line_bot_api.reply_message(event.reply_token, message)
    
    #message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(
    #    event.reply_token,
    #    message)
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)