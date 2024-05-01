from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PatternCls:
	"""Pattern commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Start import StartCls
			self._start = StartCls(self._core, self._cmd_group)
		return self._start

	@property
	def confidence(self):
		"""confidence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_confidence'):
			from .Confidence import ConfidenceCls
			self._confidence = ConfidenceCls(self._core, self._cmd_group)
		return self._confidence

	@property
	def correct(self):
		"""correct commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_correct'):
			from .Correct import CorrectCls
			self._correct = CorrectCls(self._core, self._cmd_group)
		return self._correct

	@property
	def present(self):
		"""present commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_present'):
			from .Present import PresentCls
			self._present = PresentCls(self._core, self._cmd_group)
		return self._present

	def clone(self) -> 'PatternCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PatternCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
