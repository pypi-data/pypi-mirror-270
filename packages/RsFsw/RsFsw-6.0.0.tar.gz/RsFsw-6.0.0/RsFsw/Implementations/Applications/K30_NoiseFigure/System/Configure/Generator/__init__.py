from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeneratorCls:
	"""Generator commands group definition. 4 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def control(self):
		"""control commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import ControlCls
			self._control = ControlCls(self._core, self._cmd_group)
		return self._control

	@property
	def initialise(self):
		"""initialise commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_initialise'):
			from .Initialise import InitialiseCls
			self._initialise = InitialiseCls(self._core, self._cmd_group)
		return self._initialise

	@property
	def switch(self):
		"""switch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_switch'):
			from .Switch import SwitchCls
			self._switch = SwitchCls(self._core, self._cmd_group)
		return self._switch

	def clone(self) -> 'GeneratorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GeneratorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
