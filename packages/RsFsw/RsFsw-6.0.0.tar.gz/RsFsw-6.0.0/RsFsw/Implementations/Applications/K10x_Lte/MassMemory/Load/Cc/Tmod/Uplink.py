from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	def set(self, test_model: str, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: MMEMory:LOAD[:CC<cc>]:TMOD:UL \n
		Snippet: driver.applications.k10Xlte.massMemory.load.cc.tmod.uplink.set(test_model = 'abc', carrierComponent = repcap.CarrierComponent.Default) \n
		Loads an O-RAN test case. \n
			:param test_model: string String that contains the name of the O-RAN test case, e.g. 'TC 3.2.3.7.1'.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.value_to_quoted_str(test_model)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'MMEMory:LOAD:CC{carrierComponent_cmd_val}:TMOD:UL {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> str:
		"""SCPI: MMEMory:LOAD[:CC<cc>]:TMOD:UL \n
		Snippet: value: str = driver.applications.k10Xlte.massMemory.load.cc.tmod.uplink.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Loads an O-RAN test case. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: test_model: string String that contains the name of the O-RAN test case, e.g. 'TC 3.2.3.7.1'."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'MMEMory:LOAD:CC{carrierComponent_cmd_val}:TMOD:UL?')
		return trim_str_response(response)
