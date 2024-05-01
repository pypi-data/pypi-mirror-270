from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HeaderCls:
	"""Header commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("header", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: FORMat:DEXPort:HEADer \n
		Snippet: driver.formatPy.dexport.header.set(state = False) \n
		If enabled, additional instrument and measurement settings are included in the header of the export file for result data.
		If disabled, only the pure result data from the selected traces and tables is exported. See 'Reference: ASCII file export
		format' for details. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'FORMat:DEXPort:HEADer {param}')

	def get(self) -> bool:
		"""SCPI: FORMat:DEXPort:HEADer \n
		Snippet: value: bool = driver.formatPy.dexport.header.get() \n
		If enabled, additional instrument and measurement settings are included in the header of the export file for result data.
		If disabled, only the pure result data from the selected traces and tables is exported. See 'Reference: ASCII file export
		format' for details. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'FORMat:DEXPort:HEADer?')
		return Conversions.str_to_bool(response)
