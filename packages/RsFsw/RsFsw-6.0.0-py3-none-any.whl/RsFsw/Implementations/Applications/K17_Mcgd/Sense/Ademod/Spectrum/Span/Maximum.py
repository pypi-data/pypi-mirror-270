from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN[:MAXimum] \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.spectrum.span.maximum.set(value = 1.0) \n
		Sets the DBW to the specified value and the span (around the center frequency) of the RF data to be evaluated to its new
		maximum (the demodulation bandwidth) . \n
			:param value: Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:ADEMod:SPECtrum:SPAN:MAXimum {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN[:MAXimum] \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.ademod.spectrum.span.maximum.get() \n
		Sets the DBW to the specified value and the span (around the center frequency) of the RF data to be evaluated to its new
		maximum (the demodulation bandwidth) . \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SPECtrum:SPAN:MAXimum?')
		return Conversions.str_to_float(response)
