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

	def set(self, level: enums.LowHigh, outputConnector=repcap.OutputConnector.Default, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: OUTPut<up>:TRIGger<tp>:LEVel \n
		Snippet: driver.applications.k10Xlte.output.trigger.level.set(level = enums.LowHigh.HIGH, outputConnector = repcap.OutputConnector.Default, triggerPort = repcap.TriggerPort.Default) \n
		Defines the level of the (TTL compatible) signal generated at the trigger output. Works only if you have selected a
		user-defined output with method RsFsw.Applications.K17_Mcgd.Output.Trigger.Otype.set. \n
			:param level: HIGH 5 V LOW 0 V
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(level, enums.LowHigh)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:TRIGger{triggerPort_cmd_val}:LEVel {param}')

	# noinspection PyTypeChecker
	def get(self, outputConnector=repcap.OutputConnector.Default, triggerPort=repcap.TriggerPort.Default) -> enums.LowHigh:
		"""SCPI: OUTPut<up>:TRIGger<tp>:LEVel \n
		Snippet: value: enums.LowHigh = driver.applications.k10Xlte.output.trigger.level.get(outputConnector = repcap.OutputConnector.Default, triggerPort = repcap.TriggerPort.Default) \n
		Defines the level of the (TTL compatible) signal generated at the trigger output. Works only if you have selected a
		user-defined output with method RsFsw.Applications.K17_Mcgd.Output.Trigger.Otype.set. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: level: HIGH 5 V LOW 0 V"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:TRIGger{triggerPort_cmd_val}:LEVel?')
		return Conversions.str_to_scalar_enum(response, enums.LowHigh)
