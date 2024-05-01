from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CommunicateCls:
	"""Communicate commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("communicate", core, parent)

	@property
	def gpib(self):
		"""gpib commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gpib'):
			from .Gpib import GpibCls
			self._gpib = GpibCls(self._core, self._cmd_group)
		return self._gpib

	@property
	def tcpip(self):
		"""tcpip commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tcpip'):
			from .Tcpip import TcpipCls
			self._tcpip = TcpipCls(self._core, self._cmd_group)
		return self._tcpip

	@property
	def rdevice(self):
		"""rdevice commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rdevice'):
			from .Rdevice import RdeviceCls
			self._rdevice = RdeviceCls(self._core, self._cmd_group)
		return self._rdevice

	def clone(self) -> 'CommunicateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CommunicateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
