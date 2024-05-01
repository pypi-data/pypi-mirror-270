from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlphaCls:
	"""Alpha commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alpha", core, parent)

	def set(self, alpha: float, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:FILTer[:RRC]:ALPHa \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.filterPy.rrc.alpha.set(alpha = 1.0, subBlock = repcap.SubBlock.Default) \n
		Defines the roll-off factor for the RRC filter. The RRC filter is available if the power reference is the channel power. \n
			:param alpha: Range: 0 to 1
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(alpha)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:FILTer:RRC:ALPHa {param}')

	def get(self, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:FILTer[:RRC]:ALPHa \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.espectrum.filterPy.rrc.alpha.get(subBlock = repcap.SubBlock.Default) \n
		Defines the roll-off factor for the RRC filter. The RRC filter is available if the power reference is the channel power. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: alpha: Range: 0 to 1"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:FILTer:RRC:ALPHa?')
		return Conversions.str_to_float(response)
