from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:IQ:OSC[:STATe] \n
		Snippet: driver.applications.k149Uwb.inputPy.iq.osc.state.set(state = False) \n
		Activates or deactivates Oscilloscope Baseband Input from a connected oscilloscope. This input requires optional firmware. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Oscilloscope Baseband Input not active ON | 1 Oscilloscope Baseband Input active
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:IQ:OSC:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:IQ:OSC[:STATe] \n
		Snippet: value: bool = driver.applications.k149Uwb.inputPy.iq.osc.state.get() \n
		Activates or deactivates Oscilloscope Baseband Input from a connected oscilloscope. This input requires optional firmware. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Oscilloscope Baseband Input not active ON | 1 Oscilloscope Baseband Input active"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:STATe?')
		return Conversions.str_to_bool(response)
