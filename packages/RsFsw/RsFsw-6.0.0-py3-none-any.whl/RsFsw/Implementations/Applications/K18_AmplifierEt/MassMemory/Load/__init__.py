from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoadCls:
	"""Load commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("load", core, parent)

	@property
	def equalizer(self):
		"""equalizer commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_equalizer'):
			from .Equalizer import EqualizerCls
			self._equalizer = EqualizerCls(self._core, self._cmd_group)
		return self._equalizer

	@property
	def iq(self):
		"""iq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import IqCls
			self._iq = IqCls(self._core, self._cmd_group)
		return self._iq

	@property
	def mdpd(self):
		"""mdpd commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mdpd'):
			from .Mdpd import MdpdCls
			self._mdpd = MdpdCls(self._core, self._cmd_group)
		return self._mdpd

	def clone(self) -> 'LoadCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LoadCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
