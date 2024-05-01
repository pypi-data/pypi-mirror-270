from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:LISN:FILTer:HPASs[:STATe] \n
		Snippet: driver.applications.k70Vsa.inputPy.lisn.filterPy.hpass.state.set(state = False) \n
		Turns the 150 kHz highpass filter for the ENV216 network on and off. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:LISN:FILTer:HPASs:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:LISN:FILTer:HPASs[:STATe] \n
		Snippet: value: bool = driver.applications.k70Vsa.inputPy.lisn.filterPy.hpass.state.get() \n
		Turns the 150 kHz highpass filter for the ENV216 network on and off. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'INPut:LISN:FILTer:HPASs:STATe?')
		return Conversions.str_to_bool(response)
