from django.core.management.base import BaseCommand
import asyncio
from project.app.bot.main_bot import bot


class Command(BaseCommand):
    help = "Запуск бота"

    def handle(self, *args, **options):
        
        asyncio.run(bot.polling())
        