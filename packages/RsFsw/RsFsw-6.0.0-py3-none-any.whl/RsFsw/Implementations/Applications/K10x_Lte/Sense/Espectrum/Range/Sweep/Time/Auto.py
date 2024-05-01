from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:SWEep:TIME:AUTO \n
		Snippet: driver.applications.k10Xlte.sense.espectrum.range.sweep.time.auto.set(state = False, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Turns automatic selection of the sweep time for a SEM range on and off. In case of high speed measurements, the sweep
		time has to be identical for all ranges. \n
			:param state: ON | OFF | 0 | 1
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.bool_to_str(state)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:SWEep:TIME:AUTO {param}')

	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> bool:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:SWEep:TIME:AUTO \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.espectrum.range.sweep.time.auto.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Turns automatic selection of the sweep time for a SEM range on and off. In case of high speed measurements, the sweep
		time has to be identical for all ranges. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: state: ON | OFF | 0 | 1"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:SWEep:TIME:AUTO?')
		return Conversions.str_to_bool(response)
