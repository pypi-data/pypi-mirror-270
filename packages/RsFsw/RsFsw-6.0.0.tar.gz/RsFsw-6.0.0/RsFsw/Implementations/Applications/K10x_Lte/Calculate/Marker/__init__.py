from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MarkerCls:
	"""Marker commands group definition. 49 total commands, 13 Subgroups, 0 group commands
	Repeated Capability: Marker, default value after init: Marker.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("marker", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_marker_get', 'repcap_marker_set', repcap.Marker.Nr1)

	def repcap_marker_set(self, marker: repcap.Marker) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Marker.Default
		Default value after init: Marker.Nr1"""
		self._cmd_group.set_repcap_enum_value(marker)

	def repcap_marker_get(self) -> repcap.Marker:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def function(self):
		"""function commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_function'):
			from .Function import FunctionCls
			self._function = FunctionCls(self._core, self._cmd_group)
		return self._function

	@property
	def aoff(self):
		"""aoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aoff'):
			from .Aoff import AoffCls
			self._aoff = AoffCls(self._core, self._cmd_group)
		return self._aoff

	@property
	def count(self):
		"""count commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import CountCls
			self._count = CountCls(self._core, self._cmd_group)
		return self._count

	@property
	def coupling(self):
		"""coupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coupling'):
			from .Coupling import CouplingCls
			self._coupling = CouplingCls(self._core, self._cmd_group)
		return self._coupling

	@property
	def loExclude(self):
		"""loExclude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loExclude'):
			from .LoExclude import LoExcludeCls
			self._loExclude = LoExcludeCls(self._core, self._cmd_group)
		return self._loExclude

	@property
	def maximum(self):
		"""maximum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import MaximumCls
			self._maximum = MaximumCls(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import MinimumCls
			self._minimum = MinimumCls(self._core, self._cmd_group)
		return self._minimum

	@property
	def pexcursion(self):
		"""pexcursion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pexcursion'):
			from .Pexcursion import PexcursionCls
			self._pexcursion = PexcursionCls(self._core, self._cmd_group)
		return self._pexcursion

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	@property
	def x(self):
		"""x commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import XCls
			self._x = XCls(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import YCls
			self._y = YCls(self._core, self._cmd_group)
		return self._y

	@property
	def z(self):
		"""z commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_z'):
			from .Z import ZCls
			self._z = ZCls(self._core, self._cmd_group)
		return self._z

	def clone(self) -> 'MarkerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MarkerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
