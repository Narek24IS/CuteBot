from aiogram import Router, F
from config import load_config, Config

config: Config = load_config()
router = Router()
router.message.filter(F.from_user.id == config.bot.admin_id)
test = 'text'