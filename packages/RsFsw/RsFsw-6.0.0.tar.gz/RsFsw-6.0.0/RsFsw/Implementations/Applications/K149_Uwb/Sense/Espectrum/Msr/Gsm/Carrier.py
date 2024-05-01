from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CarrierCls:
	"""Carrier commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("carrier", core, parent)

	def set(self, min_py: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:GSM:CARRier \n
		Snippet: driver.applications.k149Uwb.sense.espectrum.msr.gsm.carrier.set(min_py = 1.0, subBlock = repcap.SubBlock.Default) \n
		Defines the power of the GSM carrier (if available, see [SENSe:]ESPectrum<sb>:MSR:GSM:CPResent) . Is only available for
		band category 2 (see [SENSe:]ESPectrum<sb>:MSR:BCATegory) . \n
			:param min_py: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(min_py)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:GSM:CARRier {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:GSM:CARRier \n
		Snippet: value: float = driver.applications.k149Uwb.sense.espectrum.msr.gsm.carrier.get(subBlock = repcap.SubBlock.Default) \n
		Defines the power of the GSM carrier (if available, see [SENSe:]ESPectrum<sb>:MSR:GSM:CPResent) . Is only available for
		band category 2 (see [SENSe:]ESPectrum<sb>:MSR:BCATegory) . \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: min_py: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:GSM:CARRier?')
		return Conversions.str_to_float(response)
