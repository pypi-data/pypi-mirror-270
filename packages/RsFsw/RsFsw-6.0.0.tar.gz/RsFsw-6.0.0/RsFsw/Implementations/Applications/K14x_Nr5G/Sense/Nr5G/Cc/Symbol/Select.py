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

	def set(self, symbol: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:SYMBol:SELect \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.cc.symbol.select.set(symbol = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		Filters the displayed results in the constellation diagram by a certain OFDM symbol. \n
			:param symbol: ALL Shows the results for all symbols. numeric value (integer only) Shows the results for a single OFDM symbol.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(symbol)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:SYMBol:SELect {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:SYMBol:SELect \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.cc.symbol.select.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Filters the displayed results in the constellation diagram by a certain OFDM symbol. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: symbol: ALL Shows the results for all symbols. numeric value (integer only) Shows the results for a single OFDM symbol."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:SYMBol:SELect?')
		return Conversions.str_to_float(response)
