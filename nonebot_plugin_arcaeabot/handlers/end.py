from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment
from nonebot.params import CommandArg
from ..matcher import arc
from ..utils import is_error


async def end_handler(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    args: list = str(args).split()
    reply = args[1] + " 为不支持的命令参数！"
    if is_error():
        await arc.finish(MessageSegment.reply(event.message_id) + reply)
    else:
        await arc.finish()
