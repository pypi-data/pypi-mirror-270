from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StartCls:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, frequency: float, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:FREQuency:STARt \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.range.frequency.start.set(frequency = 1.0, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Defines the start frequency of a SEM range. Make sure to set an appropriate span. If you set a span that is
			INTRO_CMD_HELP: Prerequisites for this command \n
			- smaller than the span the SEM sweep list covers, the FSW will not measure the ranges that are outside the span - results may be invalid.
			- greater than the span the SEM sweep list covers, the FSW will adjust the start frequency of the first SEM range and the stop frequency of the last SEM range to the span
		For more information see 'Ranges and range settings'. \n
			:param frequency: Numeric value. Note that the minimum frequency range of a SEM range is 20 Hz. Unit: Hz
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:FREQuency:STARt {param}')

	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> float:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:FREQuency:STARt \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.espectrum.range.frequency.start.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Defines the start frequency of a SEM range. Make sure to set an appropriate span. If you set a span that is
			INTRO_CMD_HELP: Prerequisites for this command \n
			- smaller than the span the SEM sweep list covers, the FSW will not measure the ranges that are outside the span - results may be invalid.
			- greater than the span the SEM sweep list covers, the FSW will adjust the start frequency of the first SEM range and the stop frequency of the last SEM range to the span
		For more information see 'Ranges and range settings'. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: frequency: Numeric value. Note that the minimum frequency range of a SEM range is 20 Hz. Unit: Hz"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:FREQuency:STARt?')
		return Conversions.str_to_float(response)
