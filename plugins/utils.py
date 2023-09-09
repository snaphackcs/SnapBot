from nonebot.adapters.onebot.v12 import MessageSegment,GroupMessageEvent
import yaml

def send(event:GroupMessageEvent, content:str, type:int=0):
    """
        type: 0是元气, 1是生气, 2是悲伤
    """
    title = "test title"
    emoticons = ['ᕕ( ᐛ )ᕗ', '(╯°□°）╯︵ ┻━┻', '(っ °Д °;)っ']
    return MessageSegment.mention(event.user_id) + MessageSegment.text(f"{title}，{content}{emoticons[type]}")