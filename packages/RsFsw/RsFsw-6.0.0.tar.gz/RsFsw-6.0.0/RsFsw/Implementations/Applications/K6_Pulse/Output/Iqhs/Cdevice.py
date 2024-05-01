from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CdeviceCls:
	"""Cdevice commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cdevice", core, parent)

	def get(self, outputConnector=repcap.OutputConnector.Default) -> str:
		"""SCPI: OUTPut<up>:IQHS:CDEVice \n
		Snippet: value: str = driver.applications.k6Pulse.output.iqhs.cdevice.get(outputConnector = repcap.OutputConnector.Default) \n
		Returns a comma-separated list of information on the instrument connected to the QSFP+ connector, if available.
		For details on Digital I/Q 40G Streaming Output (FSW-B517/-B1017) , see 'Digital I/Q 40G Streaming Output'. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: iq_device_info: No help available"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:IQHS:CDEVice?')
		return trim_str_response(response)
