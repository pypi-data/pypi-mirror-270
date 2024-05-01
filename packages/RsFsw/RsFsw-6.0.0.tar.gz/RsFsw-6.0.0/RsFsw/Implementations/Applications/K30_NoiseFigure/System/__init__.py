from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SystemCls:
	"""System commands group definition. 12 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	@property
	def communicate(self):
		"""communicate commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_communicate'):
			from .Communicate import CommunicateCls
			self._communicate = CommunicateCls(self._core, self._cmd_group)
		return self._communicate

	@property
	def configure(self):
		"""configure commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_configure'):
			from .Configure import ConfigureCls
			self._configure = ConfigureCls(self._core, self._cmd_group)
		return self._configure

	@property
	def preset(self):
		"""preset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_preset'):
			from .Preset import PresetCls
			self._preset = PresetCls(self._core, self._cmd_group)
		return self._preset

	def clone(self) -> 'SystemCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SystemCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
