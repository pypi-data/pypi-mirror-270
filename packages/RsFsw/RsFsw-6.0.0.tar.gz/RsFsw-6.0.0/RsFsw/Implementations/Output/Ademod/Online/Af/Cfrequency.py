from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CfrequencyCls:
	"""Cfrequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfrequency", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: OUTPut:ADEMod[:ONLine]:AF[:CFRequency] \n
		Snippet: driver.output.ademod.online.af.cfrequency.set(frequency = 1.0) \n
		Defines the cutoff frequency for the AC highpass filter (for AC coupling only, see [SENSe:]ADEMod<n>:AF:COUPling) . \n
			:param frequency: numeric value Range: 10 Hz to DemodBW/10 (= 300 kHz for active demodulation output) , Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'OUTPut:ADEMod:ONLine:AF:CFRequency {param}')

	def get(self) -> float:
		"""SCPI: OUTPut:ADEMod[:ONLine]:AF[:CFRequency] \n
		Snippet: value: float = driver.output.ademod.online.af.cfrequency.get() \n
		Defines the cutoff frequency for the AC highpass filter (for AC coupling only, see [SENSe:]ADEMod<n>:AF:COUPling) . \n
			:return: frequency: numeric value Range: 10 Hz to DemodBW/10 (= 300 kHz for active demodulation output) , Unit: HZ"""
		response = self._core.io.query_str(f'OUTPut:ADEMod:ONLine:AF:CFRequency?')
		return Conversions.str_to_float(response)
