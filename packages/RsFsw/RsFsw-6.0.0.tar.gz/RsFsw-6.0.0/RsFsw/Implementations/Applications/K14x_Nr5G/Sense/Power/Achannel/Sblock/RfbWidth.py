from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfbWidthCls:
	"""RfbWidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfbWidth", core, parent)

	def set(self, bandwidth: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:RFBWidth \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.sblock.rfbWidth.set(bandwidth = 1.0, subBlock = repcap.SubBlock.Default) \n
		Defines the bandwidth of the individual MSR sub block. Note that sub block ranges also affect the position of the
		adjacent gap channels (CACLR) . Is for MSR signals only (see method RsFsw.Calculate.Marker.Function.Power.preset) . For
		details on MSR signals see 'Measurement on multi-standard radio (MSR) signals'. \n
			:param bandwidth: Bandwidth in Hz Unit: Hz
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:RFBWidth {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:RFBWidth \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.achannel.sblock.rfbWidth.get(subBlock = repcap.SubBlock.Default) \n
		Defines the bandwidth of the individual MSR sub block. Note that sub block ranges also affect the position of the
		adjacent gap channels (CACLR) . Is for MSR signals only (see method RsFsw.Calculate.Marker.Function.Power.preset) . For
		details on MSR signals see 'Measurement on multi-standard radio (MSR) signals'. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
			:return: bandwidth: Bandwidth in Hz Unit: Hz"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:RFBWidth?')
		return Conversions.str_to_float(response)
