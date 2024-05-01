from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SingleCls:
	"""Single commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("single", core, parent)

	@property
	def coupled(self):
		"""coupled commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coupled'):
			from .Coupled import CoupledCls
			self._coupled = CoupledCls(self._core, self._cmd_group)
		return self._coupled

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:FREQuency:SINGle \n
		Snippet: driver.applications.k30NoiseFigure.sense.frequency.single.set(frequency = 1.0) \n
		Defines the frequency for single frequency measurements. \n
			:param frequency: The minimum and maximum frequency depend on the hardware. Refer to the datasheet for details. Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:FREQuency:SINGle {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:FREQuency:SINGle \n
		Snippet: value: float = driver.applications.k30NoiseFigure.sense.frequency.single.get() \n
		Defines the frequency for single frequency measurements. \n
			:return: frequency: The minimum and maximum frequency depend on the hardware. Refer to the datasheet for details. Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:FREQuency:SINGle?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SingleCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SingleCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
