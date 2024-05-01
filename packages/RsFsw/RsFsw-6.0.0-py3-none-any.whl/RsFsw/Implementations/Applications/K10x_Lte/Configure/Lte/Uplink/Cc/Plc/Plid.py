from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlidCls:
	"""Plid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plid", core, parent)

	def set(self, identity: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PLC:PLID \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.plc.plid.set(identity = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		Selects the physical layer identity. \n
			:param identity: 0 | 1 | 2
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(identity)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PLC:PLID {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PLC:PLID \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.plc.plid.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Selects the physical layer identity. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: identity: 0 | 1 | 2"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PLC:PLID?')
		return Conversions.str_to_float(response)
