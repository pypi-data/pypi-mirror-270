from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def set(self, level: enums.LowHigh, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: OUTPut:TRIGger<tp>:LEVel \n
		Snippet: driver.applications.k6Pulse.output.trigger.level.set(level = enums.LowHigh.HIGH, triggerPort = repcap.TriggerPort.Default) \n
		Defines the level of the (TTL compatible) signal generated at the trigger output. Works only if you have selected a
		user-defined output with method RsFsw.Applications.K17_Mcgd.Output.Trigger.Otype.set. \n
			:param level: HIGH 5 V LOW 0 V
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(level, enums.LowHigh)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'OUTPut:TRIGger{triggerPort_cmd_val}:LEVel {param}')

	# noinspection PyTypeChecker
	def get(self, triggerPort=repcap.TriggerPort.Default) -> enums.LowHigh:
		"""SCPI: OUTPut:TRIGger<tp>:LEVel \n
		Snippet: value: enums.LowHigh = driver.applications.k6Pulse.output.trigger.level.get(triggerPort = repcap.TriggerPort.Default) \n
		Defines the level of the (TTL compatible) signal generated at the trigger output. Works only if you have selected a
		user-defined output with method RsFsw.Applications.K17_Mcgd.Output.Trigger.Otype.set. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: level: HIGH 5 V LOW 0 V"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'OUTPut:TRIGger{triggerPort_cmd_val}:LEVel?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)
