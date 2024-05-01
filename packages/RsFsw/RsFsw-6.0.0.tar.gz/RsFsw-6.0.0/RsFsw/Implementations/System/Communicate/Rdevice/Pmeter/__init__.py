from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmeterCls:
	"""Pmeter commands group definition. 3 total commands, 3 Subgroups, 0 group commands
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
	def define(self):
		"""define commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_define'):
			from .Define import DefineCls
			self._define = DefineCls(self._core, self._cmd_group)
		return self._define

	@property
	def configure(self):
		"""configure commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_configure'):
			from .Configure import ConfigureCls
			self._configure = ConfigureCls(self._core, self._cmd_group)
		return self._configure

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import CountCls
			self._count = CountCls(self._core, self._cmd_group)
		return self._count

	def clone(self) -> 'PmeterCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PmeterCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
