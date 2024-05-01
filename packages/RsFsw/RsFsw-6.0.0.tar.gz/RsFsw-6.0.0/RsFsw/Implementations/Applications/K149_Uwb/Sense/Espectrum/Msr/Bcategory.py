from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BcategoryCls:
	"""Bcategory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bcategory", core, parent)

	def set(self, count: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:BCATegory \n
		Snippet: driver.applications.k149Uwb.sense.espectrum.msr.bcategory.set(count = 1.0, subBlock = repcap.SubBlock.Default) \n
		Defines the band category for MSR measurements, i.e. the combination of available carriers to measure. \n
			:param count: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(count)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:BCATegory {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:MSR:BCATegory \n
		Snippet: value: float = driver.applications.k149Uwb.sense.espectrum.msr.bcategory.get(subBlock = repcap.SubBlock.Default) \n
		Defines the band category for MSR measurements, i.e. the combination of available carriers to measure. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: count: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:MSR:BCATegory?')
		return Conversions.str_to_float(response)
