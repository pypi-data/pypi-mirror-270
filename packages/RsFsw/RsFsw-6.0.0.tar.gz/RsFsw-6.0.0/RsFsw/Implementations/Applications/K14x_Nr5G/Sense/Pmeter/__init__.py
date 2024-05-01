from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmeterCls:
	"""Pmeter commands group definition. 17 total commands, 8 Subgroups, 0 group commands
	Repeated Capability: PowerMeter, default value after init: PowerMeter.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmeter", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_powerMeter_get', 'repcap_powerMeter_set', repcap.PowerMeter.Nr1)

	def repcap_powerMeter_set(self, powerMeter: repcap.PowerMeter) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to PowerMeter.Default
		Default value after init: PowerMeter.Nr1"""
		self._cmd_group.set_repcap_enum_value(powerMeter)

	def repcap_powerMeter_get(self) -> repcap.PowerMeter:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def dcycle(self):
		"""dcycle commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcycle'):
			from .Dcycle import DcycleCls
			self._dcycle = DcycleCls(self._core, self._cmd_group)
		return self._dcycle

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def mtime(self):
		"""mtime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtime'):
			from .Mtime import MtimeCls
			self._mtime = MtimeCls(self._core, self._cmd_group)
		return self._mtime

	@property
	def roffset(self):
		"""roffset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_roffset'):
			from .Roffset import RoffsetCls
			self._roffset = RoffsetCls(self._core, self._cmd_group)
		return self._roffset

	@property
	def soffset(self):
		"""soffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soffset'):
			from .Soffset import SoffsetCls
			self._soffset = SoffsetCls(self._core, self._cmd_group)
		return self._soffset

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def trigger(self):
		"""trigger commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import TriggerCls
			self._trigger = TriggerCls(self._core, self._cmd_group)
		return self._trigger

	@property
	def update(self):
		"""update commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_update'):
			from .Update import UpdateCls
			self._update = UpdateCls(self._core, self._cmd_group)
		return self._update

	def clone(self) -> 'PmeterCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PmeterCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
