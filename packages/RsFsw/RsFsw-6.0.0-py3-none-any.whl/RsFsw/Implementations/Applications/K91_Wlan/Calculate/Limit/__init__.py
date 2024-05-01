from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 65 total commands, 9 Subgroups, 0 group commands
	Repeated Capability: LimitIx, default value after init: LimitIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_limitIx_get', 'repcap_limitIx_set', repcap.LimitIx.Nr1)

	def repcap_limitIx_set(self, limitIx: repcap.LimitIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to LimitIx.Default
		Default value after init: LimitIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(limitIx)

	def repcap_limitIx_get(self) -> repcap.LimitIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def burst(self):
		"""burst commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import BurstCls
			self._burst = BurstCls(self._core, self._cmd_group)
		return self._burst

	@property
	def control(self):
		"""control commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import ControlCls
			self._control = ControlCls(self._core, self._cmd_group)
		return self._control

	@property
	def spectrum(self):
		"""spectrum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import SpectrumCls
			self._spectrum = SpectrumCls(self._core, self._cmd_group)
		return self._spectrum

	@property
	def tolerance(self):
		"""tolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tolerance'):
			from .Tolerance import ToleranceCls
			self._tolerance = ToleranceCls(self._core, self._cmd_group)
		return self._tolerance

	@property
	def upper(self):
		"""upper commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_upper'):
			from .Upper import UpperCls
			self._upper = UpperCls(self._core, self._cmd_group)
		return self._upper

	@property
	def lower(self):
		"""lower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lower'):
			from .Lower import LowerCls
			self._lower = LowerCls(self._core, self._cmd_group)
		return self._lower

	@property
	def fail(self):
		"""fail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fail'):
			from .Fail import FailCls
			self._fail = FailCls(self._core, self._cmd_group)
		return self._fail

	@property
	def espectrum(self):
		"""espectrum commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_espectrum'):
			from .Espectrum import EspectrumCls
			self._espectrum = EspectrumCls(self._core, self._cmd_group)
		return self._espectrum

	@property
	def acPower(self):
		"""acPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_acPower'):
			from .AcPower import AcPowerCls
			self._acPower = AcPowerCls(self._core, self._cmd_group)
		return self._acPower

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
