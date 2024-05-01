from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfPowerCls:
	"""IfPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifPower", core, parent)

	def set(self, level: float, instrument=repcap.Instrument.Default) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel<ant>:IFPower \n
		Snippet: driver.applications.k10Xlte.trigger.sequence.level.ifPower.set(level = 1.0, instrument = repcap.Instrument.Default) \n
		Defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event. Note that any
		RF attenuation or preamplification is considered when the trigger level is analyzed. If defined, a reference level offset
		is also considered. \n
			:param level: numeric value For details on available trigger levels and trigger bandwidths see the specifications document. Unit: dBm
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Level')
		"""
		param = Conversions.decimal_value_to_str(level)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		self._core.io.write(f'TRIGger:SEQuence:LEVel{instrument_cmd_val}:IFPower {param}')

	def get(self, instrument=repcap.Instrument.Default) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel<ant>:IFPower \n
		Snippet: value: float = driver.applications.k10Xlte.trigger.sequence.level.ifPower.get(instrument = repcap.Instrument.Default) \n
		Defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event. Note that any
		RF attenuation or preamplification is considered when the trigger level is analyzed. If defined, a reference level offset
		is also considered. \n
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Level')
			:return: level: numeric value For details on available trigger levels and trigger bandwidths see the specifications document. Unit: dBm"""
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel{instrument_cmd_val}:IFPower?')
		return Conversions.str_to_float(response)
