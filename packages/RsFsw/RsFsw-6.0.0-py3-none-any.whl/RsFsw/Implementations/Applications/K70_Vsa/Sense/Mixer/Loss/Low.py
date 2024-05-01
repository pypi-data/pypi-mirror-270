from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowCls:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def set(self, average: float) -> None:
		"""SCPI: [SENSe]:MIXer:LOSS[:LOW] \n
		Snippet: driver.applications.k70Vsa.sense.mixer.loss.low.set(average = 1.0) \n
		Defines the average conversion loss to be used for the entire low (first) range. \n
			:param average: Range: 0 to 100, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(average)
		self._core.io.write(f'SENSe:MIXer:LOSS:LOW {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:LOSS[:LOW] \n
		Snippet: value: float = driver.applications.k70Vsa.sense.mixer.loss.low.get() \n
		Defines the average conversion loss to be used for the entire low (first) range. \n
			:return: average: Range: 0 to 100, Unit: dB"""
		response = self._core.io.query_str(f'SENSe:MIXer:LOSS:LOW?')
		return Conversions.str_to_float(response)
