from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StepCls:
	"""Step commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	def set(self, stepsize: float) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP \n
		Snippet: driver.applications.k60Transient.sense.frequency.center.step.set(stepsize = 1.0) \n
		Defines the center frequency step size. You can increase or decrease the center frequency quickly in fixed steps using
		the SENS:FREQ UP AND SENS:FREQ DOWN commands, see [SENSe:]FREQuency:CENTer. \n
			:param stepsize: For fmax, refer to the specifications document. Range: 1 to fMAX, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(stepsize)
		self._core.io.write(f'SENSe:FREQuency:CENTer:STEP {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer:STEP \n
		Snippet: value: float = driver.applications.k60Transient.sense.frequency.center.step.get() \n
		Defines the center frequency step size. You can increase or decrease the center frequency quickly in fixed steps using
		the SENS:FREQ UP AND SENS:FREQ DOWN commands, see [SENSe:]FREQuency:CENTer. \n
			:return: stepsize: For fmax, refer to the specifications document. Range: 1 to fMAX, Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:STEP?')
		return Conversions.str_to_float(response)
