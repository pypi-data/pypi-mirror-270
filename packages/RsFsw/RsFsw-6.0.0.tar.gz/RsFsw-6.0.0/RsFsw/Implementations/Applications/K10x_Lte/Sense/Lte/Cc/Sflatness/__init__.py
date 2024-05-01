from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SflatnessCls:
	"""Sflatness commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sflatness", core, parent)

	@property
	def econditions(self):
		"""econditions commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_econditions'):
			from .Econditions import EconditionsCls
			self._econditions = EconditionsCls(self._core, self._cmd_group)
		return self._econditions

	@property
	def oband(self):
		"""oband commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oband'):
			from .Oband import ObandCls
			self._oband = ObandCls(self._core, self._cmd_group)
		return self._oband

	def clone(self) -> 'SflatnessCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SflatnessCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
