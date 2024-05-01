from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XcorrCls:
	"""Xcorr commands group definition. 32 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("xcorr", core, parent)

	@property
	def mlobe(self):
		"""mlobe commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mlobe'):
			from .Mlobe import MlobeCls
			self._mlobe = MlobeCls(self._core, self._cmd_group)
		return self._mlobe

	@property
	def nmse(self):
		"""nmse commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_nmse'):
			from .Nmse import NmseCls
			self._nmse = NmseCls(self._core, self._cmd_group)
		return self._nmse

	@property
	def slobe(self):
		"""slobe commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_slobe'):
			from .Slobe import SlobeCls
			self._slobe = SlobeCls(self._core, self._cmd_group)
		return self._slobe

	def clone(self) -> 'XcorrCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = XcorrCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
