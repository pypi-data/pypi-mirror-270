from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPyCls:
	"""FormatPy commands group definition. 5 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	@property
	def dexport(self):
		"""dexport commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_dexport'):
			from .Dexport import DexportCls
			self._dexport = DexportCls(self._core, self._cmd_group)
		return self._dexport

	@property
	def bstream(self):
		"""bstream commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bstream'):
			from .Bstream import BstreamCls
			self._bstream = BstreamCls(self._core, self._cmd_group)
		return self._bstream

	def clone(self) -> 'FormatPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FormatPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
