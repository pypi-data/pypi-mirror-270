from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CenterCls:
	"""Center commands group definition. 4 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	@property
	def step(self):
		"""step commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_step'):
			from .Step import StepCls
			self._step = StepCls(self._core, self._cmd_group)
		return self._step

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer \n
		Snippet: driver.applications.k17Mcgd.sense.frequency.center.set(frequency = 1.0) \n
		Defines the center frequency. \n
			:param frequency: For the allowed range and fmax, refer to the specifications document. UP Increases the center frequency by the step defined using the [SENSe:]FREQuency:CENTer:STEP command. DOWN Decreases the center frequency by the step defined using the [SENSe:]FREQuency:CENTer:STEP command. Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:CENTer {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.frequency.center.get() \n
		Defines the center frequency. \n
			:return: frequency: For the allowed range and fmax, refer to the specifications document. UP Increases the center frequency by the step defined using the [SENSe:]FREQuency:CENTer:STEP command. DOWN Decreases the center frequency by the step defined using the [SENSe:]FREQuency:CENTer:STEP command. Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'CenterCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CenterCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
