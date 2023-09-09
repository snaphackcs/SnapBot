from nonebot.adapters.onebot.v12 import MessageSegment, GroupMessageEvent
import yaml
from os import getcwd
from os.path import join
from nonebot.exception import IgnoredException


def send(event: GroupMessageEvent, content: str, type: int = 0):
    """
        type: 0是元气, 1是生气, 2是悲伤
    """
    title = "test title"
    emoticons = ['ᕕ( ᐛ )ᕗ', '(╯°□°）╯︵ ┻━┻', '(っ °Д °;)っ']
    return MessageSegment.mention(event.user_id) + MessageSegment.text(f"{title}，{content}{emoticons[type]}")


def add_user(event: GroupMessageEvent):
    path = join(getcwd(), r"\data\user_data.yaml")

    with open(path, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    if event.get_user_id() in data.keys():
        raise IgnoredException("User already exists!")
    user_info = data["wxid_example"]
    user_info["name"] = "*输入“/set -n 姓名”以录入姓名*"
    user_info["pinyin"] = "weiluru"
    user = {event.get_user_id(): user_info}

    with open(path, 'a') as file:
        yaml.dump(user, file)
