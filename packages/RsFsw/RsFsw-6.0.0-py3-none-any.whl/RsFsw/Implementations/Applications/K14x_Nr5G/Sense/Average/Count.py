from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, average: float) -> None:
		"""SCPI: [SENSe]:AVERage:COUNt \n
		Snippet: driver.applications.k14Xnr5G.sense.average.count.set(average = 1.0) \n
		Defines the number of sweeps that the application uses to average traces. In case of continuous sweep mode,
		the application calculates the moving average over the average count. In case of single sweep mode, the application stops
		the measurement and calculates the average after the average count has been reached. \n
			:param average: No help available
		"""
		param = Conversions.decimal_value_to_str(average)
		self._core.io.write(f'SENSe:AVERage:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:AVERage:COUNt \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.average.count.get() \n
		Defines the number of sweeps that the application uses to average traces. In case of continuous sweep mode,
		the application calculates the moving average over the average count. In case of single sweep mode, the application stops
		the measurement and calculates the average after the average count has been reached. \n
			:return: average: No help available"""
		response = self._core.io.query_str(f'SENSe:AVERage:COUNt?')
		return Conversions.str_to_float(response)
