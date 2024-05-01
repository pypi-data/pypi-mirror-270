from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReferenceCls:
	"""Reference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def set(self, reference: enums.FreqReference, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:HOPDetection:FREQuency:REFerence \n
		Snippet: driver.applications.k60Transient.calculate.hopDetection.frequency.reference.set(reference = enums.FreqReference.CENTer, window = repcap.Window.Default) \n
		Defines the reference point for positioning the frequency measurement range. For details on the measurement range
		parameters see 'Measurement range'. \n
			:param reference: CENTer | EDGE EDGE The measurement range is defined in reference to the hop's rising or falling edge (see method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Frequency.Offset.Begin.set and method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Frequency.Offset.End.set) . CENTer The measurement range is defined in reference to the center of the hop. FMSettling The measurement range starts at the FM settling point (see [SENSe:]HOP:FMSettling:FMSPoint?) . PMSettling The measurement range starts at the PM settling point (see [SENSe:]HOP:PMSettling:PMSPoint?) .
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(reference, enums.FreqReference)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:HOPDetection:FREQuency:REFerence {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.FreqReference:
		"""SCPI: CALCulate<n>:HOPDetection:FREQuency:REFerence \n
		Snippet: value: enums.FreqReference = driver.applications.k60Transient.calculate.hopDetection.frequency.reference.get(window = repcap.Window.Default) \n
		Defines the reference point for positioning the frequency measurement range. For details on the measurement range
		parameters see 'Measurement range'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: reference: CENTer | EDGE EDGE The measurement range is defined in reference to the hop's rising or falling edge (see method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Frequency.Offset.Begin.set and method RsFsw.Applications.K60_Transient.Calculate.HopDetection.Frequency.Offset.End.set) . CENTer The measurement range is defined in reference to the center of the hop. FMSettling The measurement range starts at the FM settling point (see [SENSe:]HOP:FMSettling:FMSPoint?) . PMSettling The measurement range starts at the PM settling point (see [SENSe:]HOP:PMSettling:PMSPoint?) ."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:HOPDetection:FREQuency:REFerence?')
		return Conversions.str_to_scalar_enum(response, enums.FreqReference)
