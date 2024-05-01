from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XCls:
	"""X commands group definition. 5 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	@property
	def slimits(self):
		"""slimits commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_slimits'):
			from .Slimits import SlimitsCls
			self._slimits = SlimitsCls(self._core, self._cmd_group)
		return self._slimits

	@property
	def ssize(self):
		"""ssize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ssize'):
			from .Ssize import SsizeCls
			self._ssize = SsizeCls(self._core, self._cmd_group)
		return self._ssize

	def clone(self) -> 'XCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = XCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
