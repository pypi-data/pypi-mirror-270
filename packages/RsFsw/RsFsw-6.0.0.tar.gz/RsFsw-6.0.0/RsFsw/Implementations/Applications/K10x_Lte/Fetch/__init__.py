from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FetchCls:
	"""Fetch commands group definition. 108 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fetch", core, parent)

	@property
	def cc(self):
		"""cc commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import CcCls
			self._cc = CcCls(self._core, self._cmd_group)
		return self._cc

	@property
	def fePpm(self):
		"""fePpm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fePpm'):
			from .FePpm import FePpmCls
			self._fePpm = FePpmCls(self._core, self._cmd_group)
		return self._fePpm

	@property
	def freqError(self):
		"""freqError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqErrorCls
			self._freqError = FreqErrorCls(self._core, self._cmd_group)
		return self._freqError

	@property
	def taError(self):
		"""taError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_taError'):
			from .TaError import TaErrorCls
			self._taError = TaErrorCls(self._core, self._cmd_group)
		return self._taError

	@property
	def pmeter(self):
		"""pmeter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import PmeterCls
			self._pmeter = PmeterCls(self._core, self._cmd_group)
		return self._pmeter

	def clone(self) -> 'FetchCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FetchCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
