from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LxiCls:
	"""Lxi commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lxi", core, parent)

	@property
	def lanReset(self):
		"""lanReset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lanReset'):
			from .LanReset import LanResetCls
			self._lanReset = LanResetCls(self._core, self._cmd_group)
		return self._lanReset

	@property
	def mdescription(self):
		"""mdescription commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mdescription'):
			from .Mdescription import MdescriptionCls
			self._mdescription = MdescriptionCls(self._core, self._cmd_group)
		return self._mdescription

	@property
	def password(self):
		"""password commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_password'):
			from .Password import PasswordCls
			self._password = PasswordCls(self._core, self._cmd_group)
		return self._password

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_info'):
			from .Info import InfoCls
			self._info = InfoCls(self._core, self._cmd_group)
		return self._info

	def clone(self) -> 'LxiCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LxiCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
