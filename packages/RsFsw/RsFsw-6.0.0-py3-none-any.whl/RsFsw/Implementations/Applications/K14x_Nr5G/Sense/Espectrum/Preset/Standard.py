from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardCls:
	"""Standard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	def set(self, standard: enums.SelectNone, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet[:STANdard] \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.preset.standard.set(standard = enums.SelectNone.NONE, subBlock = repcap.SubBlock.Default) \n
		Loads a measurement configuration. Standard definitions are stored in an xml file. The default directory for SEM
		standards is C:/R_S/INSTR/sem_std. \n
			:param standard: (enum or string) String containing the file name. If you have stored the file in a subdirectory of the directory mentioned above, you have to include the relative path to the file.
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.enum_ext_scalar_to_str(standard, enums.SelectNone)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:STANdard {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default) -> enums.SelectNone:
		"""SCPI: [SENSe]:ESPectrum<sb>:PRESet[:STANdard] \n
		Snippet: value: enums.SelectNone = driver.applications.k14Xnr5G.sense.espectrum.preset.standard.get(subBlock = repcap.SubBlock.Default) \n
		Loads a measurement configuration. Standard definitions are stored in an xml file. The default directory for SEM
		standards is C:/R_S/INSTR/sem_std. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: standard: (enum or string) String containing the file name. If you have stored the file in a subdirectory of the directory mentioned above, you have to include the relative path to the file."""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:PRESet:STANdard?')
		return Conversions.str_to_scalar_enum_ext(response, enums.SelectNone)
