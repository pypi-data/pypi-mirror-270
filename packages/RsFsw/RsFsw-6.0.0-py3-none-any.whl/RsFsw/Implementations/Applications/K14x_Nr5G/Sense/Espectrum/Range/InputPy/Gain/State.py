from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:INPut:GAIN:STATe \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.range.inputPy.gain.state.set(state = False, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Turns the preamplifier for a SEM range on and off. In case of high speed measurements, the state of the preamplifier has
		to be identical for all ranges. \n
			:param state: ON | OFF | 1 | 0
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.bool_to_str(state)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:INPut:GAIN:STATe {param}')

	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> bool:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:INPut:GAIN:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.espectrum.range.inputPy.gain.state.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Turns the preamplifier for a SEM range on and off. In case of high speed measurements, the state of the preamplifier has
		to be identical for all ranges. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: state: ON | OFF | 1 | 0"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:INPut:GAIN:STATe?')
		return Conversions.str_to_bool(response)
