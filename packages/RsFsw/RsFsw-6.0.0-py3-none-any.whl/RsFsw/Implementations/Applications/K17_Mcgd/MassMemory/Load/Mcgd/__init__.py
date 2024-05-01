from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McgdCls:
	"""Mcgd commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcgd", core, parent)

	@property
	def correctionTable(self):
		"""correctionTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_correctionTable'):
			from .CorrectionTable import CorrectionTableCls
			self._correctionTable = CorrectionTableCls(self._core, self._cmd_group)
		return self._correctionTable

	@property
	def rcalibration(self):
		"""rcalibration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rcalibration'):
			from .Rcalibration import RcalibrationCls
			self._rcalibration = RcalibrationCls(self._core, self._cmd_group)
		return self._rcalibration

	def clone(self) -> 'McgdCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = McgdCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
