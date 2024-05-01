from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValueCls:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, source: enums.SourceVsa, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:SOURce[:VALue] \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.source.value.set(source = enums.SourceVsa.BBPower, triggerPort = repcap.TriggerPort.Default) \n
		No command help available \n
			:param source: No help available
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceVsa)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:SOURce:VALue {param}')

	# noinspection PyTypeChecker
	def get(self, triggerPort=repcap.TriggerPort.Default) -> enums.SourceVsa:
		"""SCPI: TRIGger<tp>[:SEQuence]:SOURce[:VALue] \n
		Snippet: value: enums.SourceVsa = driver.applications.k70Vsa.trigger.sequence.source.value.get(triggerPort = repcap.TriggerPort.Default) \n
		No command help available \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: source: No help available"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:SOURce:VALue?')
		return Conversions.str_to_scalar_enum(response, enums.SourceVsa)
