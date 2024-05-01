from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoiseCls:
	"""Noise commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	@property
	def uncertainty(self):
		"""uncertainty commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uncertainty'):
			from .Uncertainty import UncertaintyCls
			self._uncertainty = UncertaintyCls(self._core, self._cmd_group)
		return self._uncertainty

	def clone(self) -> 'NoiseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NoiseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
