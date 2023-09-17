import aiosqlite
from nonebot import get_bot, get_driver, logger, matcher
from nonebot.internal import driver
from nonebot.params import CommandArg
from nonebot.plugin import on_command
from nonebot.matcher import Matcher
from nonebot.message import event_preprocessor
from nonebot.exception import IgnoredException 
from nonebot.adapters.onebot.v12 import GroupMessageEvent, MessageSegment
from nonebot.adapters import Message


# 填写管理员用户的微信id
admins = []

matcher = on_command("admin")

driver = get_driver()

@driver.on_startup
async def get_admin_user():
    pass

# 需要用数据库来判断是否是admin user
@event_preprocessor
async def whitelist(event: GroupMessageEvent):
    pass


@matcher.handle()
async def _(event:GroupMessageEvent, m:Matcher, args:Message = CommandArg()):


@matcher.got()
