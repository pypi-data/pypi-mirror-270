from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcCls:
	"""Cc commands group definition. 12 total commands, 11 Subgroups, 0 group commands
	Repeated Capability: CarrierComponent, default value after init: CarrierComponent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrierComponent_get', 'repcap_carrierComponent_set', repcap.CarrierComponent.Nr1)

	def repcap_carrierComponent_set(self, carrierComponent: repcap.CarrierComponent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponent.Default
		Default value after init: CarrierComponent.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrierComponent)

	def repcap_carrierComponent_get(self) -> repcap.CarrierComponent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def allocation(self):
		"""allocation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_allocation'):
			from .Allocation import AllocationCls
			self._allocation = AllocationCls(self._core, self._cmd_group)
		return self._allocation

	@property
	def antenna(self):
		"""antenna commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import AntennaCls
			self._antenna = AntennaCls(self._core, self._cmd_group)
		return self._antenna

	@property
	def carrier(self):
		"""carrier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import CarrierCls
			self._carrier = CarrierCls(self._core, self._cmd_group)
		return self._carrier

	@property
	def cword(self):
		"""cword commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cword'):
			from .Cword import CwordCls
			self._cword = CwordCls(self._core, self._cmd_group)
		return self._cword

	@property
	def location(self):
		"""location commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_location'):
			from .Location import LocationCls
			self._location = LocationCls(self._core, self._cmd_group)
		return self._location

	@property
	def modulation(self):
		"""modulation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import ModulationCls
			self._modulation = ModulationCls(self._core, self._cmd_group)
		return self._modulation

	@property
	def preamble(self):
		"""preamble commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import PreambleCls
			self._preamble = PreambleCls(self._core, self._cmd_group)
		return self._preamble

	@property
	def sflatness(self):
		"""sflatness commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sflatness'):
			from .Sflatness import SflatnessCls
			self._sflatness = SflatnessCls(self._core, self._cmd_group)
		return self._sflatness

	@property
	def slot(self):
		"""slot commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import SlotCls
			self._slot = SlotCls(self._core, self._cmd_group)
		return self._slot

	@property
	def subframe(self):
		"""subframe commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_subframe'):
			from .Subframe import SubframeCls
			self._subframe = SubframeCls(self._core, self._cmd_group)
		return self._subframe

	@property
	def symbol(self):
		"""symbol commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbol'):
			from .Symbol import SymbolCls
			self._symbol = SymbolCls(self._core, self._cmd_group)
		return self._symbol

	def clone(self) -> 'CcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
