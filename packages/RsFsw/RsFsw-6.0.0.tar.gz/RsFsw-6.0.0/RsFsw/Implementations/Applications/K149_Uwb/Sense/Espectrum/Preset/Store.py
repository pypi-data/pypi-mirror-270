from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StoreCls:
	"""Store commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)

	def set(self, table_high: str, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet:STORe \n
		Snippet: driver.applications.k149Uwb.sense.espectrum.preset.store.set(table_high = 'abc', subBlock = repcap.SubBlock.Default) \n
		Saves the current SEM measurement configuration. Standard definitions are stored in an xml file. The default directory
		for SEM standards is C:/R_S/INSTR/sem_std. \n
			:param table_high: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.value_to_quoted_str(table_high)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:STORe {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> str:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet:STORe \n
		Snippet: value: str = driver.applications.k149Uwb.sense.espectrum.preset.store.get(subBlock = repcap.SubBlock.Default) \n
		Saves the current SEM measurement configuration. Standard definitions are stored in an xml file. The default directory
		for SEM standards is C:/R_S/INSTR/sem_std. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: table_high: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:STORe?')
		return trim_str_response(response)
