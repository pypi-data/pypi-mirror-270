from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchCls:
	"""Pdcch commands group definition. 12 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcch", core, parent)

	@property
	def alevel(self):
		"""alevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alevel'):
			from .Alevel import AlevelCls
			self._alevel = AlevelCls(self._core, self._cmd_group)
		return self._alevel

	@property
	def cceIndex(self):
		"""cceIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cceIndex'):
			from .CceIndex import CceIndexCls
			self._cceIndex = CceIndexCls(self._core, self._cmd_group)
		return self._cceIndex

	@property
	def dciFormat(self):
		"""dciFormat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dciFormat'):
			from .DciFormat import DciFormatCls
			self._dciFormat = DciFormatCls(self._core, self._cmd_group)
		return self._dciFormat

	@property
	def dciSettings(self):
		"""dciSettings commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_dciSettings'):
			from .DciSettings import DciSettingsCls
			self._dciSettings = DciSettingsCls(self._core, self._cmd_group)
		return self._dciSettings

	@property
	def plength(self):
		"""plength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plength'):
			from .Plength import PlengthCls
			self._plength = PlengthCls(self._core, self._cmd_group)
		return self._plength

	@property
	def rnti(self):
		"""rnti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rnti'):
			from .Rnti import RntiCls
			self._rnti = RntiCls(self._core, self._cmd_group)
		return self._rnti

	@property
	def usage(self):
		"""usage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usage'):
			from .Usage import UsageCls
			self._usage = UsageCls(self._core, self._cmd_group)
		return self._usage

	def clone(self) -> 'PdcchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PdcchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
