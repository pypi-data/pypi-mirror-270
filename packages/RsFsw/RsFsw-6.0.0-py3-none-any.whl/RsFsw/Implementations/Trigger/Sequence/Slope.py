from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlopeCls:
	"""Slope commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slope", core, parent)

	def set(self, slope: enums.SlopeType) -> None:
		"""SCPI: TRIGger[:SEQuence]:SLOPe \n
		Snippet: driver.trigger.sequence.slope.set(slope = enums.SlopeType.NEGative) \n
		For all trigger sources except time, you can define whether triggering occurs when the signal rises to the trigger level
		or falls down to it. \n
			:param slope: POSitive | NEGative POSitive Triggers when the signal rises to the trigger level (rising edge) . NEGative Triggers when the signal drops to the trigger level (falling edge) .
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SlopeType)
		self._core.io.write(f'TRIGger:SEQuence:SLOPe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SlopeType:
		"""SCPI: TRIGger[:SEQuence]:SLOPe \n
		Snippet: value: enums.SlopeType = driver.trigger.sequence.slope.get() \n
		For all trigger sources except time, you can define whether triggering occurs when the signal rises to the trigger level
		or falls down to it. \n
			:return: slope: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)
