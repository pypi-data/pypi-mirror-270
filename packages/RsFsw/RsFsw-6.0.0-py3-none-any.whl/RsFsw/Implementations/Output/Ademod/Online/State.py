from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: OUTPut:ADEMod[:ONLine][:STATe] \n
		Snippet: driver.output.ademod.online.state.set(state = False) \n
		Enables or disables online demodulation output to the IF/VIDEO/DEMOD output connector on the rear panel of the FSW. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'OUTPut:ADEMod:ONLine:STATe {param}')

	def get(self) -> bool:
		"""SCPI: OUTPut:ADEMod[:ONLine][:STATe] \n
		Snippet: value: bool = driver.output.ademod.online.state.get() \n
		Enables or disables online demodulation output to the IF/VIDEO/DEMOD output connector on the rear panel of the FSW. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'OUTPut:ADEMod:ONLine:STATe?')
		return Conversions.str_to_bool(response)
