from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment
from nonebot.params import CommandArg
from ..matcher import arc
from ..data import UserInfo
from ..draw_image import UserArcaeaInfo
from ..utils import is_error


async def b30_handler(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    args: list = str(args).split()

    if args[0] == "b30" or args[0] == "b40":

        user_info = UserInfo.get_or_none(UserInfo.user_qq == event.user_id)

        # Expection
        if is_error(mode="more") and len(args) >= 2:
            await arc.send(MessageSegment.reply(event.message_id) + "过多的命令参数！")

        if not user_info:
            await arc.finish(MessageSegment.reply(event.message_id) + "你还没绑定呢！")

        if UserArcaeaInfo.is_querying(user_info.arcaea_id):
            if is_error():
                await arc.finish(MessageSegment.reply(event.message_id) + "您已在查询队列, 请勿重复发起查询。")
            else:
                await arc.finish()

        # Query
        result = await UserArcaeaInfo.draw_user_b30(user_info.arcaea_id)
        await arc.finish(MessageSegment.reply(event.message_id) + result)
