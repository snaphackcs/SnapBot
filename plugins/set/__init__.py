from nonebot.adapters.onebot.v12 import GroupMessageEvent,MessageSegment,Message
from nonebot.message import event_preprocessor
from nonebot.plugin import on_command
from nonebot.exception import IgnoredException
from nonebot.adapters.onebot.v12.exception import UnsupportedAction
from nonebot import get_bot, get_driver,logger
from os import getcwd
from os.path import join
from .config import Config
from .utils import name
from ..utils import send

# 按照正则表达式匹配，别的匹配方式会在暂时不存在的文档里面提及
# 是大佬就直接读nonebot2的文档，里面有一个on_command的函数，更符合snaphack对于微信机器人的想象
matcher = on_command("set")

sub = Config.parse_obj(get_driver().config).subcommands

# 不需要进行对于群的过滤，已经使用上面hook例子函数过滤了
# 这里的matcher就是上面的on_regex定义的
@matcher.handle()
async def _(event:GroupMessageEvent): # GroupMessageEvent代表收到的是群消息
    bot = get_bot()
    args = event.alt_message.split(" ")[1:]

    if sub[args[0]] == "name":
        if len(args[1]) > 5:
            message = send(event, f"你要不要看看你的名字啥长度", 1)
            await bot.send_message(detail_type="group", group_id=event.group_id, message=message)
            raise IgnoredException("too long for nickname")
        name(args[1], event.get_user_id())
        message = send(event, f"你的名字已被Bot设置为{args[1]}")
        logger.info(event.message_id)
        await bot.send_message(detail_type="group", group_id=event.group_id, message=message)


    await matcher.finish()


    # 表明此事件结束
    

    # [MessageSegment(type='mention', data={'user_id': 'wxid_70w1u71g296j12'}), MessageSegment(type='text', data={'text': 'hi'})]
    # [MessageSegment(type='text', data={'text': '/set -n '}), MessageSegment(type='mention', data={'user_id': 'wxid_vhuqscg5tjnu22'}), MessageSegment(type='text', data={'text': 'taizi'})]