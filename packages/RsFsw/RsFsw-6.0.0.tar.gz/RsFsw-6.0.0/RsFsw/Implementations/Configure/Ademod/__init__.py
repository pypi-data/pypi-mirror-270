from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdemodCls:
	"""Ademod commands group definition. 17 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ademod", core, parent)

	@property
	def results(self):
		"""results commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_results'):
			from .Results import ResultsCls
			self._results = ResultsCls(self._core, self._cmd_group)
		return self._results

	def clone(self) -> 'AdemodCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AdemodCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
