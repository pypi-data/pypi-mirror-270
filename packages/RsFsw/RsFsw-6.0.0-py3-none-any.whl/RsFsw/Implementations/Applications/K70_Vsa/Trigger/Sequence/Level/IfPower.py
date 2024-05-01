from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfPowerCls:
	"""IfPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifPower", core, parent)

	def set(self, level_if_power: float, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:LEVel:IFPower \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.level.ifPower.set(level_if_power = 1.0, triggerPort = repcap.TriggerPort.Default) \n
		Defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event. Note that any
		RF attenuation or preamplification is considered when the trigger level is analyzed. If defined, a reference level offset
		is also considered. \n
			:param level_if_power: No help available
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.decimal_value_to_str(level_if_power)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:LEVel:IFPower {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default) -> float:
		"""SCPI: TRIGger<tp>[:SEQuence]:LEVel:IFPower \n
		Snippet: value: float = driver.applications.k70Vsa.trigger.sequence.level.ifPower.get(triggerPort = repcap.TriggerPort.Default) \n
		Defines the power level at the third intermediate frequency that must be exceeded to cause a trigger event. Note that any
		RF attenuation or preamplification is considered when the trigger level is analyzed. If defined, a reference level offset
		is also considered. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: level_if_power: No help available"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:LEVel:IFPower?')
		return Conversions.str_to_float(response)
