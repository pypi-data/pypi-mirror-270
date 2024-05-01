from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SciCls:
	"""Sci commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sci", core, parent)

	def set(self, configuration: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:CSIRs:SCI \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.csirs.sci.set(configuration = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		Defines the subframe configuration for the CSI reference signal. \n
			:param configuration: Number that selects the subframe configuration. Range: 0 to 154
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(configuration)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:CSIRs:SCI {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:CSIRs:SCI \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.csirs.sci.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Defines the subframe configuration for the CSI reference signal. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: configuration: Number that selects the subframe configuration. Range: 0 to 154"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:CSIRs:SCI?')
		return Conversions.str_to_float(response)
