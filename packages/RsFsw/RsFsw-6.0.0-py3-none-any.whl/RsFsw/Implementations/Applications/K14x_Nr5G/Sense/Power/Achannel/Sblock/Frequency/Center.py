from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CenterCls:
	"""Center commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	def set(self, frequency: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:FREQuency:CENTer \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.sblock.frequency.center.set(frequency = 1.0, subBlock = repcap.SubBlock.Default) \n
		Defines the center of the specified MSR sub block. Note that the position of the sub block also affects the position of
		the adjacent gap (CACLR) channels. Is for MSR signals only (see method RsFsw.Calculate.Marker.Function.Power.preset) .
		For details on MSR signals see 'Measurement on multi-standard radio (MSR) signals'. \n
			:param frequency: absolute frequency in Hz Unit: Hz
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:FREQuency:CENTer {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:FREQuency:CENTer \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.achannel.sblock.frequency.center.get(subBlock = repcap.SubBlock.Default) \n
		Defines the center of the specified MSR sub block. Note that the position of the sub block also affects the position of
		the adjacent gap (CACLR) channels. Is for MSR signals only (see method RsFsw.Calculate.Marker.Function.Power.preset) .
		For details on MSR signals see 'Measurement on multi-standard radio (MSR) signals'. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
			:return: frequency: absolute frequency in Hz Unit: Hz"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:FREQuency:CENTer?')
		return Conversions.str_to_float(response)
