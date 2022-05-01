from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment
from nonebot.params import CommandArg
from ..matcher import arc


async def unbind_handler(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    args: list = str(args).split()
    if args[0] == "calc":

        score, ptt, ptt2 = 60

        if int(args[1]) == range(600, 10002000):
            score = int(args[1])
        if int(args[2]) == range(600, 10002000):
            score = int(args[2])
        if float(args[1]) == range(0, 11.5):
            ptt = float(args[1])
        if float(args[2]) == range(0, 11.5):
            ptt2 = float(args[2])

        if ptt != 60 and ptt2 != 60:
            if ptt - ptt2 <= -1:
                reply = "曲面定数为 [%.2f]\n单曲 Rating 为 [%.2lf]\n计算结果: %d", ptt, ptt2, 9800000 - (ptt - ptt2 + 1) * 200000
                await arc.finish(MessageSegment.reply(event.message_id) + reply)
            else:
                reply = "曲面定数为 [%.2f]\n单曲 Rating 为 [%.2lf]\n计算结果: %d", ptt, ptt2, 9500000 - (ptt - ptt2) * 300000
                await arc.finish(MessageSegment.reply(event.message_id) + reply)

        if score == 60 or ptt == 60:
            await arc.finish(MessageSegment.reply(event.message_id) + "无法合理计算")

        if score >= 10000000:
            score = 10000000

        if score >= 9800000:
            reply = "曲面定数为 [%.2f]\n单曲分数为 [%d]\n计算结果: %.2lf", ptt, score, (10000000 - score) / 200000 + ptt
            await arc.finish(MessageSegment.reply(event.message_id) + reply)

        if score >= 1200:
            reply = "曲面定数为 [%.2f]\n单曲分数为 [%d]\n计算结果: %.2lf", ptt, score, (9800000 - score) / 300000 + ptt
            await arc.finish(MessageSegment.reply(event.message_id) + reply)

        if score >= 1000:
            score = 1000

        if score >= 980:
            reply = "曲面定数为 [%.2f]\n单曲分数为 [%d]w\n计算结果: %.2lf", ptt, score, (10000000 - score * 10000) / 200000 + ptt
            await arc.finish(MessageSegment.reply(event.message_id) + reply)

        if score > 60:
            reply = "曲面定数为 [%.2f]\n单曲分数为 [%d]w\n计算结果: %.2lf", ptt, score, (9800000 - score * 10000) / 300000 + ptt
            await arc.finish(MessageSegment.reply(event.message_id) + reply)
