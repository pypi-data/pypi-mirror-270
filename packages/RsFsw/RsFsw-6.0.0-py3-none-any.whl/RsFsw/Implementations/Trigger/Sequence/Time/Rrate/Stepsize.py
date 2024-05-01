from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StepsizeCls:
	"""Stepsize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stepsize", core, parent)

	def set(self, rate: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:TIME:RRATe:STEPsize \n
		Snippet: driver.trigger.sequence.time.rrate.stepsize.set(rate = 1.0) \n
		No command help available \n
			:param rate: No help available
		"""
		param = Conversions.decimal_value_to_str(rate)
		self._core.io.write(f'TRIGger:SEQuence:TIME:RRATe:STEPsize {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:TIME:RRATe:STEPsize \n
		Snippet: value: float = driver.trigger.sequence.time.rrate.stepsize.get() \n
		No command help available \n
			:return: rate: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:TIME:RRATe:STEPsize?')
		return Conversions.str_to_float(response)
