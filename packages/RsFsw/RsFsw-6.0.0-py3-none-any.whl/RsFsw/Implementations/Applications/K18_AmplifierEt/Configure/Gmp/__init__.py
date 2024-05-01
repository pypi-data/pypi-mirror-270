from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GmpCls:
	"""Gmp commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gmp", core, parent)

	@property
	def lag(self):
		"""lag commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lag'):
			from .Lag import LagCls
			self._lag = LagCls(self._core, self._cmd_group)
		return self._lag

	@property
	def lead(self):
		"""lead commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lead'):
			from .Lead import LeadCls
			self._lead = LeadCls(self._core, self._cmd_group)
		return self._lead

	def clone(self) -> 'GmpCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GmpCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
