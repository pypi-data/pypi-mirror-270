from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: float) -> None:
		"""SCPI: [SENSe]:EVALuation:STATistics:COUNt \n
		Snippet: driver.applications.k149Uwb.sense.evaluation.statistics.count.set(count = 1.0) \n
		Sets the number of packets to capture. \n
			:param count: numeric value
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:EVALuation:STATistics:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:EVALuation:STATistics:COUNt \n
		Snippet: value: float = driver.applications.k149Uwb.sense.evaluation.statistics.count.get() \n
		Sets the number of packets to capture. \n
			:return: count: numeric value"""
		response = self._core.io.query_str(f'SENSe:EVALuation:STATistics:COUNt?')
		return Conversions.str_to_float(response)
