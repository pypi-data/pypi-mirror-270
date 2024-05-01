from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPyCls:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: enums.ScpiRecorderFormat) -> None:
		"""SCPI: SYSTem:SRECorder:FORMat \n
		Snippet: driver.system.srecorder.formatPy.set(format_py = enums.ScpiRecorderFormat.LONG) \n
		Defines whether the commands are recorded using the short or long SCPI notation. \n
			:param format_py: SHORt | LONG SHORt The shortform of the keyword is used. Example: FREQ:CENT LONG The entire keyword is used. Example: FREQuency:CENTer
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.ScpiRecorderFormat)
		self._core.io.write(f'SYSTem:SRECorder:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ScpiRecorderFormat:
		"""SCPI: SYSTem:SRECorder:FORMat \n
		Snippet: value: enums.ScpiRecorderFormat = driver.system.srecorder.formatPy.get() \n
		Defines whether the commands are recorded using the short or long SCPI notation. \n
			:return: format_py: SHORt | LONG SHORt The shortform of the keyword is used. Example: FREQ:CENT LONG The entire keyword is used. Example: FREQuency:CENTer"""
		response = self._core.io.query_str(f'SYSTem:SRECorder:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.ScpiRecorderFormat)
