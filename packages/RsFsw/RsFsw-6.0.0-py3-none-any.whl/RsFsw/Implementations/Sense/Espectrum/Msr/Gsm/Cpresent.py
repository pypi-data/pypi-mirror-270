from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CpresentCls:
	"""Cpresent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cpresent", core, parent)

	def set(self, state: bool, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:GSM:CPResent \n
		Snippet: driver.sense.espectrum.msr.gsm.cpresent.set(state = False, subBlock = repcap.SubBlock.Default) \n
		Defines whether a GSM/Edge carrier is located at the edge of the specified RF bandwidth. In this case, the specification
		demands specific limits for the SEM ranges.
		Is only available for band category 2 (see [SENSe:]ESPectrum<sb>:MSR:BCATegory) . \n
			:param state: ON | OFF | 1 | 0
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.bool_to_str(state)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:GSM:CPResent {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> bool:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:GSM:CPResent \n
		Snippet: value: bool = driver.sense.espectrum.msr.gsm.cpresent.get(subBlock = repcap.SubBlock.Default) \n
		Defines whether a GSM/Edge carrier is located at the edge of the specified RF bandwidth. In this case, the specification
		demands specific limits for the SEM ranges.
		Is only available for band category 2 (see [SENSe:]ESPectrum<sb>:MSR:BCATegory) . \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: state: ON | OFF | 1 | 0"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:GSM:CPResent?')
		return Conversions.str_to_bool(response)
