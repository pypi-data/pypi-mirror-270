from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OscCls:
	"""Osc commands group definition. 17 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("osc", core, parent)

	@property
	def conState(self):
		"""conState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_conState'):
			from .ConState import ConStateCls
			self._conState = ConStateCls(self._core, self._cmd_group)
		return self._conState

	@property
	def idn(self):
		"""idn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_idn'):
			from .Idn import IdnCls
			self._idn = IdnCls(self._core, self._cmd_group)
		return self._idn

	@property
	def impedance(self):
		"""impedance commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_impedance'):
			from .Impedance import ImpedanceCls
			self._impedance = ImpedanceCls(self._core, self._cmd_group)
		return self._impedance

	@property
	def coupling(self):
		"""coupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coupling'):
			from .Coupling import CouplingCls
			self._coupling = CouplingCls(self._core, self._cmd_group)
		return self._coupling

	@property
	def vdevice(self):
		"""vdevice commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vdevice'):
			from .Vdevice import VdeviceCls
			self._vdevice = VdeviceCls(self._core, self._cmd_group)
		return self._vdevice

	@property
	def vfirmware(self):
		"""vfirmware commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vfirmware'):
			from .Vfirmware import VfirmwareCls
			self._vfirmware = VfirmwareCls(self._core, self._cmd_group)
		return self._vfirmware

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def tcpip(self):
		"""tcpip commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcpip'):
			from .Tcpip import TcpipCls
			self._tcpip = TcpipCls(self._core, self._cmd_group)
		return self._tcpip

	@property
	def balanced(self):
		"""balanced commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_balanced'):
			from .Balanced import BalancedCls
			self._balanced = BalancedCls(self._core, self._cmd_group)
		return self._balanced

	@property
	def fullscale(self):
		"""fullscale commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fullscale'):
			from .Fullscale import FullscaleCls
			self._fullscale = FullscaleCls(self._core, self._cmd_group)
		return self._fullscale

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRateCls
			self._symbolRate = SymbolRateCls(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def skew(self):
		"""skew commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_skew'):
			from .Skew import SkewCls
			self._skew = SkewCls(self._core, self._cmd_group)
		return self._skew

	def clone(self) -> 'OscCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OscCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
