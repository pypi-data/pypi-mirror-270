from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DdemCls:
	"""Ddem commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ddem", core, parent)

	@property
	def burst(self):
		"""burst commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import BurstCls
			self._burst = BurstCls(self._core, self._cmd_group)
		return self._burst

	@property
	def spectrum(self):
		"""spectrum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	def clone(self) -> 'DdemCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DdemCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
