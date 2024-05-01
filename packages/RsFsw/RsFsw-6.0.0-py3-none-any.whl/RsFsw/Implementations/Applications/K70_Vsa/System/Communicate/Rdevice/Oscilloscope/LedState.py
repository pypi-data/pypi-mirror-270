from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LedStateCls:
	"""LedState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ledState", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.LedState:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:LEDState \n
		Snippet: value: enums.LedState = driver.applications.k70Vsa.system.communicate.rdevice.oscilloscope.ledState.get() \n
		Returns the state of the LAN connection to the oscilloscope for the optional 2 GHz / 5 GHz bandwidth extension
		(FSW-B2000/B5000) . For details see 'Alignment'. \n
			:return: led_state: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)
