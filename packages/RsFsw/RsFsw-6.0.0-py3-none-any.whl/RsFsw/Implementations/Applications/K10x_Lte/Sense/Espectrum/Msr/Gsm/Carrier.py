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

	def set(self, power: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:GSM:CARRier \n
		Snippet: driver.applications.k10Xlte.sense.espectrum.msr.gsm.carrier.set(power = 1.0, subBlock = repcap.SubBlock.Default) \n
		Defines the power of the GSM carrier (if available, see [SENSe:]ESPectrum<sb>:MSR:GSM:CPResent) . Is only available for
		band category 2 (see [SENSe:]ESPectrum<sb>:MSR:BCATegory) . \n
			:param power: Range: 0 dBm to 100 dBm, Unit: dBm
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(power)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:GSM:CARRier {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:GSM:CARRier \n
		Snippet: value: float = driver.applications.k10Xlte.sense.espectrum.msr.gsm.carrier.get(subBlock = repcap.SubBlock.Default) \n
		Defines the power of the GSM carrier (if available, see [SENSe:]ESPectrum<sb>:MSR:GSM:CPResent) . Is only available for
		band category 2 (see [SENSe:]ESPectrum<sb>:MSR:BCATegory) . \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: power: Range: 0 dBm to 100 dBm, Unit: dBm"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:GSM:CARRier?')
		return Conversions.str_to_float(response)
