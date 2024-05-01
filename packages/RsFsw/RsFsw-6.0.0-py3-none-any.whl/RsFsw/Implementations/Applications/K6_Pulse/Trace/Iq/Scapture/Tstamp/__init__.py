from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TstampCls:
	"""Tstamp commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tstamp", core, parent)

	@property
	def sstart(self):
		"""sstart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sstart'):
			from .Sstart import SstartCls
			self._sstart = SstartCls(self._core, self._cmd_group)
		return self._sstart

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import TriggerCls
			self._trigger = TriggerCls(self._core, self._cmd_group)
		return self._trigger

	def clone(self) -> 'TstampCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TstampCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
