from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AchannelCls:
	"""Achannel commands group definition. 15 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("achannel", core, parent)

	@property
	def preset(self):
		"""preset commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_preset'):
			from .Preset import PresetCls
			self._preset = PresetCls(self._core, self._cmd_group)
		return self._preset

	@property
	def acPairs(self):
		"""acPairs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acPairs'):
			from .AcPairs import AcPairsCls
			self._acPairs = AcPairsCls(self._core, self._cmd_group)
		return self._acPairs

	@property
	def bandwidth(self):
		"""bandwidth commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def cbwidth(self):
		"""cbwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbwidth'):
			from .Cbwidth import CbwidthCls
			self._cbwidth = CbwidthCls(self._core, self._cmd_group)
		return self._cbwidth

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def reference(self):
		"""reference commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import ReferenceCls
			self._reference = ReferenceCls(self._core, self._cmd_group)
		return self._reference

	@property
	def spacing(self):
		"""spacing commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_spacing'):
			from .Spacing import SpacingCls
			self._spacing = SpacingCls(self._core, self._cmd_group)
		return self._spacing

	@property
	def txChannel(self):
		"""txChannel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_txChannel'):
			from .TxChannel import TxChannelCls
			self._txChannel = TxChannelCls(self._core, self._cmd_group)
		return self._txChannel

	def clone(self) -> 'AchannelCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AchannelCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
