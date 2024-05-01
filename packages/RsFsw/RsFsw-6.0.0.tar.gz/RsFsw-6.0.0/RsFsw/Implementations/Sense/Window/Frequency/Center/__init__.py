from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CenterCls:
	"""Center commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

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

	def set(self, center: float, window=repcap.Window.Default) -> None:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:CENTer \n
		Snippet: driver.sense.window.frequency.center.set(center = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param center: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(center)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:FREQuency:CENTer {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:CENTer \n
		Snippet: value: float = driver.sense.window.frequency.center.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: center: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:FREQuency:CENTer?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'CenterCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CenterCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
