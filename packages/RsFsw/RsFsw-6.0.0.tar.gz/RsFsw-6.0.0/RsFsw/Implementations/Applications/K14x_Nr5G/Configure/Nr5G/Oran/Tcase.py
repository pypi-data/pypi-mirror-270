from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcaseCls:
	"""Tcase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcase", core, parent)

	def set(self, test_case: enums.TestCaseNr5G) -> None:
		"""SCPI: CONFigure[:NR5G]:ORAN:TCASe \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.oran.tcase.set(test_case = enums.TestCaseNr5G.NONE) \n
		Selects an O-RAN test case. \n
			:param test_case: (enum or string) string String containing the name of the test case, e.g. 'TC 3.2.3.1.1'. The string 'NONE' removes a test case.
		"""
		param = Conversions.enum_ext_scalar_to_str(test_case, enums.TestCaseNr5G)
		self._core.io.write(f'CONFigure:NR5G:ORAN:TCASe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TestCaseNr5G:
		"""SCPI: CONFigure[:NR5G]:ORAN:TCASe \n
		Snippet: value: enums.TestCaseNr5G = driver.applications.k14Xnr5G.configure.nr5G.oran.tcase.get() \n
		Selects an O-RAN test case. \n
			:return: test_case: (enum or string) string String containing the name of the test case, e.g. 'TC 3.2.3.1.1'. The string 'NONE' removes a test case."""
		response = self._core.io.query_str(f'CONFigure:NR5G:ORAN:TCASe?')
		return Conversions.str_to_scalar_enum_ext(response, enums.TestCaseNr5G)
