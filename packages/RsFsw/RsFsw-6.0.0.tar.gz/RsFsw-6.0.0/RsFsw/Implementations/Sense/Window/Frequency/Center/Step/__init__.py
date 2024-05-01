from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StepCls:
	"""Step commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	@property
	def link(self):
		"""link commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_link'):
			from .Link import LinkCls
			self._link = LinkCls(self._core, self._cmd_group)
		return self._link

	def set(self, frequency_step: float, window=repcap.Window.Default) -> None:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:CENTer:STEP \n
		Snippet: driver.sense.window.frequency.center.step.set(frequency_step = 1.0, window = repcap.Window.Default) \n
		No command help available \n
			:param frequency_step: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(frequency_step)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:FREQuency:CENTer:STEP {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: [SENSe][:WINDow<n>]:FREQuency:CENTer:STEP \n
		Snippet: value: float = driver.sense.window.frequency.center.step.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: frequency_step: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:FREQuency:CENTer:STEP?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'StepCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StepCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
