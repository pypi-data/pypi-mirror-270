from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DtimeCls:
	"""Dtime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtime", core, parent)

	def set(self, time: float, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:DTIMe \n
		Snippet: driver.applications.k10Xlte.sense.pmeter.trigger.dtime.set(time = 1.0, powerMeter = repcap.PowerMeter.Default) \n
		Defines the time period that the input signal has to stay below the IF power trigger level before the measurement starts. \n
			:param time: Range: 0 s to 1 s, Unit: S
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.decimal_value_to_str(time)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:DTIMe {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:DTIMe \n
		Snippet: value: float = driver.applications.k10Xlte.sense.pmeter.trigger.dtime.get(powerMeter = repcap.PowerMeter.Default) \n
		Defines the time period that the input signal has to stay below the IF power trigger level before the measurement starts. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: time: Range: 0 s to 1 s, Unit: S"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:DTIMe?')
		return Conversions.str_to_float(response)
