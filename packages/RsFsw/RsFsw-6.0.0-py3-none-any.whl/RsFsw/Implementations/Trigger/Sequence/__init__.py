from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SequenceCls:
	"""Sequence commands group definition. 28 total commands, 15 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequence", core, parent)

	@property
	def level(self):
		"""level commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import LevelCls
			self._level = LevelCls(self._core, self._cmd_group)
		return self._level

	@property
	def ctpis(self):
		"""ctpis commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctpis'):
			from .Ctpis import CtpisCls
			self._ctpis = CtpisCls(self._core, self._cmd_group)
		return self._ctpis

	@property
	def bbPower(self):
		"""bbPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbPower'):
			from .BbPower import BbPowerCls
			self._bbPower = BbPowerCls(self._core, self._cmd_group)
		return self._bbPower

	@property
	def time(self):
		"""time commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	@property
	def mask(self):
		"""mask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mask'):
			from .Mask import MaskCls
			self._mask = MaskCls(self._core, self._cmd_group)
		return self._mask

	@property
	def pretrigger(self):
		"""pretrigger commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pretrigger'):
			from .Pretrigger import PretriggerCls
			self._pretrigger = PretriggerCls(self._core, self._cmd_group)
		return self._pretrigger

	@property
	def postTrigger(self):
		"""postTrigger commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_postTrigger'):
			from .PostTrigger import PostTriggerCls
			self._postTrigger = PostTriggerCls(self._core, self._cmd_group)
		return self._postTrigger

	@property
	def tdTrigger(self):
		"""tdTrigger commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdTrigger'):
			from .TdTrigger import TdTriggerCls
			self._tdTrigger = TdTriggerCls(self._core, self._cmd_group)
		return self._tdTrigger

	@property
	def dtime(self):
		"""dtime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtime'):
			from .Dtime import DtimeCls
			self._dtime = DtimeCls(self._core, self._cmd_group)
		return self._dtime

	@property
	def holdoff(self):
		"""holdoff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_holdoff'):
			from .Holdoff import HoldoffCls
			self._holdoff = HoldoffCls(self._core, self._cmd_group)
		return self._holdoff

	@property
	def ifPower(self):
		"""ifPower commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ifPower'):
			from .IfPower import IfPowerCls
			self._ifPower = IfPowerCls(self._core, self._cmd_group)
		return self._ifPower

	@property
	def oscilloscope(self):
		"""oscilloscope commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_oscilloscope'):
			from .Oscilloscope import OscilloscopeCls
			self._oscilloscope = OscilloscopeCls(self._core, self._cmd_group)
		return self._oscilloscope

	@property
	def rfPower(self):
		"""rfPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfPower'):
			from .RfPower import RfPowerCls
			self._rfPower = RfPowerCls(self._core, self._cmd_group)
		return self._rfPower

	@property
	def slope(self):
		"""slope commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slope'):
			from .Slope import SlopeCls
			self._slope = SlopeCls(self._core, self._cmd_group)
		return self._slope

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import SourceCls
			self._source = SourceCls(self._core, self._cmd_group)
		return self._source

	def clone(self) -> 'SequenceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SequenceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
