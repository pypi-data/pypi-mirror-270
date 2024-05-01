from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SmappingCls:
	"""Smapping commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("smapping", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def normalise(self):
		"""normalise commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_normalise'):
			from .Normalise import NormaliseCls
			self._normalise = NormaliseCls(self._core, self._cmd_group)
		return self._normalise

	@property
	def tx(self):
		"""tx commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_tx'):
			from .Tx import TxCls
			self._tx = TxCls(self._core, self._cmd_group)
		return self._tx

	def clone(self) -> 'SmappingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SmappingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
