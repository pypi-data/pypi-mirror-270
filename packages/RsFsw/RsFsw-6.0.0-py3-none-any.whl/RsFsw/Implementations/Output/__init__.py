from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OutputCls:
	"""Output commands group definition. 23 total commands, 8 Subgroups, 0 group commands
	Repeated Capability: OutputConnector, default value after init: OutputConnector.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_outputConnector_get', 'repcap_outputConnector_set', repcap.OutputConnector.Nr1)

	def repcap_outputConnector_set(self, outputConnector: repcap.OutputConnector) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to OutputConnector.Default
		Default value after init: OutputConnector.Nr1"""
		self._cmd_group.set_repcap_enum_value(outputConnector)

	def repcap_outputConnector_get(self) -> repcap.OutputConnector:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def diq(self):
		"""diq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_diq'):
			from .Diq import DiqCls
			self._diq = DiqCls(self._core, self._cmd_group)
		return self._diq

	@property
	def iqhs(self):
		"""iqhs commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqhs'):
			from .Iqhs import IqhsCls
			self._iqhs = IqhsCls(self._core, self._cmd_group)
		return self._iqhs

	@property
	def uport(self):
		"""uport commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_uport'):
			from .Uport import UportCls
			self._uport = UportCls(self._core, self._cmd_group)
		return self._uport

	@property
	def ifreq(self):
		"""ifreq commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ifreq'):
			from .Ifreq import IfreqCls
			self._ifreq = IfreqCls(self._core, self._cmd_group)
		return self._ifreq

	@property
	def video(self):
		"""video commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_video'):
			from .Video import VideoCls
			self._video = VideoCls(self._core, self._cmd_group)
		return self._video

	@property
	def ademod(self):
		"""ademod commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ademod'):
			from .Ademod import AdemodCls
			self._ademod = AdemodCls(self._core, self._cmd_group)
		return self._ademod

	@property
	def trigger(self):
		"""trigger commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import TriggerCls
			self._trigger = TriggerCls(self._core, self._cmd_group)
		return self._trigger

	def clone(self) -> 'OutputCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OutputCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
