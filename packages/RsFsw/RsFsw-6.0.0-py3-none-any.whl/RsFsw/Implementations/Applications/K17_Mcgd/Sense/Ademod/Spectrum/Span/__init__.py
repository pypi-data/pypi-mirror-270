from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpanCls:
	"""Span commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("span", core, parent)

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def zoom(self):
		"""zoom commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zoom'):
			from .Zoom import ZoomCls
			self._zoom = ZoomCls(self._core, self._cmd_group)
		return self._zoom

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.spectrum.span.set(frequency = 1.0) \n
		Sets/queries the frequency span in Hz. Note that this command is maintained for compatibility reasons only.
		Use the [SENSe<ip>:]FREQuency:SPAN command for new remote control programs. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:ADEMod:SPECtrum:SPAN {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.ademod.spectrum.span.get() \n
		Sets/queries the frequency span in Hz. Note that this command is maintained for compatibility reasons only.
		Use the [SENSe<ip>:]FREQuency:SPAN command for new remote control programs. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SPECtrum:SPAN?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SpanCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpanCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
