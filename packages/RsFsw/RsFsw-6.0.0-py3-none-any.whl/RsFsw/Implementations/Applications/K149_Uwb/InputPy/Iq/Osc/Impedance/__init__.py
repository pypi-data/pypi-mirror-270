from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImpedanceCls:
	"""Impedance commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impedance", core, parent)

	@property
	def ptype(self):
		"""ptype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptype'):
			from .Ptype import PtypeCls
			self._ptype = PtypeCls(self._core, self._cmd_group)
		return self._ptype

	def set(self, impedance: float) -> None:
		"""SCPI: INPut:IQ:OSC:IMPedance \n
		Snippet: driver.applications.k149Uwb.inputPy.iq.osc.impedance.set(impedance = 1.0) \n
		Selects the nominal input impedance of the analog baseband input. The command is not available for measurements with the
		optional 'Digital Baseband' interface. For input from the RF input, use the method RsFsw.Applications.K10x_Lte.InputPy.
		Impedance.set command. For analog baseband input without an oscilloscope, use the method RsFsw.InputPy.Iq.Impedance.
		set command. \n
			:param impedance: 50 | 75 numeric value User-defined impedance from 50 Ohm to 100000000 Ohm (=100 MOhm) User-defined values are only available for the Spectrum application, the I/Q Analyzer (and thus MSRA mode, primary application only) and the optional Docsis 3.1 application. Unit: Ohm
		"""
		param = Conversions.decimal_value_to_str(impedance)
		self._core.io.write(f'INPut:IQ:OSC:IMPedance {param}')

	def get(self) -> float:
		"""SCPI: INPut:IQ:OSC:IMPedance \n
		Snippet: value: float = driver.applications.k149Uwb.inputPy.iq.osc.impedance.get() \n
		Selects the nominal input impedance of the analog baseband input. The command is not available for measurements with the
		optional 'Digital Baseband' interface. For input from the RF input, use the method RsFsw.Applications.K10x_Lte.InputPy.
		Impedance.set command. For analog baseband input without an oscilloscope, use the method RsFsw.InputPy.Iq.Impedance.
		set command. \n
			:return: impedance: 50 | 75 numeric value User-defined impedance from 50 Ohm to 100000000 Ohm (=100 MOhm) User-defined values are only available for the Spectrum application, the I/Q Analyzer (and thus MSRA mode, primary application only) and the optional Docsis 3.1 application. Unit: Ohm"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:IMPedance?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'ImpedanceCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ImpedanceCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
