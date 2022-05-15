import logging

from .. import loader, utils

@loader.tds
class ChirovMod(loader.Module):
	"""Слава украине на каждое сообщение чирова"""
	strings = {
        'name': 'Chirov')
        
        async def chirovcmd(self, message):
        	"""Kekw"""
        logger.debug("logged")
        await utils.answer(message, "да")
