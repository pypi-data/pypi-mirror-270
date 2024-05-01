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
		"""SCPI: INPut:IQ:OSC:SRATe \n
		Snippet: driver.inputPy.iq.osc.symbolRate.set(sample_rate = 1.0) \n
		Returns the used oscilloscope acquisition sample rate, which depends on the used I/Q mode (see method RsFsw.Applications.
		K149_Uwb.InputPy.Iq.Osc.TypePy.set) . \n
			:param sample_rate: 10 GHz | 20 GHz 10 GHz differential mode 20 GHz single-ended mode Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'INPut:IQ:OSC:SRATe {param}')

	def get(self) -> float:
		"""SCPI: INPut:IQ:OSC:SRATe \n
		Snippet: value: float = driver.inputPy.iq.osc.symbolRate.get() \n
		Returns the used oscilloscope acquisition sample rate, which depends on the used I/Q mode (see method RsFsw.Applications.
		K149_Uwb.InputPy.Iq.Osc.TypePy.set) . \n
			:return: sample_rate: 10 GHz | 20 GHz 10 GHz differential mode 20 GHz single-ended mode Unit: Hz"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:SRATe?')
		return Conversions.str_to_float(response)
