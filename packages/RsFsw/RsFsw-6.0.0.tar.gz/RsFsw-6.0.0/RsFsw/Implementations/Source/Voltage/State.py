from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SOURce:VOLTage[:STATe] \n
		Snippet: driver.source.voltage.state.set(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce:VOLTage:STATe {param}')

	def get(self) -> bool:
		"""SCPI: SOURce:VOLTage[:STATe] \n
		Snippet: value: bool = driver.source.voltage.state.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SOURce:VOLTage:STATe?')
		return Conversions.str_to_bool(response)
