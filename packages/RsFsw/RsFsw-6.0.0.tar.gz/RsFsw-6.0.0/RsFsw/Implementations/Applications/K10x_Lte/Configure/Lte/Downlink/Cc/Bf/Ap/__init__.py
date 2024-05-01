from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApCls:
	"""Ap commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ap", core, parent)

	@property
	def cell(self):
		"""cell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cell'):
			from .Cell import CellCls
			self._cell = CellCls(self._core, self._cmd_group)
		return self._cell

	@property
	def csi(self):
		"""csi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csi'):
			from .Csi import CsiCls
			self._csi = CsiCls(self._core, self._cmd_group)
		return self._csi

	@property
	def uers(self):
		"""uers commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uers'):
			from .Uers import UersCls
			self._uers = UersCls(self._core, self._cmd_group)
		return self._uers

	def clone(self) -> 'ApCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
