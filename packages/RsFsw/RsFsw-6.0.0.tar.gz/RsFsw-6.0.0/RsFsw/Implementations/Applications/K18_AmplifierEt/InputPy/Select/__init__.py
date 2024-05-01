from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	@property
	def bbAnalog(self):
		"""bbAnalog commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbAnalog'):
			from .BbAnalog import BbAnalogCls
			self._bbAnalog = BbAnalogCls(self._core, self._cmd_group)
		return self._bbAnalog

	def set(self, signal_source: enums.InputSourceB) -> None:
		"""SCPI: INPut:SELect \n
		Snippet: driver.applications.k18AmplifierEt.inputPy.select.set(signal_source = enums.InputSourceB.FIQ) \n
		Selects the signal source for measurements, i.e. it defines which connector is used to input data to the FSW.
		If no additional input options are installed, only RF input is supported. For FSW85 models with two RF input connectors,
		you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.InputPy.TypePy.set. \n
			:param signal_source: OBB Oscilloscope Baseband signal For details on Oscilloscope Baseband Input see 'Processing Oscilloscope Baseband Input'. Not available for Input2. RF Radio Frequency ('RF INPUT' connector) FIQ I/Q data file (selected by method RsFsw.InputPy.File.Path.set) For details, see 'Basics on Input from I/Q Data Files'. Not available for Input2. DIQ Digital IQ data (only available with optional 'Digital Baseband' interface) For details on I/Q input see 'Digital Input'. Not available for Input2. AIQ Analog Baseband signal (only available with optional 'Analog Baseband' interface) For details on Analog Baseband input, see 'Processing Data From the Analog Baseband Interface'. Not available for Input2.
		"""
		param = Conversions.enum_scalar_to_str(signal_source, enums.InputSourceB)
		self._core.io.write(f'INPut:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.InputSourceB:
		"""SCPI: INPut:SELect \n
		Snippet: value: enums.InputSourceB = driver.applications.k18AmplifierEt.inputPy.select.get() \n
		Selects the signal source for measurements, i.e. it defines which connector is used to input data to the FSW.
		If no additional input options are installed, only RF input is supported. For FSW85 models with two RF input connectors,
		you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.InputPy.TypePy.set. \n
			:return: signal_source: No help available"""
		response = self._core.io.query_str(f'INPut:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.InputSourceB)

	def clone(self) -> 'SelectCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SelectCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
