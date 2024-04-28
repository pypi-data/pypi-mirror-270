from apscheduler.schedulers.asyncio import AsyncIOScheduler
from clovers.core.config import config as clovers_config
from clovers.core.plugin import Plugin
from .config import Config


config_key = __package__
config_data = Config.model_validate(clovers_config.get(config_key, {}))
clovers_config[config_key] = config_data.model_dump()

plugin = Plugin()
scheduler = AsyncIOScheduler()
scheduler.configure(**config_data.scheduler_config)


@plugin.startup
async def _():
    if not scheduler.running:
        scheduler.start()


@plugin.shutdown
async def _():
    if scheduler.running:
        scheduler.shutdown()


__plugin__ = plugin
