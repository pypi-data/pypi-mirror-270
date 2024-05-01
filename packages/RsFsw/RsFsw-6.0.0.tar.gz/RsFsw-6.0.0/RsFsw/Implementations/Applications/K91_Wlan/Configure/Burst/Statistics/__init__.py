from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatisticsCls:
	"""Statistics commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistics", core, parent)

	@property
	def bstream(self):
		"""bstream commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bstream'):
			from .Bstream import BstreamCls
			self._bstream = BstreamCls(self._core, self._cmd_group)
		return self._bstream

	@property
	def cumulativeDistribFnc(self):
		"""cumulativeDistribFnc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cumulativeDistribFnc'):
			from .CumulativeDistribFnc import CumulativeDistribFncCls
			self._cumulativeDistribFnc = CumulativeDistribFncCls(self._core, self._cmd_group)
		return self._cumulativeDistribFnc

	@property
	def sfield(self):
		"""sfield commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sfield'):
			from .Sfield import SfieldCls
			self._sfield = SfieldCls(self._core, self._cmd_group)
		return self._sfield

	def clone(self) -> 'StatisticsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StatisticsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
