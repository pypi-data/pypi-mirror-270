from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResolutionCls:
	"""Resolution commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resolution", core, parent)

	def set(self, resolution: float) -> None:
		"""SCPI: [SENSe]:IQ:BANDwidth:RESolution \n
		Snippet: driver.applications.iqAnalyzer.sense.iq.bandwidth.resolution.set(resolution = 1.0) \n
		Defines the resolution bandwidth manually if [SENSe:]IQ:BWIDth:MODE is set to MAN. Defines the resolution bandwidth. The
		available RBW values depend on the sample rate and record length. For details see 'Frequency resolution of FFT results -
		RBW'. \n
			:param resolution: refer to specifications document Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(resolution)
		self._core.io.write(f'SENSe:IQ:BANDwidth:RESolution {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:IQ:BANDwidth:RESolution \n
		Snippet: value: float = driver.applications.iqAnalyzer.sense.iq.bandwidth.resolution.get() \n
		Defines the resolution bandwidth manually if [SENSe:]IQ:BWIDth:MODE is set to MAN. Defines the resolution bandwidth. The
		available RBW values depend on the sample rate and record length. For details see 'Frequency resolution of FFT results -
		RBW'. \n
			:return: resolution: No help available"""
		response = self._core.io.query_str(f'SENSe:IQ:BANDwidth:RESolution?')
		return Conversions.str_to_float(response)
