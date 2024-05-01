from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfbWidthCls:
	"""RfbWidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfbWidth", core, parent)

	def set(self, bandwidth: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:RFBWidth \n
		Snippet: driver.sense.espectrum.msr.rfbWidth.set(bandwidth = 1.0, subBlock = repcap.SubBlock.Default) \n
		Defines the RF bandwidth of the base station for MSR measurements. \n
			:param bandwidth: Bandwidth in Hz Unit: Hz
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:RFBWidth {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:RFBWidth \n
		Snippet: value: float = driver.sense.espectrum.msr.rfbWidth.get(subBlock = repcap.SubBlock.Default) \n
		Defines the RF bandwidth of the base station for MSR measurements. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: bandwidth: Bandwidth in Hz Unit: Hz"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:RFBWidth?')
		return Conversions.str_to_float(response)
