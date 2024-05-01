from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TddCls:
	"""Tdd commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdd", core, parent)

	@property
	def spsc(self):
		"""spsc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spsc'):
			from .Spsc import SpscCls
			self._spsc = SpscCls(self._core, self._cmd_group)
		return self._spsc

	@property
	def udConf(self):
		"""udConf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_udConf'):
			from .UdConf import UdConfCls
			self._udConf = UdConfCls(self._core, self._cmd_group)
		return self._udConf

	def clone(self) -> 'TddCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TddCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
