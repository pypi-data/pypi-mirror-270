from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfPowerCls:
	"""IfPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifPower", core, parent)

	def set(self, trigger_level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:IFPower \n
		Snippet: driver.trigger.sequence.level.ifPower.set(trigger_level = 1.0) \n
		Defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event. Note that any
		RF attenuation or preamplification is considered when the trigger level is analyzed. If defined, a reference level offset
		is also considered. For compatibility reasons, this command is also available for the 'Baseband Power' trigger source
		when using the 'Analog Baseband' interface. \n
			:param trigger_level: For details on available trigger levels and trigger bandwidths, see the specifications document. Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(trigger_level)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:IFPower {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel:IFPower \n
		Snippet: value: float = driver.trigger.sequence.level.ifPower.get() \n
		Defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event. Note that any
		RF attenuation or preamplification is considered when the trigger level is analyzed. If defined, a reference level offset
		is also considered. For compatibility reasons, this command is also available for the 'Baseband Power' trigger source
		when using the 'Analog Baseband' interface. \n
			:return: trigger_level: For details on available trigger levels and trigger bandwidths, see the specifications document. Unit: DBM"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:IFPower?')
		return Conversions.str_to_float(response)
