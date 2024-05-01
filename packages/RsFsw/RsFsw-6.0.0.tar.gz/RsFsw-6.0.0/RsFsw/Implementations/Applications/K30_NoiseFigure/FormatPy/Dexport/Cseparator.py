from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CseparatorCls:
	"""Cseparator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cseparator", core, parent)

	def set(self, column_separator: enums.FileSeparator) -> None:
		"""SCPI: FORMat:DEXPort:CSEParator \n
		Snippet: driver.applications.k30NoiseFigure.formatPy.dexport.cseparator.set(column_separator = enums.FileSeparator.COMMa) \n
		Selects the column separator for exported trace data. The selected value is not affected by a preset.
		The command therefore has no reset value. \n
			:param column_separator: COMMa Selects a comma as a separator. SEMicolon Selects a semicolon as a separator. TAB Selects a tabulator as a separator.
		"""
		param = Conversions.enum_scalar_to_str(column_separator, enums.FileSeparator)
		self._core.io.write(f'FORMat:DEXPort:CSEParator {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FileSeparator:
		"""SCPI: FORMat:DEXPort:CSEParator \n
		Snippet: value: enums.FileSeparator = driver.applications.k30NoiseFigure.formatPy.dexport.cseparator.get() \n
		Selects the column separator for exported trace data. The selected value is not affected by a preset.
		The command therefore has no reset value. \n
			:return: column_separator: No help available"""
		response = self._core.io.query_str(f'FORMat:DEXPort:CSEParator?')
		return Conversions.str_to_scalar_enum(response, enums.FileSeparator)
