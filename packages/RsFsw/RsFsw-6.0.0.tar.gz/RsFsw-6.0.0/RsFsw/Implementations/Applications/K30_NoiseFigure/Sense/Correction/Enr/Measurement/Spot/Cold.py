from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ColdCls:
	"""Cold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cold", core, parent)

	def set(self, temperature: float) -> None:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:SPOT:COLD \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.enr.measurement.spot.cold.set(temperature = 1.0) \n
		Defines a constant temperature of a resistor not supplied with power (Tcold) used during measurements. The command is
		available when you have selected a noise source with resistor characteristics with
		[SENSe:]CORRection:ENR[:MEASurement]:TYPE. \n
			:param temperature: Temperature in degrees Kelvin. Unit: K
		"""
		param = Conversions.decimal_value_to_str(temperature)
		self._core.io.write(f'SENSe:CORRection:ENR:MEASurement:SPOT:COLD {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:SPOT:COLD \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.correction.enr.measurement.spot.cold.get() \n
		Defines a constant temperature of a resistor not supplied with power (Tcold) used during measurements. The command is
		available when you have selected a noise source with resistor characteristics with
		[SENSe:]CORRection:ENR[:MEASurement]:TYPE. \n
			:return: temperature: Temperature in degrees Kelvin. Unit: K"""
		response = self._core.io.query_str(f'SENSe:CORRection:ENR:MEASurement:SPOT:COLD?')
		return Conversions.str_to_float(response)
