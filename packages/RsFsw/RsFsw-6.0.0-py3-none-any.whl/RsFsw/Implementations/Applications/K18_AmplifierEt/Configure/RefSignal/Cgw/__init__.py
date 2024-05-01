from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CgwCls:
	"""Cgw commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cgw", core, parent)

	@property
	def amode(self):
		"""amode commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amode'):
			from .Amode import AmodeCls
			self._amode = AmodeCls(self._core, self._cmd_group)
		return self._amode

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedStateCls
			self._ledState = LedStateCls(self._core, self._cmd_group)
		return self._ledState

	@property
	def read(self):
		"""read commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_read'):
			from .Read import ReadCls
			self._read = ReadCls(self._core, self._cmd_group)
		return self._read

	def clone(self) -> 'CgwCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CgwCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
