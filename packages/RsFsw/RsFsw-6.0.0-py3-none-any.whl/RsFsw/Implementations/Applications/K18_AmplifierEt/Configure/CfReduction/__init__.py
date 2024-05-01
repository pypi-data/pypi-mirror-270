from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CfReductionCls:
	"""CfReduction commands group definition. 25 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfReduction", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def iterations(self):
		"""iterations commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iterations'):
			from .Iterations import IterationsCls
			self._iterations = IterationsCls(self._core, self._cmd_group)
		return self._iterations

	@property
	def ccFactor(self):
		"""ccFactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccFactor'):
			from .CcFactor import CcFactorCls
			self._ccFactor = CcFactorCls(self._core, self._cmd_group)
		return self._ccFactor

	@property
	def cfDelta(self):
		"""cfDelta commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfDelta'):
			from .CfDelta import CfDeltaCls
			self._cfDelta = CfDeltaCls(self._core, self._cmd_group)
		return self._cfDelta

	@property
	def sbandwidth(self):
		"""sbandwidth commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_sbandwidth'):
			from .Sbandwidth import SbandwidthCls
			self._sbandwidth = SbandwidthCls(self._core, self._cmd_group)
		return self._sbandwidth

	@property
	def cspacing(self):
		"""cspacing commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_cspacing'):
			from .Cspacing import CspacingCls
			self._cspacing = CspacingCls(self._core, self._cmd_group)
		return self._cspacing

	@property
	def apply(self):
		"""apply commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_apply'):
			from .Apply import ApplyCls
			self._apply = ApplyCls(self._core, self._cmd_group)
		return self._apply

	@property
	def read(self):
		"""read commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_read'):
			from .Read import ReadCls
			self._read = ReadCls(self._core, self._cmd_group)
		return self._read

	@property
	def rsOrignal(self):
		"""rsOrignal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsOrignal'):
			from .RsOrignal import RsOrignalCls
			self._rsOrignal = RsOrignalCls(self._core, self._cmd_group)
		return self._rsOrignal

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def pfrequency(self):
		"""pfrequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pfrequency'):
			from .Pfrequency import PfrequencyCls
			self._pfrequency = PfrequencyCls(self._core, self._cmd_group)
		return self._pfrequency

	@property
	def sfrequency(self):
		"""sfrequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfrequency'):
			from .Sfrequency import SfrequencyCls
			self._sfrequency = SfrequencyCls(self._core, self._cmd_group)
		return self._sfrequency

	@property
	def mfOrder(self):
		"""mfOrder commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mfOrder'):
			from .MfOrder import MfOrderCls
			self._mfOrder = MfOrderCls(self._core, self._cmd_group)
		return self._mfOrder

	def clone(self) -> 'CfReductionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CfReductionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
