from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


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

	def set(self, span: float, window=repcap.Window.Default) -> None:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:SPAN \n
		Snippet: driver.sense.window.frequency.span.set(span = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param span: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(span)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:FREQuency:SPAN {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:SPAN \n
		Snippet: value: float = driver.sense.window.frequency.span.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: span: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:FREQuency:SPAN?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SpanCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpanCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
