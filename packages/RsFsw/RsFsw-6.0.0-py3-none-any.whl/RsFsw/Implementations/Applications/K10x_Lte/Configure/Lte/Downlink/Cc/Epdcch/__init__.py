from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpdcchCls:
	"""Epdcch commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("epdcch", core, parent)

	@property
	def localized(self):
		"""localized commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_localized'):
			from .Localized import LocalizedCls
			self._localized = LocalizedCls(self._core, self._cmd_group)
		return self._localized

	@property
	def nprb(self):
		"""nprb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nprb'):
			from .Nprb import NprbCls
			self._nprb = NprbCls(self._core, self._cmd_group)
		return self._nprb

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def rbassign(self):
		"""rbassign commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbassign'):
			from .Rbassign import RbassignCls
			self._rbassign = RbassignCls(self._core, self._cmd_group)
		return self._rbassign

	@property
	def sid(self):
		"""sid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sid'):
			from .Sid import SidCls
			self._sid = SidCls(self._core, self._cmd_group)
		return self._sid

	def clone(self) -> 'EpdcchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EpdcchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
