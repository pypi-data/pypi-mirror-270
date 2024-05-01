from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CouplingCls:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def set(self, coupling: enums.CouplingTypeB) -> None:
		"""SCPI: INPut:IQ:OSC:COUPling \n
		Snippet: driver.inputPy.iq.osc.coupling.set(coupling = enums.CouplingTypeB.AC) \n
		Determines the coupling of the oscilloscope to the FSW. \n
			:param coupling: DC | DCLimit | AC DC DC coupling shows all parts of an input signal. DC 50 Ohm coupling is the default for 50Ohm input impedance to connect, for example, active probes. DCLimit DC coupling with 1 M Ohm input impedance to connect standard passive probes. AC AC coupling is useful if the DC component of a signal is of no interest. AC coupling blocks the DC component of the signal so that the waveform is centered on zero volts.
		"""
		param = Conversions.enum_scalar_to_str(coupling, enums.CouplingTypeB)
		self._core.io.write(f'INPut:IQ:OSC:COUPling {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CouplingTypeB:
		"""SCPI: INPut:IQ:OSC:COUPling \n
		Snippet: value: enums.CouplingTypeB = driver.inputPy.iq.osc.coupling.get() \n
		Determines the coupling of the oscilloscope to the FSW. \n
			:return: coupling: DC | DCLimit | AC DC DC coupling shows all parts of an input signal. DC 50 Ohm coupling is the default for 50Ohm input impedance to connect, for example, active probes. DCLimit DC coupling with 1 M Ohm input impedance to connect standard passive probes. AC AC coupling is useful if the DC component of a signal is of no interest. AC coupling blocks the DC component of the signal so that the waveform is centered on zero volts."""
		response = self._core.io.query_str(f'INPut:IQ:OSC:COUPling?')
		return Conversions.str_to_scalar_enum(response, enums.CouplingTypeB)
