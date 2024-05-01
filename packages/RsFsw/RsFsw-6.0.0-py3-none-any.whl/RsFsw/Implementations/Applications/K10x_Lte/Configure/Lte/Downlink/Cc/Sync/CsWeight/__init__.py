from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CsWeightCls:
	"""CsWeight commands group definition. 10 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csWeight", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def noFrame(self):
		"""noFrame commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noFrame'):
			from .NoFrame import NoFrameCls
			self._noFrame = NoFrameCls(self._core, self._cmd_group)
		return self._noFrame

	@property
	def fhFrame(self):
		"""fhFrame commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fhFrame'):
			from .FhFrame import FhFrameCls
			self._fhFrame = FhFrameCls(self._core, self._cmd_group)
		return self._fhFrame

	@property
	def shFrame(self):
		"""shFrame commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_shFrame'):
			from .ShFrame import ShFrameCls
			self._shFrame = ShFrameCls(self._core, self._cmd_group)
		return self._shFrame

	@property
	def antenna(self):
		"""antenna commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import AntennaCls
			self._antenna = AntennaCls(self._core, self._cmd_group)
		return self._antenna

	def clone(self) -> 'CsWeightCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CsWeightCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
