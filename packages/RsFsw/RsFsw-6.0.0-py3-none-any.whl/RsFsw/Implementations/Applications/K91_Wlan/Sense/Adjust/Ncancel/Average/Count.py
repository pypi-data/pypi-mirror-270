from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: float) -> None:
		"""SCPI: [SENSe]:ADJust:NCANcel:AVERage[:COUNt] \n
		Snippet: driver.applications.k91Wlan.sense.adjust.ncancel.average.count.set(count = 1.0) \n
		Defines the number of measurements that are performed on the captured I/Q data to determine the average noise density due
		to the spectrum analyzer. Only available if I/Q noise cancellation is enabled ([SENSe:]ADJust:NCANcel:AVERage[:STATe] ON)
		. \n
			:param count: integer Number of measurements
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:ADJust:NCANcel:AVERage:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADJust:NCANcel:AVERage[:COUNt] \n
		Snippet: value: float = driver.applications.k91Wlan.sense.adjust.ncancel.average.count.get() \n
		Defines the number of measurements that are performed on the captured I/Q data to determine the average noise density due
		to the spectrum analyzer. Only available if I/Q noise cancellation is enabled ([SENSe:]ADJust:NCANcel:AVERage[:STATe] ON)
		. \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'SENSe:ADJust:NCANcel:AVERage:COUNt?')
		return Conversions.str_to_float(response)
