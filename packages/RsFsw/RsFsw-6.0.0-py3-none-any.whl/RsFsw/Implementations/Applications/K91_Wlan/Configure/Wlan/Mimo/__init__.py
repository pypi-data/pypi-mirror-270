from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	@property
	def capture(self):
		"""capture commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_capture'):
			from .Capture import CaptureCls
			self._capture = CaptureCls(self._core, self._cmd_group)
		return self._capture

	@property
	def csd(self):
		"""csd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csd'):
			from .Csd import CsdCls
			self._csd = CsdCls(self._core, self._cmd_group)
		return self._csd

	@property
	def osp(self):
		"""osp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_osp'):
			from .Osp import OspCls
			self._osp = OspCls(self._core, self._cmd_group)
		return self._osp

	def clone(self) -> 'MimoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MimoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
