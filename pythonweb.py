from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)
import requests # pip install requests

import urllib3


app = Flask(__name__)

line_bot_api = LineBotApi('PpNhy1loFsQWx2Iaw5imgbwlNGWibIHuReRgrDxZgLZVyBq1AlQZgaLq5BxAuVFYPVOeOKUeNDvRzKouPDRAzEJ6ER8Hj9lZYPCtdAnRFVWFYiJMWc5wxnAy2lAahX/teOvGh8rGaLj0s8uxAJzj/QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('181d1c80ab13effe16793f4e266e1426')

APPID="LineBotRpi"
KEY = "bjuWQftBs1hMHSw"
SECRET = "EUUdgsgDClUdqdzIDGnwjZ752"
Topic = "/Userprofile"

url = 'https://api.netpie.io/topic/' + str(APPID) + str(Topic)
#curl -X PUT "https://api.netpie.io/topic/LineBotRpi/LED_Control" -d "ON" -u Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I 

urlRESTAPI = 'https://api.netpie.io/topic/' + str(APPID) + str(Topic) + '?auth=' + str(KEY) + ':' + str(SECRET)
#https://api.netpie.io/topic/LineBotRpi/LED_Control?auth=Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I



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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #global url , KEY , SECRET
    text = (str(event.message.text)).lower()
    if text == "profile":
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            #r = requests.put(url, data = {'':str(profile.display_name)} , auth=(str(KEY),str(SECRET)))
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message),
                    TextSendMessage(text='User ID: ' + profile.user_id)
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="ขอโทษด้วยค่ะ ฉันไม่เข้าใจค่ะ I'm sorry. I don't understand."))
            
    elif text == "menu":
        Menu_url = "http://149.28.153.220:1880/ui/#/0" # Menu Web Url
        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url='https://scontent.fbkk6-1.fna.fbcdn.net/v/t1.0-9/39454660_1001737283342645_6691743344214671360_n.jpg?_nc_cat=100&_nc_ht=scontent.fbkk6-1.fna&oh=8155c7522c7b274d7afcf65d5d07dfc2&oe=5CA6BAA1',
                                action=URIAction(uri=Menu_url,
                                                 label='500 Baht')),
            ImageCarouselColumn(image_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.0-9/39442752_1001738930009147_2170020964899749888_n.jpg?_nc_cat=103&_nc_ht=scontent.fbkk6-2.fna&oh=ec390fe97902d919704e68cc36534165&oe=5CAFD3A8',
                                action=URIAction(uri=Menu_url,
                                                 label='80 Baht')),
            ImageCarouselColumn(image_url='https://scontent.fbkk6-1.fna.fbcdn.net/v/t1.0-9/39221449_1001737313342642_6907313284718788608_n.jpg?_nc_cat=108&_nc_ht=scontent.fbkk6-1.fna&oh=63d6884a0af21043195873c19de8a1fc&oe=5CA5B7BB',
                                action=URIAction(uri=Menu_url,
                                                 label='200 Baht'))
        ])
        template_message = TemplateSendMessage(
            alt_text="Thank you.", template=image_carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        
    elif text == "hi" or text == "hello" or text == "hey":
        Menu_url = "http://149.28.153.220:1880/ui/#/0" # Menu Web Url
        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url='https://scontent.fbkk6-1.fna.fbcdn.net/v/t1.0-9/39454660_1001737283342645_6691743344214671360_n.jpg?_nc_cat=100&_nc_ht=scontent.fbkk6-1.fna&oh=8155c7522c7b274d7afcf65d5d07dfc2&oe=5CA6BAA1',
                                action=URIAction(uri=Menu_url,
                                                 label='500 Baht')),
            ImageCarouselColumn(image_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.0-9/39442752_1001738930009147_2170020964899749888_n.jpg?_nc_cat=103&_nc_ht=scontent.fbkk6-2.fna&oh=ec390fe97902d919704e68cc36534165&oe=5CAFD3A8',
                                action=URIAction(uri=Menu_url,
                                                 label='80 Baht')),
            ImageCarouselColumn(image_url='https://scontent.fbkk6-1.fna.fbcdn.net/v/t1.0-9/39221449_1001737313342642_6907313284718788608_n.jpg?_nc_cat=108&_nc_ht=scontent.fbkk6-1.fna&oh=63d6884a0af21043195873c19de8a1fc&oe=5CA5B7BB',
                                action=URIAction(uri=Menu_url,
                                                 label='200 Baht'))
        ])
        template_message = TemplateSendMessage(
            alt_text="Thank you.", template=image_carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    elif text == "contact":
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url="https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.0-9/39308160_1001769490006091_9184433768859959296_o.jpg?_nc_cat=101&_nc_ht=scontent.fbkk6-2.fna&oh=a9b3a35f7a3a7a48bb75fbadeb8c5896&oe=5CAD82C2",
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri="https://tesracademy.wordpress.com/", label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text="TESR Co.,Ltd.", weight='bold', size='xl', margin='md'),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Bangkok, Thailand',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Time',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="09:00 - 22:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
             footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Website', uri="https://tesracademy.wordpress.com")
                    ),
                    # separator
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Facebook', uri="http://www.facebook.com/ThaiEmbedded")
                    ),
                    # separator
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Youtube', uri="http://www.youtube.com/tesrchannel")
                    ),
                    # separator
                    SeparatorComponent(),
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Line@', uri="https://line.me/R/ti/p/%40ion1900z")
                    ),
                    # separator
                    SeparatorComponent(),
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Call', uri='tel:0904656519'),
                    )
                    
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Thank you", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
        
    elif text == "name card":
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            url = "https://api.line.me/v2/bot/message/push"
            token = "PpNhy1loFsQWx2Iaw5imgbwlNGWibIHuReRgrDxZgLZVyBq1AlQZgaLq5BxAuVFYPVOeOKUeNDvRzKouPDRAzEJ6ER8Hj9lZYPCtdAnRFVWFYiJMWc5wxnAy2lAahX/teOvGh8rGaLj0s8uxAJzj/QdB04t89/1O/w1cDnyilFU=" # your Line Notify token
            headers = {'Authorization':'Bearer '+token}
            LineUserID = profile.user_id
            
            msg = {
                "to": profile.user_id ,
                "messages":[
                    {
                        "type":"image",
                        "originalContentUrl":"https://scontent.fbkk7-3.fna.fbcdn.net/v/t1.0-9/48237135_1076094315906941_7505595876794957824_o.jpg?_nc_cat=103&_nc_ht=scontent.fbkk7-3.fna&oh=271db4c48b3e65eda662bfc9e99f9d08&oe=5CA47C98",
                        "previewImageUrl":"https://scontent.fbkk7-3.fna.fbcdn.net/v/t1.0-9/48237135_1076094315906941_7505595876794957824_o.jpg?_nc_cat=103&_nc_ht=scontent.fbkk7-3.fna&oh=271db4c48b3e65eda662bfc9e99f9d08&oe=5CA47C98"
                    }
                ]
            }

            res = requests.post(url, headers=headers , json = msg)

            msg = {
                "to": profile.user_id ,
                "messages":[
                    {
                        "type":"image",
                        "originalContentUrl":"https://scontent.fbkk7-3.fna.fbcdn.net/v/t1.0-9/47689252_1076094299240276_3886605963024662528_n.jpg?_nc_cat=100&_nc_ht=scontent.fbkk7-3.fna&oh=19e4c45d18a293c2e25e623333db5797&oe=5C9826F9",
                        "previewImageUrl":"https://scontent.fbkk7-3.fna.fbcdn.net/v/t1.0-9/47689252_1076094299240276_3886605963024662528_n.jpg?_nc_cat=100&_nc_ht=scontent.fbkk7-3.fna&oh=19e4c45d18a293c2e25e623333db5797&oe=5C9826F9"
                    }
                ]
            }

            res = requests.post(url, headers=headers , json = msg)
            
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="ขอโทษด้วยค่ะ ฉันไม่เข้าใจค่ะ I'm sorry. I don't understand."))

    elif text == "order":
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            #r = requests.put(url, data = {'':str(profile.display_name)} , auth=(str(KEY),str(SECRET)))
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text="http://149.28.153.220:1880/ui/#/0")
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="ขอโทษด้วยค่ะ ฉันไม่เข้าใจค่ะ I'm sorry. I don't understand."))
    #elif "temp?" in text:
        #REST API NETPIE read sensor value
        #r = requests.put(url, data = {'':'temp?'} , auth=(str(KEY),str(SECRET)))
        
        #http = urllib3.PoolManager()
        #response = http.request('GET',urlRESTAPI) # read data from publish retain

        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=((str(response.data)).split('"')[7]) + " °C"))
        
        #r = requests.get(urlRESTAPI)
        #https://api.netpie.io/topic/LineBotRpi/LED_Control?auth=Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I
        
        
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="ขอโทษด้วยค่ะ ฉันไม่เข้าใจค่ะ I'm sorry. I don't understand."))

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(
            title=event.message.title, address=event.message.address,
            latitude=event.message.latitude, longitude=event.message.longitude
        )
    )


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )


@handler.add(BeaconEvent)
def handle_beacon(event):
    Menu_url = "http://149.28.153.220:1880/ui/#/0" # Menu Web Url
    image_carousel_template = ImageCarouselTemplate(columns=[
        ImageCarouselColumn(image_url='https://scontent.fbkk6-1.fna.fbcdn.net/v/t1.0-9/39454660_1001737283342645_6691743344214671360_n.jpg?_nc_cat=100&_nc_ht=scontent.fbkk6-1.fna&oh=8155c7522c7b274d7afcf65d5d07dfc2&oe=5CA6BAA1',
                            action=URIAction(uri=Menu_url,
                                             label='500 Baht')),
        ImageCarouselColumn(image_url='https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.0-9/39442752_1001738930009147_2170020964899749888_n.jpg?_nc_cat=103&_nc_ht=scontent.fbkk6-2.fna&oh=ec390fe97902d919704e68cc36534165&oe=5CAFD3A8',
                            action=URIAction(uri=Menu_url,
                                             label='80 Baht')),
        ImageCarouselColumn(image_url='https://scontent.fbkk6-1.fna.fbcdn.net/v/t1.0-9/39221449_1001737313342642_6907313284718788608_n.jpg?_nc_cat=108&_nc_ht=scontent.fbkk6-1.fna&oh=63d6884a0af21043195873c19de8a1fc&oe=5CA5B7BB',
                            action=URIAction(uri=Menu_url,
                                             label='200 Baht'))
    ])
    template_message = TemplateSendMessage(
        alt_text="Thank you.", template=image_carousel_template)
    line_bot_api.reply_message(event.reply_token, template_message)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Got beacon event. hwid={}, device_message(hex string)={}'.format(
                event.beacon.hwid, event.beacon.dm)))
    line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text="Hi")
                ]
            )


if __name__ == "__main__":
    app.run()
