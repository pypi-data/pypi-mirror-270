from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsweepCls:
	"""Psweep commands group definition. 13 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psweep", core, parent)

	@property
	def adjust(self):
		"""adjust commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import AdjustCls
			self._adjust = AdjustCls(self._core, self._cmd_group)
		return self._adjust

	@property
	def expected(self):
		"""expected commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_expected'):
			from .Expected import ExpectedCls
			self._expected = ExpectedCls(self._core, self._cmd_group)
		return self._expected

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def x(self):
		"""x commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_x'):
			from .X import XCls
			self._x = XCls(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_y'):
			from .Y import YCls
			self._y = YCls(self._core, self._cmd_group)
		return self._y

	@property
	def z(self):
		"""z commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_z'):
			from .Z import ZCls
			self._z = ZCls(self._core, self._cmd_group)
		return self._z

	def clone(self) -> 'PsweepCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PsweepCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
