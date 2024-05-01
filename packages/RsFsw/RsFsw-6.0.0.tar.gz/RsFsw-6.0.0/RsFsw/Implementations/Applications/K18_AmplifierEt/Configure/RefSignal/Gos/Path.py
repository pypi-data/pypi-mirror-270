from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PathCls:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:PATH \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.path.set(filename = 'abc') \n
		Defines the path to load user-defined reference waveform files to. If you do not specify a path, the file is loaded to
		C:/R_S/INSTR/USER/K18/ReferenceFiles. \n
			:param filename: String containing the path of the file.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'CONFigure:REFSignal:GOS:PATH {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:REFSignal:GOS:PATH \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.refSignal.gos.path.get() \n
		Defines the path to load user-defined reference waveform files to. If you do not specify a path, the file is loaded to
		C:/R_S/INSTR/USER/K18/ReferenceFiles. \n
			:return: filename: String containing the path of the file."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:PATH?')
		return trim_str_response(response)
