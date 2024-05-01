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
		"""SCPI: OUTPut:IQHS[:STATe] \n
		Snippet: driver.output.iqhs.state.set(state = False) \n
		Enables or disables a digital output stream to the optional QSFP+ connector, if available. For details on Digital I/Q 40G
		Streaming Output (FSW-B517/-B1017) , see 'Digital I/Q 40G Streaming Output'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'OUTPut:IQHS:STATe {param}')

	def get(self) -> bool:
		"""SCPI: OUTPut:IQHS[:STATe] \n
		Snippet: value: bool = driver.output.iqhs.state.get() \n
		Enables or disables a digital output stream to the optional QSFP+ connector, if available. For details on Digital I/Q 40G
		Streaming Output (FSW-B517/-B1017) , see 'Digital I/Q 40G Streaming Output'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'OUTPut:IQHS:STATe?')
		return Conversions.str_to_bool(response)
