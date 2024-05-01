from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRateCls:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, count: int) -> None:
		"""SCPI: TRACe:IQ:SRATe \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.symbolRate.set(count = 1) \n
		Sets the final user sample rate for the acquired I/Q data. Thus, the user sample rate can be modified without affecting
		the actual data capturing settings on the FSW. Note: The smaller the user sample rate, the smaller the usable I/Q
		bandwidth, see 'Sample rate and maximum usable I/Q bandwidth for RF input'. In order to ensure a minimum usable I/Q
		bandwidth use the method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.Mbwidth.set command. \n
			:param count: The valid sample rates are described in 'Sample rate and maximum usable I/Q bandwidth for RF input'. Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'TRACe:IQ:SRATe {param}')

	def get(self) -> int:
		"""SCPI: TRACe:IQ:SRATe \n
		Snippet: value: int = driver.applications.iqAnalyzer.trace.iq.symbolRate.get() \n
		Sets the final user sample rate for the acquired I/Q data. Thus, the user sample rate can be modified without affecting
		the actual data capturing settings on the FSW. Note: The smaller the user sample rate, the smaller the usable I/Q
		bandwidth, see 'Sample rate and maximum usable I/Q bandwidth for RF input'. In order to ensure a minimum usable I/Q
		bandwidth use the method RsFsw.Applications.K17_Mcgd.Trace.Iq.Wband.Mbwidth.set command. \n
			:return: count: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:SRATe?')
		return Conversions.str_to_int(response)
