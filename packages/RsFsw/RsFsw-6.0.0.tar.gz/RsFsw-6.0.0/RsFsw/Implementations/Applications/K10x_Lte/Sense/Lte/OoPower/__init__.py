from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OoPowerCls:
	"""OoPower commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ooPower", core, parent)

	@property
	def atiming(self):
		"""atiming commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_atiming'):
			from .Atiming import AtimingCls
			self._atiming = AtimingCls(self._core, self._cmd_group)
		return self._atiming

	@property
	def ncorrection(self):
		"""ncorrection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncorrection'):
			from .Ncorrection import NcorrectionCls
			self._ncorrection = NcorrectionCls(self._core, self._cmd_group)
		return self._ncorrection

	def clone(self) -> 'OoPowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OoPowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
