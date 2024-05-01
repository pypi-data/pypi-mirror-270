from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LayoutCls:
	"""Layout commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("layout", core, parent)

	@property
	def identify(self):
		"""identify commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_identify'):
			from .Identify import IdentifyCls
			self._identify = IdentifyCls(self._core, self._cmd_group)
		return self._identify

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import CatalogCls
			self._catalog = CatalogCls(self._core, self._cmd_group)
		return self._catalog

	@property
	def add(self):
		"""add commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_add'):
			from .Add import AddCls
			self._add = AddCls(self._core, self._cmd_group)
		return self._add

	@property
	def replace(self):
		"""replace commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_replace'):
			from .Replace import ReplaceCls
			self._replace = ReplaceCls(self._core, self._cmd_group)
		return self._replace

	@property
	def move(self):
		"""move commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_move'):
			from .Move import MoveCls
			self._move = MoveCls(self._core, self._cmd_group)
		return self._move

	@property
	def remove(self):
		"""remove commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_remove'):
			from .Remove import RemoveCls
			self._remove = RemoveCls(self._core, self._cmd_group)
		return self._remove

	@property
	def splitter(self):
		"""splitter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_splitter'):
			from .Splitter import SplitterCls
			self._splitter = SplitterCls(self._core, self._cmd_group)
		return self._splitter

	def clone(self) -> 'LayoutCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LayoutCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
