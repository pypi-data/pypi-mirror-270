from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.ReferenceSourceD, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:SOURce \n
		Snippet: driver.applications.k30NoiseFigure.trigger.sequence.source.set(source = enums.ReferenceSourceD.EXT2, triggerPort = repcap.TriggerPort.Default) \n
		Selects the trigger source. Note on external triggers: If a measurement is configured to wait for an external trigger
		signal in a remote control program, remote control is blocked until the trigger is received and the program can continue.
		Make sure this situation is avoided in your remote control programs. \n
			:param source: IMMediate Free run (no trigger event to start a measurement) . EXTernal Measurement starts when the external trigger signal exceeds a certain level. Trigger signal from the 'Trigger In' connector. EXT2 Trigger signal from the 'Trigger Input / Output' connector. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'Trigger 3 Input / Output' connector. Note: Connector must be configured for 'Input'. RFPower Measurement starts when the first intermediate frequency exceeds a certain level. (Frequency and time domain measurements only.) Not available for input from the optional Digital Baseband Interface or the optional analog baseband Interface. IFPower Measurement starts when the second intermediate frequency exceeds a certain level. Not available for input from the optional digital baseband interface. For input from the optional analog baseband interface, this parameter is interpreted as BBPower for compatibility reasons. IQPower Measurement starts when the sampled I/Q data exceeds a certain magnitude. For applications that process I/Q data, such as the I/Q analyzer or optional applications. BBPower Measurement starts when the baseband power exceeds a certain level. For digital input via the optional digital baseband interface or the optional analog baseband interface. PSEN External power sensor GP0 | GP1 | GP2 | GP3 | GP4 | GP5 For applications that process I/Q data, such as the I/Q analyzer or optional applications, and only if the optional digital baseband interface is available. Defines triggering of the measurement directly via the LVDS connector. The parameter specifies which general purpose bit (0 to 5) will provide the trigger data. TUNit If activated, the measurement is triggered by a connected R&S FS-Z11 trigger unit, simultaneously for all connected analyzers.
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ReferenceSourceD)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, triggerPort=repcap.TriggerPort.Default) -> enums.ReferenceSourceD:
		"""SCPI: TRIGger<tp>[:SEQuence]:SOURce \n
		Snippet: value: enums.ReferenceSourceD = driver.applications.k30NoiseFigure.trigger.sequence.source.get(triggerPort = repcap.TriggerPort.Default) \n
		Selects the trigger source. Note on external triggers: If a measurement is configured to wait for an external trigger
		signal in a remote control program, remote control is blocked until the trigger is received and the program can continue.
		Make sure this situation is avoided in your remote control programs. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: source: IMMediate Free run (no trigger event to start a measurement) . EXTernal Measurement starts when the external trigger signal exceeds a certain level. Trigger signal from the 'Trigger In' connector. EXT2 Trigger signal from the 'Trigger Input / Output' connector. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'Trigger 3 Input / Output' connector. Note: Connector must be configured for 'Input'. RFPower Measurement starts when the first intermediate frequency exceeds a certain level. (Frequency and time domain measurements only.) Not available for input from the optional Digital Baseband Interface or the optional analog baseband Interface. IFPower Measurement starts when the second intermediate frequency exceeds a certain level. Not available for input from the optional digital baseband interface. For input from the optional analog baseband interface, this parameter is interpreted as BBPower for compatibility reasons. IQPower Measurement starts when the sampled I/Q data exceeds a certain magnitude. For applications that process I/Q data, such as the I/Q analyzer or optional applications. BBPower Measurement starts when the baseband power exceeds a certain level. For digital input via the optional digital baseband interface or the optional analog baseband interface. PSEN External power sensor GP0 | GP1 | GP2 | GP3 | GP4 | GP5 For applications that process I/Q data, such as the I/Q analyzer or optional applications, and only if the optional digital baseband interface is available. Defines triggering of the measurement directly via the LVDS connector. The parameter specifies which general purpose bit (0 to 5) will provide the trigger data. TUNit If activated, the measurement is triggered by a connected R&S FS-Z11 trigger unit, simultaneously for all connected analyzers."""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceSourceD)
