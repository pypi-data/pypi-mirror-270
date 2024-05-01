from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CalculateCls:
	"""Calculate commands group definition. 301 total commands, 13 Subgroups, 0 group commands
	Repeated Capability: Window, default value after init: Window.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calculate", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_window_get', 'repcap_window_set', repcap.Window.Nr1)

	def repcap_window_set(self, window: repcap.Window) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Window.Default
		Default value after init: Window.Nr1"""
		self._cmd_group.set_repcap_enum_value(window)

	def repcap_window_get(self) -> repcap.Window:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def distribution(self):
		"""distribution commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_distribution'):
			from .Distribution import DistributionCls
			self._distribution = DistributionCls(self._core, self._cmd_group)
		return self._distribution

	@property
	def unit(self):
		"""unit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import UnitCls
			self._unit = UnitCls(self._core, self._cmd_group)
		return self._unit

	@property
	def deltaMarker(self):
		"""deltaMarker commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_deltaMarker'):
			from .DeltaMarker import DeltaMarkerCls
			self._deltaMarker = DeltaMarkerCls(self._core, self._cmd_group)
		return self._deltaMarker

	@property
	def marker(self):
		"""marker commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import MarkerCls
			self._marker = MarkerCls(self._core, self._cmd_group)
		return self._marker

	@property
	def msra(self):
		"""msra commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_msra'):
			from .Msra import MsraCls
			self._msra = MsraCls(self._core, self._cmd_group)
		return self._msra

	@property
	def rtms(self):
		"""rtms commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rtms'):
			from .Rtms import RtmsCls
			self._rtms = RtmsCls(self._core, self._cmd_group)
		return self._rtms

	@property
	def ar(self):
		"""ar commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ar'):
			from .Ar import ArCls
			self._ar = ArCls(self._core, self._cmd_group)
		return self._ar

	@property
	def hopDetection(self):
		"""hopDetection commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_hopDetection'):
			from .HopDetection import HopDetectionCls
			self._hopDetection = HopDetectionCls(self._core, self._cmd_group)
		return self._hopDetection

	@property
	def chrDetection(self):
		"""chrDetection commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_chrDetection'):
			from .ChrDetection import ChrDetectionCls
			self._chrDetection = ChrDetectionCls(self._core, self._cmd_group)
		return self._chrDetection

	@property
	def result(self):
		"""result commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import ResultCls
			self._result = ResultCls(self._core, self._cmd_group)
		return self._result

	@property
	def spectrogram(self):
		"""spectrogram commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_spectrogram'):
			from .Spectrogram import SpectrogramCls
			self._spectrogram = SpectrogramCls(self._core, self._cmd_group)
		return self._spectrogram

	@property
	def trace(self):
		"""trace commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import TraceCls
			self._trace = TraceCls(self._core, self._cmd_group)
		return self._trace

	@property
	def trend(self):
		"""trend commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_trend'):
			from .Trend import TrendCls
			self._trend = TrendCls(self._core, self._cmd_group)
		return self._trend

	def clone(self) -> 'CalculateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CalculateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
