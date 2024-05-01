from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NameCls:
	"""Name commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("name", core, parent)

	def set(self, name: str) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:NAME \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.name.set(name = 'abc') \n
		No command help available \n
			:param name: No help available
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:NAME {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:NAME \n
		Snippet: value: str = driver.applications.k70Vsa.sense.ddemod.search.sync.name.get() \n
		No command help available \n
			:return: name: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:NAME?')
		return trim_str_response(response)
