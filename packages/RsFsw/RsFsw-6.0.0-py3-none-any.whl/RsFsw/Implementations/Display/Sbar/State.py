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
		"""SCPI: DISPlay:SBAR[:STATe] \n
		Snippet: driver.display.sbar.state.set(state = False) \n
		This command turns the status bar on and off. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'DISPlay:SBAR:STATe {param}')

	def get(self) -> bool:
		"""SCPI: DISPlay:SBAR[:STATe] \n
		Snippet: value: bool = driver.display.sbar.state.get() \n
		This command turns the status bar on and off. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'DISPlay:SBAR:STATe?')
		return Conversions.str_to_bool(response)
