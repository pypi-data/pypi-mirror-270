from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FskCls:
	"""Fsk commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fsk", core, parent)

	@property
	def cfdrift(self):
		"""cfdrift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfdrift'):
			from .Cfdrift import CfdriftCls
			self._cfdrift = CfdriftCls(self._core, self._cmd_group)
		return self._cfdrift

	@property
	def derror(self):
		"""derror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_derror'):
			from .Derror import DerrorCls
			self._derror = DerrorCls(self._core, self._cmd_group)
		return self._derror

	@property
	def mdeviation(self):
		"""mdeviation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mdeviation'):
			from .Mdeviation import MdeviationCls
			self._mdeviation = MdeviationCls(self._core, self._cmd_group)
		return self._mdeviation

	@property
	def rdeviation(self):
		"""rdeviation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rdeviation'):
			from .Rdeviation import RdeviationCls
			self._rdeviation = RdeviationCls(self._core, self._cmd_group)
		return self._rdeviation

	def clone(self) -> 'FskCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FskCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
