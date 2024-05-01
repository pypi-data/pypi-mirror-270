from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffsetCls:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:OFFSet \n
		Snippet: driver.applications.k149Uwb.sense.frequency.offset.set(frequency = 1.0) \n
		Defines a frequency offset. If this value is not 0 Hz, the application assumes that the input signal was frequency
		shifted outside the application. All results of type 'frequency' will be corrected for this shift numerically by the
		application. See also 'Frequency Offset'. Note: In MSRA mode, the setting command is only available for the MSRA primary
		application. For MSRA secondary applications, only the query command is available. \n
			:param frequency: Range: -1 THz to 1 THz, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:OFFSet \n
		Snippet: value: float = driver.applications.k149Uwb.sense.frequency.offset.get() \n
		Defines a frequency offset. If this value is not 0 Hz, the application assumes that the input signal was frequency
		shifted outside the application. All results of type 'frequency' will be corrected for this shift numerically by the
		application. See also 'Frequency Offset'. Note: In MSRA mode, the setting command is only available for the MSRA primary
		application. For MSRA secondary applications, only the query command is available. \n
			:return: frequency: No help available"""
		response = self._core.io.query_str(f'SENSe:FREQuency:OFFSet?')
		return Conversions.str_to_float(response)
