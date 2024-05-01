from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def p1Db(self):
		"""p1Db commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_p1Db'):
			from .P1Db import P1DbCls
			self._p1Db = P1DbCls(self._core, self._cmd_group)
		return self._p1Db

	@property
	def p3Db(self):
		"""p3Db commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_p3Db'):
			from .P3Db import P3DbCls
			self._p3Db = P3DbCls(self._core, self._cmd_group)
		return self._p3Db

	@property
	def pndb(self):
		"""pndb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pndb'):
			from .Pndb import PndbCls
			self._pndb = PndbCls(self._core, self._cmd_group)
		return self._pndb

	@property
	def cvalue(self):
		"""cvalue commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cvalue'):
			from .Cvalue import CvalueCls
			self._cvalue = CvalueCls(self._core, self._cmd_group)
		return self._cvalue

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
