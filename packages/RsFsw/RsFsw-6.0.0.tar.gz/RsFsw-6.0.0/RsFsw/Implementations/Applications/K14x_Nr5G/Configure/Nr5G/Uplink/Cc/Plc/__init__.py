from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlcCls:
	"""Plc commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plc", core, parent)

	@property
	def cid(self):
		"""cid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cid'):
			from .Cid import CidCls
			self._cid = CidCls(self._core, self._cmd_group)
		return self._cid

	@property
	def detection(self):
		"""detection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_detection'):
			from .Detection import DetectionCls
			self._detection = DetectionCls(self._core, self._cmd_group)
		return self._detection

	@property
	def pclass(self):
		"""pclass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pclass'):
			from .Pclass import PclassCls
			self._pclass = PclassCls(self._core, self._cmd_group)
		return self._pclass

	def clone(self) -> 'PlcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PlcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
