from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrNumberCls:
	"""SrNumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srNumber", core, parent)

	def get(self, serial_no: str, probe=repcap.Probe.Default) -> str:
		"""SCPI: [SENSe]:PROBe<pb>:ID:SRNumber \n
		Snippet: value: str = driver.applications.k91Wlan.sense.probe.id.srNumber.get(serial_no = 'abc', probe = repcap.Probe.Default) \n
		Queries the serial number of the probe. \n
			:param serial_no: No help available
			:param probe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Probe')
			:return: result: 1..n Selects the connector: 1 = Baseband Input I 2 = Baseband Input Q 3 = RF"""
		param = Conversions.value_to_quoted_str(serial_no)
		probe_cmd_val = self._cmd_group.get_repcap_cmd_value(probe, repcap.Probe)
		response = self._core.io.query_str(f'SENSe:PROBe{probe_cmd_val}:ID:SRNumber? {param}')
		return trim_str_response(response)
