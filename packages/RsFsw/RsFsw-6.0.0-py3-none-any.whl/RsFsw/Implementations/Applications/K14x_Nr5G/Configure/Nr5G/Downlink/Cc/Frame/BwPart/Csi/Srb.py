from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrbCls:
	"""Srb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srb", core, parent)

	def set(self, resource_block: float, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, csiRs=repcap.CsiRs.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:CSI<csi>:SRB \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.csi.srb.set(resource_block = 1.0, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, csiRs = repcap.CsiRs.Default) \n
		Select the first resource block occupied by the CSI reference signal. \n
			:param resource_block: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param csiRs: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csi')
		"""
		param = Conversions.decimal_value_to_str(resource_block)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		csiRs_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRs, repcap.CsiRs)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:CSI{csiRs_cmd_val}:SRB {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, csiRs=repcap.CsiRs.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:CSI<csi>:SRB \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.csi.srb.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, csiRs = repcap.CsiRs.Default) \n
		Select the first resource block occupied by the CSI reference signal. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param csiRs: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csi')
			:return: resource_block: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		csiRs_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRs, repcap.CsiRs)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:CSI{csiRs_cmd_val}:SRB?')
		return Conversions.str_to_float(response)
