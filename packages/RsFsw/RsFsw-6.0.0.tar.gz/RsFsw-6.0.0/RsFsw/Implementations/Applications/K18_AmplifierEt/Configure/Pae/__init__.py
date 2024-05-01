from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PaeCls:
	"""Pae commands group definition. 7 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pae", core, parent)

	@property
	def ichannel(self):
		"""ichannel commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ichannel'):
			from .Ichannel import IchannelCls
			self._ichannel = IchannelCls(self._core, self._cmd_group)
		return self._ichannel

	@property
	def pconsumption(self):
		"""pconsumption commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pconsumption'):
			from .Pconsumption import PconsumptionCls
			self._pconsumption = PconsumptionCls(self._core, self._cmd_group)
		return self._pconsumption

	@property
	def qchannel(self):
		"""qchannel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_qchannel'):
			from .Qchannel import QchannelCls
			self._qchannel = QchannelCls(self._core, self._cmd_group)
		return self._qchannel

	def clone(self) -> 'PaeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PaeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
