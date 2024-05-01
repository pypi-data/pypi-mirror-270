from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ViqDataCls:
	"""ViqData commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("viqData", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: MMEMory:SELect[:ITEM]:VIQData \n
		Snippet: driver.massMemory.select.item.viqData.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'MMEMory:SELect:ITEM:VIQData {param}')

	def get(self) -> bool:
		"""SCPI: MMEMory:SELect[:ITEM]:VIQData \n
		Snippet: value: bool = driver.massMemory.select.item.viqData.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'MMEMory:SELect:ITEM:VIQData?')
		return Conversions.str_to_bool(response)
