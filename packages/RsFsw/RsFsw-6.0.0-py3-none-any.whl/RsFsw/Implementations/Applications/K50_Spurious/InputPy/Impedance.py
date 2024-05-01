from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImpedanceCls:
	"""Impedance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impedance", core, parent)

	def set(self, impedance: int) -> None:
		"""SCPI: INPut:IMPedance \n
		Snippet: driver.applications.k50Spurious.inputPy.impedance.set(impedance = 1) \n
		Selects the nominal input impedance of the RF input. In some applications, only 50 Ohm are supported. For input from the
		'Analog Baseband' interface, use the method RsFsw.InputPy.Iq.Impedance.set command. \n
			:param impedance: 50 | 75 numeric value User-defined impedance from 50 Ohm to 100000000 Ohm (=100 MOhm) User-defined values are only available for the Spectrum application, the I/Q Analyzer, and some optional applications. (In MSRA mode, primary only) Unit: OHM
		"""
		param = Conversions.decimal_value_to_str(impedance)
		self._core.io.write(f'INPut:IMPedance {param}')

	def get(self) -> int:
		"""SCPI: INPut:IMPedance \n
		Snippet: value: int = driver.applications.k50Spurious.inputPy.impedance.get() \n
		Selects the nominal input impedance of the RF input. In some applications, only 50 Ohm are supported. For input from the
		'Analog Baseband' interface, use the method RsFsw.InputPy.Iq.Impedance.set command. \n
			:return: impedance: 50 | 75 numeric value User-defined impedance from 50 Ohm to 100000000 Ohm (=100 MOhm) User-defined values are only available for the Spectrum application, the I/Q Analyzer, and some optional applications. (In MSRA mode, primary only) Unit: OHM"""
		response = self._core.io.query_str(f'INPut:IMPedance?')
		return Conversions.str_to_int(response)
