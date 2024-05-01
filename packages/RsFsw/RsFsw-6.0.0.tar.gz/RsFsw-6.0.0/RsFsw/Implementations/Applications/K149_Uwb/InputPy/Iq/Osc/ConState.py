from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConStateCls:
	"""ConState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conState", core, parent)

	def get(self) -> float:
		"""SCPI: INPut:IQ:OSC:CONState \n
		Snippet: value: float = driver.applications.k149Uwb.inputPy.iq.osc.conState.get() \n
		Returns the state of the LAN connection to the oscilloscope for the optional Oscilloscope Baseband Input. For details see
		'Processing Oscilloscope Baseband Input'. \n
			:return: connection_state: CONNECTED | NOT_CONNECTED | ESTABLISHING_CONNECTION CONNECTED Connection to the instrument has been established successfully. ESTABLISHING_CONNECTION Connection is currently being established. NOT_CONNECTED Connection to the instrument could not be established. Check the connection between the FSW and the oscilloscope, and make sure the IP address of the oscilloscope has been defined (see method RsFsw.Applications.K149_Uwb.InputPy.Iq.Osc.Tcpip.set) ."""
		response = self._core.io.query_str(f'INPut:IQ:OSC:CONState?')
		return Conversions.str_to_float(response)
