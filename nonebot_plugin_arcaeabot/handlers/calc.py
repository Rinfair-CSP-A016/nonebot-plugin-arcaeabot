from nonebot.adapters.onebot.v11 import Bot, MessageEvent, Message, MessageSegment
from nonebot.params import CommandArg
from ..matcher import arc
from ..utils import is_float_num


def calc(ptt: float, score: int, ptt2: float = -100):
    if ptt2 != -100:
        if ptt - ptt2 <= -1:
            ans = 9800000 - (ptt - ptt2 + 1) * 200000
        else:
            ans = 9500000 - (ptt - ptt2) * 300000
    else:
        if score >= 9800000:
            ans = (score - 9800000) / 200000 + ptt
        else:
            ans = (score - 9500000) / 300000 + ptt
    if ans < 0:
        return 0
    return ans


async def calc_handler(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    args: list = str(args).split()
    if args[0] == "calc":

        score, ptt, ptt2 = 60, 60, 60

        if is_float_num(args[1]):
            if 0 <= float(args[1]) <= 60:
                ptt = float(args[1])

        if args[2].isdigit():
            if 60 <= int(args[2]) <= 10002000:
                score = int(args[2])
        if is_float_num(args[2]):
            if 0 <= float(args[2]) <= 60:
                ptt2 = float(args[2])

        if ptt != 60 and ptt2 != 60:
            if ptt - ptt2 <= -1:
                reply = "曲面定数：%.2f\n单曲 Rating ：%.2lf\n计算结果: %d" % (ptt, ptt2, calc(ptt=ptt, ptt2=ptt2))
                await arc.finish(MessageSegment.reply(event.message_id) + reply)
            else:
                reply = "曲面定数：%.2f\n单曲 Rating ：%.2lf\n计算结果: %d" % (ptt, ptt2, calc(ptt=ptt, ptt2=ptt2))
                await arc.finish(MessageSegment.reply(event.message_id) + reply)

        if score == 60 or ptt == 60:
            await arc.finish(MessageSegment.reply(event.message_id) + "无法合理计算！")

        if score >= 10000000:
            score = 10000000

        if score >= 9800000:
            reply = "曲面定数：%.2f\n单曲分数：%d\n计算结果: %.2lf" % (ptt, score, calc(ptt=ptt, score=score))
            await arc.finish(MessageSegment.reply(event.message_id) + reply)

        if score >= 1200:
            reply = "曲面定数：%.2f\n单曲分数：%d\n计算结果: %.2lf" % (ptt, score, calc(ptt=ptt, score=score))
            await arc.finish(MessageSegment.reply(event.message_id) + reply)

        if score >= 1000:
            score = 1000

        if score >= 980:
            reply = "曲面定数：%.2f\n单曲分数：%dw\n计算结果: %.2lf" % (ptt, score, (score * 10000 - 9800000) / 200000 + ptt)
            await arc.finish(MessageSegment.reply(event.message_id) + reply)

        if score > 60:
            reply = "曲面定数：%.2f\n单曲分数：%dw\n计算结果: %.2lf" % (ptt, score, (score * 10000 - 9500000) / 300000 + ptt)
            await arc.finish(MessageSegment.reply(event.message_id) + reply)
