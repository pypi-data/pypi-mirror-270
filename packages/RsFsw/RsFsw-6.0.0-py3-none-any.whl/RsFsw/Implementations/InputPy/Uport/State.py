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
		"""SCPI: INPut:UPORt:STATe \n
		Snippet: driver.inputPy.uport.state.set(state = False) \n
		Toggles the control lines of the user ports for the AUX PORT connector. This SUB-D male connector is located on the rear
		panel of the FSW. See 'Aux. Port' for details. \n
			:param state: ON | 1 User port is switched to INPut OFF | 0 User port is switched to OUTPut
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:UPORt:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:UPORt:STATe \n
		Snippet: value: bool = driver.inputPy.uport.state.get() \n
		Toggles the control lines of the user ports for the AUX PORT connector. This SUB-D male connector is located on the rear
		panel of the FSW. See 'Aux. Port' for details. \n
			:return: state: ON | 1 User port is switched to INPut OFF | 0 User port is switched to OUTPut"""
		response = self._core.io.query_str(f'INPut:UPORt:STATe?')
		return Conversions.str_to_bool(response)
