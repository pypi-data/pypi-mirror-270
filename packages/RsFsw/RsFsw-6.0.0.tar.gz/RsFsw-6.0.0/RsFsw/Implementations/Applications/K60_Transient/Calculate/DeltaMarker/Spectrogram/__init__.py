from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpectrogramCls:
	"""Spectrogram commands group definition. 12 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrogram", core, parent)

	@property
	def frame(self):
		"""frame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import FrameCls
			self._frame = FrameCls(self._core, self._cmd_group)
		return self._frame

	@property
	def sarea(self):
		"""sarea commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sarea'):
			from .Sarea import SareaCls
			self._sarea = SareaCls(self._core, self._cmd_group)
		return self._sarea

	@property
	def xy(self):
		"""xy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_xy'):
			from .Xy import XyCls
			self._xy = XyCls(self._core, self._cmd_group)
		return self._xy

	@property
	def y(self):
		"""y commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_y'):
			from .Y import YCls
			self._y = YCls(self._core, self._cmd_group)
		return self._y

	def clone(self) -> 'SpectrogramCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpectrogramCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
