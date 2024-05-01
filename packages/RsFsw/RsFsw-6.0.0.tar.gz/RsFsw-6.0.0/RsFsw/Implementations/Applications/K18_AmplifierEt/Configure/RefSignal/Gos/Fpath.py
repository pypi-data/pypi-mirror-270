from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FpathCls:
	"""Fpath commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fpath", core, parent)

	def set(self, file_path: str) -> None:
		"""SCPI: CONFigure:REFSignal:GOS:FPATh \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.gos.fpath.set(file_path = 'abc') \n
		Defines the name and path of the user-defined reference waveform file when loaded to the analyzer. \n
			:param file_path: String containing the path and name of the file.
		"""
		param = Conversions.value_to_quoted_str(file_path)
		self._core.io.write(f'CONFigure:REFSignal:GOS:FPATh {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:REFSignal:GOS:FPATh \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.refSignal.gos.fpath.get() \n
		Defines the name and path of the user-defined reference waveform file when loaded to the analyzer. \n
			:return: file_path: String containing the path and name of the file."""
		response = self._core.io.query_str(f'CONFigure:REFSignal:GOS:FPATh?')
		return trim_str_response(response)
