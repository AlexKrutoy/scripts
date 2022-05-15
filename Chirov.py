import logging

from .. import loader, utils

@loader.tds
class ChirovMod(loader.Module):
	"""Слава украине на каждое сообщение чирова"""
	strings = {
        'name': 'Chirov'}
        
@loader.unrestricted
async def chirovcmd(self, message):
	"""Слава украине"""
	logger.debug("logged")
	await utils.answer(message, "да")
