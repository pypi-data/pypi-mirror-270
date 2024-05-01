from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmSettlingCls:
	"""PmSettling commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmSettling", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	@property
	def pmsLength(self):
		"""pmsLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmsLength'):
			from .PmsLength import PmsLengthCls
			self._pmsLength = PmsLengthCls(self._core, self._cmd_group)
		return self._pmsLength

	@property
	def pmSpoint(self):
		"""pmSpoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmSpoint'):
			from .PmSpoint import PmSpointCls
			self._pmSpoint = PmSpointCls(self._core, self._cmd_group)
		return self._pmSpoint

	@property
	def pmStime(self):
		"""pmStime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmStime'):
			from .PmStime import PmStimeCls
			self._pmStime = PmStimeCls(self._core, self._cmd_group)
		return self._pmStime

	def clone(self) -> 'PmSettlingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PmSettlingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
