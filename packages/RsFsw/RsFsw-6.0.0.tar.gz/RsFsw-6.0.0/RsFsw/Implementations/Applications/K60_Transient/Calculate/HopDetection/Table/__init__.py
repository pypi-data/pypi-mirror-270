from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TableCls:
	"""Table commands group definition. 34 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	@property
	def state(self):
		"""state commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def timing(self):
		"""timing commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import TimingCls
			self._timing = TimingCls(self._core, self._cmd_group)
		return self._timing

	@property
	def frequency(self):
		"""frequency commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def fmSettling(self):
		"""fmSettling commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmSettling'):
			from .FmSettling import FmSettlingCls
			self._fmSettling = FmSettlingCls(self._core, self._cmd_group)
		return self._fmSettling

	@property
	def pmSettling(self):
		"""pmSettling commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmSettling'):
			from .PmSettling import PmSettlingCls
			self._pmSettling = PmSettlingCls(self._core, self._cmd_group)
		return self._pmSettling

	@property
	def phase(self):
		"""phase commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import PhaseCls
			self._phase = PhaseCls(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import PowerCls
			self._power = PowerCls(self._core, self._cmd_group)
		return self._power

	@property
	def results(self):
		"""results commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_results'):
			from .Results import ResultsCls
			self._results = ResultsCls(self._core, self._cmd_group)
		return self._results

	@property
	def total(self):
		"""total commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_total'):
			from .Total import TotalCls
			self._total = TotalCls(self._core, self._cmd_group)
		return self._total

	@property
	def column(self):
		"""column commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_column'):
			from .Column import ColumnCls
			self._column = ColumnCls(self._core, self._cmd_group)
		return self._column

	def clone(self) -> 'TableCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TableCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
