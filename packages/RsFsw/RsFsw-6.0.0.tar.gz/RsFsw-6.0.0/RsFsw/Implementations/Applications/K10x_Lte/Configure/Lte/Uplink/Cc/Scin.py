from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScinCls:
	"""Scin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scin", core, parent)

	def set(self, offset: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SCIN \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.scin.set(offset = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param offset: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SCIN {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SCIN \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.scin.get(carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: offset: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SCIN?')
		return Conversions.str_to_float(response)
