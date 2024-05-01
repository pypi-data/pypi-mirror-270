from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRateCls:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, sample_rate: float) -> None:
		"""SCPI: [SENSe]:SRATe \n
		Snippet: driver.applications.k149Uwb.sense.symbolRate.set(sample_rate = 1.0) \n
		Defines the sample rate for the current measurement. Note that the sample rate and the measurement bandwidth are
		interdependent (see [SENSe:]BWIDth:DEMod) . For information on supported sample rates and bandwidths see the
		specifications document. \n
			:param sample_rate: Range: 100 Hz to depends on installed options, Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'SENSe:SRATe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SRATe \n
		Snippet: value: float = driver.applications.k149Uwb.sense.symbolRate.get() \n
		Defines the sample rate for the current measurement. Note that the sample rate and the measurement bandwidth are
		interdependent (see [SENSe:]BWIDth:DEMod) . For information on supported sample rates and bandwidths see the
		specifications document. \n
			:return: sample_rate: Range: 100 Hz to depends on installed options, Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:SRATe?')
		return Conversions.str_to_float(response)
