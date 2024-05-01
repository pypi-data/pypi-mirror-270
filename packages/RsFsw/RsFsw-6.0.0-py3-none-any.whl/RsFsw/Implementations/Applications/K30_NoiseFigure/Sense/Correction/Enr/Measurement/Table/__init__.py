from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TableCls:
	"""Table commands group definition. 7 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import SelectCls
			self._select = SelectCls(self._core, self._cmd_group)
		return self._select

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def temperature(self):
		"""temperature commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_temperature'):
			from .Temperature import TemperatureCls
			self._temperature = TemperatureCls(self._core, self._cmd_group)
		return self._temperature

	def delete(self, table_name: str) -> None:
		"""SCPI: [SENSe]:CORRection:ENR[:MEASurement]:TABLe:DELete \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.enr.measurement.table.delete(table_name = 'abc') \n
		Deletes a temperature table. \n
			:param table_name: String containing the name of the table.
		"""
		param = Conversions.value_to_quoted_str(table_name)
		self._core.io.write(f'SENSe:CORRection:ENR:MEASurement:TABLe:DELete {param}')

	def clone(self) -> 'TableCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TableCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
