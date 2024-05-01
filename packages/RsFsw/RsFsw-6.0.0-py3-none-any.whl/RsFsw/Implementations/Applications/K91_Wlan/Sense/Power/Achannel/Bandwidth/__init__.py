from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BandwidthCls:
	"""Bandwidth commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import ChannelCls
			self._channel = ChannelCls(self._core, self._cmd_group)
		return self._channel

	@property
	def achannel(self):
		"""achannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_achannel'):
			from .Achannel import AchannelCls
			self._achannel = AchannelCls(self._core, self._cmd_group)
		return self._achannel

	@property
	def alternate(self):
		"""alternate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alternate'):
			from .Alternate import AlternateCls
			self._alternate = AlternateCls(self._core, self._cmd_group)
		return self._alternate

	def clone(self) -> 'BandwidthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BandwidthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
