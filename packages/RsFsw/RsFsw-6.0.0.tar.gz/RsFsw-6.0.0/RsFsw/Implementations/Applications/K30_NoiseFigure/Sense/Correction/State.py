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
		"""SCPI: [SENSe]:CORRection[:STATe] \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.state.set(state = False) \n
		Turns correction of measurement results (normalization) on and off. The command is available after you have created a
		reference trace for the selected measurement type with [SENSe:]CORRection:COLLect[:ACQuire]. Is only available if
		External Generator Control (R&S FSW-B10) is installed and active. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:CORRection:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:CORRection[:STATe] \n
		Snippet: value: bool = driver.applications.k30NoiseFigure.sense.correction.state.get() \n
		Turns correction of measurement results (normalization) on and off. The command is available after you have created a
		reference trace for the selected measurement type with [SENSe:]CORRection:COLLect[:ACQuire]. Is only available if
		External Generator Control (R&S FSW-B10) is installed and active. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:CORRection:STATe?')
		return Conversions.str_to_bool(response)
