from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:IQ:OSC:BALanced[:STATe] \n
		Snippet: driver.inputPy.iq.osc.balanced.state.set(state = False) \n
		No command help available \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Single ended ON | 1 Differential
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:IQ:OSC:BALanced:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:IQ:OSC:BALanced[:STATe] \n
		Snippet: value: bool = driver.inputPy.iq.osc.balanced.state.get() \n
		No command help available \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Single ended ON | 1 Differential"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:BALanced:STATe?')
		return Conversions.str_to_bool(response)
