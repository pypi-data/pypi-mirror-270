from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultipleCls:
	"""Multiple commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: ZoomWindow, default value after init: ZoomWindow.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiple", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_zoomWindow_get', 'repcap_zoomWindow_set', repcap.ZoomWindow.Nr1)

	def repcap_zoomWindow_set(self, zoomWindow: repcap.ZoomWindow) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ZoomWindow.Default
		Default value after init: ZoomWindow.Nr1"""
		self._cmd_group.set_repcap_enum_value(zoomWindow)

	def repcap_zoomWindow_get(self) -> repcap.ZoomWindow:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def area(self):
		"""area commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_area'):
			from .Area import AreaCls
			self._area = AreaCls(self._core, self._cmd_group)
		return self._area

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'MultipleCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultipleCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
