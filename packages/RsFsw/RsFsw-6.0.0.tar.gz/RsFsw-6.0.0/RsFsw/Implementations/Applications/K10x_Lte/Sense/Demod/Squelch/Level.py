from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: [SENSe]:DEMod:SQUelch:LEVel \n
		Snippet: driver.applications.k10Xlte.sense.demod.squelch.level.set(level = 1.0) \n
		Defines the threshold for selective demodulation. All signals below the threshold are not demodulated. \n
			:param level: Percentage of the display height. Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:DEMod:SQUelch:LEVel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:SQUelch:LEVel \n
		Snippet: value: float = driver.applications.k10Xlte.sense.demod.squelch.level.get() \n
		Defines the threshold for selective demodulation. All signals below the threshold are not demodulated. \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'SENSe:DEMod:SQUelch:LEVel?')
		return Conversions.str_to_float(response)
