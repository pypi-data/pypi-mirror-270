from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WoverlapCls:
	"""Woverlap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("woverlap", core, parent)

	def set(self, window_overlap: float) -> None:
		"""SCPI: CONFigure:FDOMain:WOVerlap \n
		Snippet: driver.applications.k18AmplifierEt.configure.fdomain.woverlap.set(window_overlap = 1.0) \n
		Defines the part of a single FFT window that is re-calculated by the next FFT calculation when using multiple FFT windows. \n
			:param window_overlap: Range: 0 to 99.9, Unit: percent
		"""
		param = Conversions.decimal_value_to_str(window_overlap)
		self._core.io.write(f'CONFigure:FDOMain:WOVerlap {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:FDOMain:WOVerlap \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.fdomain.woverlap.get() \n
		Defines the part of a single FFT window that is re-calculated by the next FFT calculation when using multiple FFT windows. \n
			:return: window_overlap: Range: 0 to 99.9, Unit: percent"""
		response = self._core.io.query_str(f'CONFigure:FDOMain:WOVerlap?')
		return Conversions.str_to_float(response)
