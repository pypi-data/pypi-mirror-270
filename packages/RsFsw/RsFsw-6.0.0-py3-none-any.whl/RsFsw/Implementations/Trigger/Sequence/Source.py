from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, source: enums.TriggerSeqSource) -> None:
		"""SCPI: TRIGger[:SEQuence]:SOURce \n
		Snippet: driver.trigger.sequence.source.set(source = enums.TriggerSeqSource.ACVideo) \n
		Selects the trigger source. For triggering with AF, AM, AMRelative, FM, and PM trigger sources to be successful, the
		measurement time must cover at least 5 periods of the audio signal. For details on trigger sources, see 'Trigger Source'.
		Note on external triggers: If a measurement is configured to wait for an external trigger signal in a remote control
		program, remote control is blocked until the trigger is received and the program can continue. Make sure that this
		situation is avoided in your remote control programs. \n
			:param source: IMMediate Free Run EXTernal Trigger signal from the 'Trigger Input' connector. If the optional 2 GHz bandwidth extension (B2000/B5000) is installed and active, this parameter activates the 'Ch3' input connector on the oscilloscope. Then the FSW triggers when the signal fed into the 'Ch3' input connector on the oscilloscope meets or exceeds the specified trigger level. Note: In previous firmware versions, the external trigger was connected to the 'Ch2' input on the oscilloscope. As of firmware version FSW 2.30, the 'Ch3' input on the oscilloscope must be used! If power splitter mode is active, this parameter activates the 'EXT TRIGGER INPUT' connector on the oscilloscope. Then the FSW triggers when the signal fed into the 'EXT TRIGGER INPUT' connector on the oscilloscope meets or exceeds the specified trigger level. EXT2 Trigger signal from the 'Trigger Input/Output' connector. For FSW85 models, Trigger 2 is not available due to the second RF input connector on the front panel. The trigger signal is taken from the 'Trigger Input/Output' connector on the rear panel. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'TRIGGER 3 INPUT/ OUTPUT' connector. Note: Connector must be configured for 'Input'. RFPower First intermediate frequency (Frequency and time domain measurements only.) Not available for input from the optional 'Analog Baseband' interface. Not available for input from the optional 'Digital Baseband' interface. IFPower Second intermediate frequency Not available for input from the optional 'Digital Baseband' interface. For input from the optional 'Analog Baseband' interface, this parameter is interpreted as BBPower for compatibility reasons. IQPower Magnitude of sampled I/Q data For applications that process I/Q data, such as the I/Q Analyzer or optional applications. Not available for input from the optional 'Digital Baseband' interface. TIME Time interval BBPower Baseband power For input from the optional 'Analog Baseband' interface. For input from the optional 'Digital Baseband' interface. PSEN External power sensor AF AF power signal FM FM power signal AM corresponds to the RF power signal AMRelative corresponds to the AM signal PM PM power signal GP0 | GP1 | GP2 | GP3 | GP4 | GP5 For applications that process I/Q data, such as the I/Q Analyzer or optional applications, and only if the optional 'Digital Baseband' interface is available. Defines triggering of the measurement directly via the LVDS connector. The parameter specifies which general-purpose bit (0 to 5) provides the trigger data. The assignment of the general-purpose bits used by the Digital IQ trigger to the LVDS connector pins is provided in 'Digital I/Q'.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSeqSource)
		self._core.io.write(f'TRIGger:SEQuence:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TriggerSeqSource:
		"""SCPI: TRIGger[:SEQuence]:SOURce \n
		Snippet: value: enums.TriggerSeqSource = driver.trigger.sequence.source.get() \n
		Selects the trigger source. For triggering with AF, AM, AMRelative, FM, and PM trigger sources to be successful, the
		measurement time must cover at least 5 periods of the audio signal. For details on trigger sources, see 'Trigger Source'.
		Note on external triggers: If a measurement is configured to wait for an external trigger signal in a remote control
		program, remote control is blocked until the trigger is received and the program can continue. Make sure that this
		situation is avoided in your remote control programs. \n
			:return: source: IMMediate Free Run EXTernal Trigger signal from the 'Trigger Input' connector. If the optional 2 GHz bandwidth extension (B2000/B5000) is installed and active, this parameter activates the 'Ch3' input connector on the oscilloscope. Then the FSW triggers when the signal fed into the 'Ch3' input connector on the oscilloscope meets or exceeds the specified trigger level. Note: In previous firmware versions, the external trigger was connected to the 'Ch2' input on the oscilloscope. As of firmware version FSW 2.30, the 'Ch3' input on the oscilloscope must be used! If power splitter mode is active, this parameter activates the 'EXT TRIGGER INPUT' connector on the oscilloscope. Then the FSW triggers when the signal fed into the 'EXT TRIGGER INPUT' connector on the oscilloscope meets or exceeds the specified trigger level. EXT2 Trigger signal from the 'Trigger Input/Output' connector. For FSW85 models, Trigger 2 is not available due to the second RF input connector on the front panel. The trigger signal is taken from the 'Trigger Input/Output' connector on the rear panel. Note: Connector must be configured for 'Input'. EXT3 Trigger signal from the 'TRIGGER 3 INPUT/ OUTPUT' connector. Note: Connector must be configured for 'Input'. RFPower First intermediate frequency (Frequency and time domain measurements only.) Not available for input from the optional 'Analog Baseband' interface. Not available for input from the optional 'Digital Baseband' interface. IFPower Second intermediate frequency Not available for input from the optional 'Digital Baseband' interface. For input from the optional 'Analog Baseband' interface, this parameter is interpreted as BBPower for compatibility reasons. IQPower Magnitude of sampled I/Q data For applications that process I/Q data, such as the I/Q Analyzer or optional applications. Not available for input from the optional 'Digital Baseband' interface. TIME Time interval BBPower Baseband power For input from the optional 'Analog Baseband' interface. For input from the optional 'Digital Baseband' interface. PSEN External power sensor AF AF power signal FM FM power signal AM corresponds to the RF power signal AMRelative corresponds to the AM signal PM PM power signal GP0 | GP1 | GP2 | GP3 | GP4 | GP5 For applications that process I/Q data, such as the I/Q Analyzer or optional applications, and only if the optional 'Digital Baseband' interface is available. Defines triggering of the measurement directly via the LVDS connector. The parameter specifies which general-purpose bit (0 to 5) provides the trigger data. The assignment of the general-purpose bits used by the Digital IQ trigger to the LVDS connector pins is provided in 'Digital I/Q'."""
		response = self._core.io.query_str(f'TRIGger:SEQuence:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSeqSource)
