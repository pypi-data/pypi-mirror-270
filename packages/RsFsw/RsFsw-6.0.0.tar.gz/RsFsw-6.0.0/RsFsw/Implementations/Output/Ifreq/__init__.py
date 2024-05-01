from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfreqCls:
	"""Ifreq commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifreq", core, parent)

	@property
	def sband(self):
		"""sband commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sband'):
			from .Sband import SbandCls
			self._sband = SbandCls(self._core, self._cmd_group)
		return self._sband

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import SourceCls
			self._source = SourceCls(self._core, self._cmd_group)
		return self._source

	@property
	def ifFrequency(self):
		"""ifFrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ifFrequency'):
			from .IfFrequency import IfFrequencyCls
			self._ifFrequency = IfFrequencyCls(self._core, self._cmd_group)
		return self._ifFrequency

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'IfreqCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IfreqCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
