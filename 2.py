import logging

from .. import loader, utils

@loader.tds
class ChirovMod(loader.Module):
	"""Слава bebra на каждое сообщение чирова"""
	strings = {
        'name': 'Chirov')
        
        async def chirovcmd(self, message):
        	"""Kekw"""
        await utils.answer(message, "да")
