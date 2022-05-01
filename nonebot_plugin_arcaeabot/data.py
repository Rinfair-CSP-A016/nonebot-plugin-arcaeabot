from nonebot.log import logger
from os import makedirs, path
import peewee as pw
from ._RHelper import RHelper

root = RHelper()
makedirs(root.database, exist_ok=True)
db = pw.SqliteDatabase(root.database / ("user_data.db"))


class UserInfo(pw.Model):
    user_qq = pw.IntegerField()
    arcaea_id = pw.CharField()
    arcaea_name = pw.CharField()

    class Meta:
        database = db
        primary_key = pw.CompositeKey("user_qq", "arcaea_id")

class UserConfig(pw.Model):
    user_qq = pw.IntegerField()
    single_song_theme = pw.CharField()
    best30_theme = pw.CharField()


    class Meta:
        database = db
        primary_key = pw.CompositeKey("user_qq", "single_song_theme", "best30_theme")

if not path.exists(root.database / ("user_data.db")):
    logger.info("创建数据库于", root.database / ("user_data.db"))
    db.connect()
    db.create_tables([UserInfo])
    db.close()
else:
    db.connect()
    if "userconfig" not in db.get_tables():
        db.create_tables([UserConfig])
