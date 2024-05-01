from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WlfRatioCls:
	"""WlfRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wlfRatio", core, parent)

	def set(self, wlength_ratio: float) -> None:
		"""SCPI: CONFigure:FDOMain:WLFRatio \n
		Snippet: driver.applications.k18AmplifierEt.configure.fdomain.wlfRatio.set(wlength_ratio = 1.0) \n
		Defines the window length as a percentage of the FFT length (see method RsFsw.Applications.K18_AmplifierEt.Configure.
		Fdomain.FftLength.set) . \n
			:param wlength_ratio: Range: 0.1 to 100, Unit: percent
		"""
		param = Conversions.decimal_value_to_str(wlength_ratio)
		self._core.io.write(f'CONFigure:FDOMain:WLFRatio {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:FDOMain:WLFRatio \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.fdomain.wlfRatio.get() \n
		Defines the window length as a percentage of the FFT length (see method RsFsw.Applications.K18_AmplifierEt.Configure.
		Fdomain.FftLength.set) . \n
			:return: wlength_ratio: Range: 0.1 to 100, Unit: percent"""
		response = self._core.io.query_str(f'CONFigure:FDOMain:WLFRatio?')
		return Conversions.str_to_float(response)
