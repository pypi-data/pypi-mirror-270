from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SlopeCls:
	"""Slope commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slope", core, parent)

	def set(self, edge: enums.SlopeType, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:SLOPe \n
		Snippet: driver.applications.k10Xlte.sense.pmeter.trigger.slope.set(edge = enums.SlopeType.NEGative, powerMeter = repcap.PowerMeter.Default) \n
		Selects the trigger condition for external power triggers. \n
			:param edge: POSitive The measurement starts in case the trigger signal shows a positive edge. NEGative The measurement starts in case the trigger signal shows a negative edge.
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.enum_scalar_to_str(edge, enums.SlopeType)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:SLOPe {param}')

	# noinspection PyTypeChecker
	def get(self, powerMeter=repcap.PowerMeter.Default) -> enums.SlopeType:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:SLOPe \n
		Snippet: value: enums.SlopeType = driver.applications.k10Xlte.sense.pmeter.trigger.slope.get(powerMeter = repcap.PowerMeter.Default) \n
		Selects the trigger condition for external power triggers. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: edge: POSitive The measurement starts in case the trigger signal shows a positive edge. NEGative The measurement starts in case the trigger signal shows a negative edge."""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)
