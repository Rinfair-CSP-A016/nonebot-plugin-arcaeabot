from nonebot_plugin_arcaea.handlers.assets_update import assets_update_handler
from .matcher import arc
from .handlers import (
    help_handler,
    bind_handler,
    pre_handler
)


arc.handle()(help_handler)
arc.handle()(bind_handler)
arc.handle()(pre_handler)
arc.handle()(assets_update_handler)