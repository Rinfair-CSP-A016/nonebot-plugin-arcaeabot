from typing import List
from nonebot.adapters.onebot.v11 import MessageSegment
from ._RHelper import RHelper
from .AUA.schema.api.another.song_random import Content as SongRandomContent
from .AUA.schema.api.v5.song_info import SongInfo

root = RHelper()


def draw_help():
    return "\n".join(
        [
            "/arc bind <arcaea id> 进行绑定",
            "/arc unbind 解除绑定",
            "/arc info 查看绑定信息",
            "/arc recent 查询上一次游玩记录",
            "/arc b30 查询 best 30 记录",
            "/arc assets_update 更新曲绘与立绘资源",
            "/arc best <曲名> [难度] 查询单曲最高分",
            "/arc song <曲名> [难度] 查询信息",
            "/arc random [难度] 随机指定难度的歌曲",
            "/arc random [难度min] [难度max] 随机指定难度区间的歌曲",
        ]
    )


def draw_song(song_info: SongRandomContent):
    if not isinstance(song_info.song_info, SongInfo):
        image = "file://" + root.assets.song / song_info.song_id / ("base.jpg")
        result = "\n".join(
            [
                f"Name: {song_info.song_info[0].name_en}",
                f"[Past]: {song_info.song_info[0].rating/10}",
                f"[Present]: {song_info.song_info[1].rating/10}",
                f"[Future]: {song_info.song_info[2].rating/10}",
            ]
        )
        result += (
            f"\n[Beyond]: {song_info.song_info[3].rating/10}"
            if len(song_info.song_info) > 3
            else ""
        )
        result += "\n获取详细信息请在添加难度后缀"
    else:
        difficulty = ["Past", "Present", "Future", "Beyond"][song_info.difficulty]
        cover_name = "3.jpg" if difficulty == 3 else "base.jpg"
        image = "file://" + root.assets.song / song_info.song_id / cover_name
        result = "\n".join(
            [
                f"曲名: {song_info.song_info.name_en}[{difficulty}]",
                f"曲师: {song_info.song_info.artist}",
                f"曲绘: {song_info.song_info.jacket_designer}",
                f"时长: " + "%02d:%02d" % divmod(song_info.song_info.time, 60),
                f"BPM:  {song_info.song_info.bpm}",
                f"谱师: {song_info.song_info.chart_designer}",
                f"Note数: {song_info.song_info.note}",
                f"Rating: {song_info.song_info.rating/10}",
                f"隶属曲包: {song_info.song_info.set_friendly}",
                "上线时间: " + song_info.song_info.date.strftime("%Y-%m-%d"),
            ]
        )
        result += "\n需要世界模式解锁" if song_info.song_info.world_unlock is True else ""
        result += "\n需要下载" if song_info.song_info.remote_download is True else ""
    return MessageSegment.image(image) + "\n" + result
