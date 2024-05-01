from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HfIndicatorCls:
	"""HfIndicator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hfIndicator", core, parent)

	def set(self, indicator: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PRACh:HFINdicator \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.prach.hfIndicator.set(indicator = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		Defines the PRACH half frame indicator. \n
			:param indicator: numeric value Unit: dB
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(indicator)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PRACh:HFINdicator {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PRACh:HFINdicator \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.prach.hfIndicator.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Defines the PRACH half frame indicator. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: indicator: numeric value Unit: dB"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PRACh:HFINdicator?')
		return Conversions.str_to_float(response)
