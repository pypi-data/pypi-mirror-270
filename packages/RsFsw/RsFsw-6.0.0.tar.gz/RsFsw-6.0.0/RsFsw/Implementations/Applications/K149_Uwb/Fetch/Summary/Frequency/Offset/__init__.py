from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffsetCls:
	"""Offset commands group definition. 8 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	@property
	def hz(self):
		"""hz commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_hz'):
			from .Hz import HzCls
			self._hz = HzCls(self._core, self._cmd_group)
		return self._hz

	@property
	def ppm(self):
		"""ppm commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppm'):
			from .Ppm import PpmCls
			self._ppm = PpmCls(self._core, self._cmd_group)
		return self._ppm

	def clone(self) -> 'OffsetCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OffsetCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
