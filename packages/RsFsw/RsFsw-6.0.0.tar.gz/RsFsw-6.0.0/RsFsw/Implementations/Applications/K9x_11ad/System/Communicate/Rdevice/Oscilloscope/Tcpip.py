from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcpipCls:
	"""Tcpip commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcpip", core, parent)

	def set(self, tcpip: str) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:TCPip \n
		Snippet: driver.applications.k9X11Ad.system.communicate.rdevice.oscilloscope.tcpip.set(tcpip = 'abc') \n
		Defines the TCPIP address or computer name of the oscilloscope connected to the FSW via LAN. Note: The IP address is
		maintained after a [PRESET], and is transferred between applications. \n
			:param tcpip: computer name or IP address
		"""
		param = Conversions.value_to_quoted_str(tcpip)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:TCPip {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:RDEVice:OSCilloscope:TCPip \n
		Snippet: value: str = driver.applications.k9X11Ad.system.communicate.rdevice.oscilloscope.tcpip.get() \n
		Defines the TCPIP address or computer name of the oscilloscope connected to the FSW via LAN. Note: The IP address is
		maintained after a [PRESET], and is transferred between applications. \n
			:return: tcpip: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:OSCilloscope:TCPip?')
		return trim_str_response(response)
