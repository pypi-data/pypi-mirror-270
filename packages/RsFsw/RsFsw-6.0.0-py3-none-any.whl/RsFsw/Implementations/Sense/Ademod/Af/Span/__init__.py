from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpanCls:
	"""Span commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("span", core, parent)

	@property
	def full(self):
		"""full commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_full'):
			from .Full import FullCls
			self._full = FullCls(self._core, self._cmd_group)
		return self._full

	def set(self, span: float) -> None:
		"""SCPI: [SENSe]:ADEMod:AF:SPAN \n
		Snippet: driver.sense.ademod.af.span.set(span = 1.0) \n
		Sets the span (around the center frequency) for AF spectrum result display. The span is limited to DBW/2 (see
		[SENSe:]BWIDth:DEMod) . \n
			:param span: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(span)
		self._core.io.write(f'SENSe:ADEMod:AF:SPAN {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:AF:SPAN \n
		Snippet: value: float = driver.sense.ademod.af.span.get() \n
		Sets the span (around the center frequency) for AF spectrum result display. The span is limited to DBW/2 (see
		[SENSe:]BWIDth:DEMod) . \n
			:return: span: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:ADEMod:AF:SPAN?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SpanCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpanCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
