from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, carrier: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:CARRier:SELect \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.cc.carrier.select.set(carrier = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		Filters the displayed results in the constellation diagram by a certain subcarrier. \n
			:param carrier: ALL Shows the results for all subcarriers. numeric value (integer only) Shows the results for a single subcarrier.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(carrier)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:CARRier:SELect {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:CARRier:SELect \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.cc.carrier.select.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Filters the displayed results in the constellation diagram by a certain subcarrier. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: carrier: ALL Shows the results for all subcarriers. numeric value (integer only) Shows the results for a single subcarrier."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:CARRier:SELect?')
		return Conversions.str_to_float(response)
