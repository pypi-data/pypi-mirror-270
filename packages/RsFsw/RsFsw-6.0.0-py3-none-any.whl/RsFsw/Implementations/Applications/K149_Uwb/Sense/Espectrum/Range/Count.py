from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> int:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:COUNt \n
		Snippet: value: int = driver.applications.k149Uwb.sense.espectrum.range.count.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Queries the number of ranges in the sweep list. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: result: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:COUNt?')
		return Conversions.str_to_int(response)
