from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PtypeCls:
	"""Ptype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptype", core, parent)

	def set(self, pad_type: enums.PadType) -> None:
		"""SCPI: INPut:IMPedance:PTYPe \n
		Snippet: driver.inputPy.impedance.ptype.set(pad_type = enums.PadType.MLPad) \n
		Defines the type of matching pad used for impedance conversion for RF input. For input from the 'Analog Baseband'
		interface, use the method RsFsw.InputPy.Iq.Impedance.Ptype.set command. \n
			:param pad_type: SRESistor | MLPad SRESistor Series-R MLPad Minimum Loss Pad
		"""
		param = Conversions.enum_scalar_to_str(pad_type, enums.PadType)
		self._core.io.write(f'INPut:IMPedance:PTYPe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PadType:
		"""SCPI: INPut:IMPedance:PTYPe \n
		Snippet: value: enums.PadType = driver.inputPy.impedance.ptype.get() \n
		Defines the type of matching pad used for impedance conversion for RF input. For input from the 'Analog Baseband'
		interface, use the method RsFsw.InputPy.Iq.Impedance.Ptype.set command. \n
			:return: pad_type: SRESistor | MLPad SRESistor Series-R MLPad Minimum Loss Pad"""
		response = self._core.io.query_str(f'INPut:IMPedance:PTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.PadType)
