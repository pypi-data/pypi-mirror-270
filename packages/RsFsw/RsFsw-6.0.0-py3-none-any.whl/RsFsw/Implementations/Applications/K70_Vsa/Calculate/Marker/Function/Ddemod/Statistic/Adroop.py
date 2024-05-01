from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdroopCls:
	"""Adroop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("adroop", core, parent)

	def get(self, result_type: enums.ResultTypeStat, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:DDEMod:STATistic:ADRoop \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.marker.function.ddemod.statistic.adroop.get(result_type = enums.ResultTypeStat.AVG, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Queries the results of the amplitude droop error measurement performed for digital demodulation. The output values are
		the same as those provided in the 'Modulation Accuracy' table (see 'Result summary') . \n
			:param result_type: none Amplitude droop in dB/symbol (for current sweep) AVG Amplitude droop in dB/symbol, evaluating the linear average value over several sweeps RPE Peak value for amplitude droop over several sweeps SDEV Standard deviation of amplitude droop PCTL 95 percentile value of amplitude droop
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: result: No help available"""
		param = Conversions.enum_scalar_to_str(result_type, enums.ResultTypeStat)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:DDEMod:STATistic:ADRoop? {param}')
		return Conversions.str_to_float(response)
