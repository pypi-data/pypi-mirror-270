from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MarkerCls:
	"""Marker commands group definition. 1 total commands, 1 Subgroups, 0 group commands
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
	def link(self):
		"""link commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_link'):
			from .Link import LinkCls
			self._link = LinkCls(self._core, self._cmd_group)
		return self._link

	def clone(self) -> 'MarkerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MarkerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
