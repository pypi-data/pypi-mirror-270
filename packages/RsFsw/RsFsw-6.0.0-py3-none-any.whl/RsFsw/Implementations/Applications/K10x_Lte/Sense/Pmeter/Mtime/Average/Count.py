from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, number_readings: float, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:MTIMe:AVERage:COUNt \n
		Snippet: driver.applications.k10Xlte.sense.pmeter.mtime.average.count.set(number_readings = 1.0, powerMeter = repcap.PowerMeter.Default) \n
		Sets the number of power readings included in the averaging process of power sensor measurements. Extended averaging
		yields more stable results for power sensor measurements, especially for measurements on signals with a low power,
		because it minimizes the effects of noise. \n
			:param number_readings: An average count of 0 or 1 performs one power reading. Range: 0 to 256
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.decimal_value_to_str(number_readings)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:MTIMe:AVERage:COUNt {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: [SENSe]:PMETer<p>:MTIMe:AVERage:COUNt \n
		Snippet: value: float = driver.applications.k10Xlte.sense.pmeter.mtime.average.count.get(powerMeter = repcap.PowerMeter.Default) \n
		Sets the number of power readings included in the averaging process of power sensor measurements. Extended averaging
		yields more stable results for power sensor measurements, especially for measurements on signals with a low power,
		because it minimizes the effects of noise. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: number_readings: An average count of 0 or 1 performs one power reading. Range: 0 to 256"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:MTIMe:AVERage:COUNt?')
		return Conversions.str_to_float(response)
