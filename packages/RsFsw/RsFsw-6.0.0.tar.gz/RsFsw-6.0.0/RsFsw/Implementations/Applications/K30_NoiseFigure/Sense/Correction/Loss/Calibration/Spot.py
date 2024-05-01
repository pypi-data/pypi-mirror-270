from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpotCls:
	"""Spot commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spot", core, parent)

	def set(self, loss: float) -> None:
		"""SCPI: [SENSe]:CORRection:LOSS:CALibration:SPOT \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.loss.calibration.spot.set(loss = 1.0) \n
		Defines a constant calibration loss for all measurement points. \n
			:param loss: Range: -999.99 to 999.99, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(loss)
		self._core.io.write(f'SENSe:CORRection:LOSS:CALibration:SPOT {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:LOSS:CALibration:SPOT \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.correction.loss.calibration.spot.get() \n
		Defines a constant calibration loss for all measurement points. \n
			:return: loss: Range: -999.99 to 999.99, Unit: dB"""
		response = self._core.io.query_str(f'SENSe:CORRection:LOSS:CALibration:SPOT?')
		return Conversions.str_to_float(response)
