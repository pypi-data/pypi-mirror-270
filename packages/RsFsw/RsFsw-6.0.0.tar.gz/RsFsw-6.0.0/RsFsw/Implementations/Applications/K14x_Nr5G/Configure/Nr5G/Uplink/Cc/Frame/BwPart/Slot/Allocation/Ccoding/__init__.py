from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcodingCls:
	"""Ccoding commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccoding", core, parent)

	@property
	def imcs(self):
		"""imcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imcs'):
			from .Imcs import ImcsCls
			self._imcs = ImcsCls(self._core, self._cmd_group)
		return self._imcs

	@property
	def mcsTable(self):
		"""mcsTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .McsTable import McsTableCls
			self._mcsTable = McsTableCls(self._core, self._cmd_group)
		return self._mcsTable

	@property
	def rvIndex(self):
		"""rvIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rvIndex'):
			from .RvIndex import RvIndexCls
			self._rvIndex = RvIndexCls(self._core, self._cmd_group)
		return self._rvIndex

	def clone(self) -> 'CcodingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcodingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
