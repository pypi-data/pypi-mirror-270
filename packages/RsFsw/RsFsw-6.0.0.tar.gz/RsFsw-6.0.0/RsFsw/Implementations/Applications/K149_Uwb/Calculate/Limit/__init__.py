from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitCls:
	"""Limit commands group definition. 12 total commands, 1 Subgroups, 0 group commands
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
	def espectrum(self):
		"""espectrum commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_espectrum'):
			from .Espectrum import EspectrumCls
			self._espectrum = EspectrumCls(self._core, self._cmd_group)
		return self._espectrum

	def clone(self) -> 'LimitCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LimitCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
