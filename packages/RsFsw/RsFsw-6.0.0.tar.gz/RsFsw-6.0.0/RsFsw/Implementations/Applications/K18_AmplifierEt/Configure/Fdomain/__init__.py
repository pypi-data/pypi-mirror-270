from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FdomainCls:
	"""Fdomain commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fdomain", core, parent)

	@property
	def fftLength(self):
		"""fftLength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fftLength'):
			from .FftLength import FftLengthCls
			self._fftLength = FftLengthCls(self._core, self._cmd_group)
		return self._fftLength

	@property
	def wfunction(self):
		"""wfunction commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wfunction'):
			from .Wfunction import WfunctionCls
			self._wfunction = WfunctionCls(self._core, self._cmd_group)
		return self._wfunction

	@property
	def woverlap(self):
		"""woverlap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_woverlap'):
			from .Woverlap import WoverlapCls
			self._woverlap = WoverlapCls(self._core, self._cmd_group)
		return self._woverlap

	@property
	def wlfRatio(self):
		"""wlfRatio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_wlfRatio'):
			from .WlfRatio import WlfRatioCls
			self._wlfRatio = WlfRatioCls(self._core, self._cmd_group)
		return self._wlfRatio

	@property
	def squelch(self):
		"""squelch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_squelch'):
			from .Squelch import SquelchCls
			self._squelch = SquelchCls(self._core, self._cmd_group)
		return self._squelch

	def clone(self) -> 'FdomainCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FdomainCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
