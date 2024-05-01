from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MarkerCls:
	"""Marker commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("marker", core, parent)

	def set(self) -> None:
		"""SCPI: OUTPut:IQHS:MARKer \n
		Snippet: driver.output.iqhs.marker.set() \n
		Inserts marker information to the data stream during a running I/Q data output recording. Useful to mark a specific event
		during the measurement that you detect in the result window, for example. Then you can search for the marker information
		in the output data to analyze the effects at that time. For details on Digital I/Q 40G Streaming Output (FSW-B517/-B1017)
		, see 'Digital I/Q 40G Streaming Output'. \n
		"""
		self._core.io.write(f'OUTPut:IQHS:MARKer')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: OUTPut:IQHS:MARKer \n
		Snippet: driver.output.iqhs.marker.set_with_opc() \n
		Inserts marker information to the data stream during a running I/Q data output recording. Useful to mark a specific event
		during the measurement that you detect in the result window, for example. Then you can search for the marker information
		in the output data to analyze the effects at that time. For details on Digital I/Q 40G Streaming Output (FSW-B517/-B1017)
		, see 'Digital I/Q 40G Streaming Output'. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'OUTPut:IQHS:MARKer', opc_timeout_ms)
