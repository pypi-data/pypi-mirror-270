from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OoPowerCls:
	"""OoPower commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ooPower", core, parent)

	@property
	def offPower(self):
		"""offPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offPower'):
			from .OffPower import OffPowerCls
			self._offPower = OffPowerCls(self._core, self._cmd_group)
		return self._offPower

	@property
	def transient(self):
		"""transient commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transient'):
			from .Transient import TransientCls
			self._transient = TransientCls(self._core, self._cmd_group)
		return self._transient

	def clone(self) -> 'OoPowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OoPowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
