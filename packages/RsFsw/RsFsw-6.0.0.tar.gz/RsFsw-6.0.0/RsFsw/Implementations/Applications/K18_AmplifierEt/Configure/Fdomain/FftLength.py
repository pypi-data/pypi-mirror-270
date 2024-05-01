from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FftLengthCls:
	"""FftLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fftLength", core, parent)

	def set(self, fft_length: float) -> None:
		"""SCPI: CONFigure:FDOMain:FFTLength \n
		Snippet: driver.applications.k18AmplifierEt.configure.fdomain.fftLength.set(fft_length = 1.0) \n
		Defines the number of frequency points determined by each FFT calculation. The more points are used, the higher the
		resolution in the spectrum becomes, but the longer the calculation takes. \n
			:param fft_length: Range: 1k to 32k, Unit: -
		"""
		param = Conversions.decimal_value_to_str(fft_length)
		self._core.io.write(f'CONFigure:FDOMain:FFTLength {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:FDOMain:FFTLength \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.fdomain.fftLength.get() \n
		Defines the number of frequency points determined by each FFT calculation. The more points are used, the higher the
		resolution in the spectrum becomes, but the longer the calculation takes. \n
			:return: fft_length: Range: 1k to 32k, Unit: -"""
		response = self._core.io.query_str(f'CONFigure:FDOMain:FFTLength?')
		return Conversions.str_to_float(response)
