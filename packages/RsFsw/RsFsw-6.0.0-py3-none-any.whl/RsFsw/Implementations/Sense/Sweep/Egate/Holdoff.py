from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HoldoffCls:
	"""Holdoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("holdoff", core, parent)

	def set(self, delay_time: float) -> None:
		"""SCPI: [SENSe]:SWEep:EGATe:HOLDoff \n
		Snippet: driver.sense.sweep.egate.holdoff.set(delay_time = 1.0) \n
		Defines the delay time between the gate signal and the continuation of the measurement. Note: If you perform gated
		measurements in combination with the IF Power trigger, the FSW ignores the holding time for frequency sweep, FFT sweep,
		zero span and I/Q mode measurements. \n
			:param delay_time: Range: 0 s to 30 s, Unit: S
		"""
		param = Conversions.decimal_value_to_str(delay_time)
		self._core.io.write(f'SENSe:SWEep:EGATe:HOLDoff {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:EGATe:HOLDoff \n
		Snippet: value: float = driver.sense.sweep.egate.holdoff.get() \n
		Defines the delay time between the gate signal and the continuation of the measurement. Note: If you perform gated
		measurements in combination with the IF Power trigger, the FSW ignores the holding time for frequency sweep, FFT sweep,
		zero span and I/Q mode measurements. \n
			:return: delay_time: Range: 0 s to 30 s, Unit: S"""
		response = self._core.io.query_str(f'SENSe:SWEep:EGATe:HOLDoff?')
		return Conversions.str_to_float(response)
