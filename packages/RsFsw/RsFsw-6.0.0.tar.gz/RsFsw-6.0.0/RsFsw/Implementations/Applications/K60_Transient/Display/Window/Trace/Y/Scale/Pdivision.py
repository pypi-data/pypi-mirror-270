from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdivisionCls:
	"""Pdivision commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdivision", core, parent)

	def set(self, value: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:PDIVision \n
		Snippet: driver.applications.k60Transient.display.window.trace.y.scale.pdivision.set(value = 1.0, window = repcap.Window.Default) \n
		Determines the values shown for each division on the x-axis or y-axis in the specified window. One or more multiples of
		10n can be selected. The R&S FSW WLAN application then selects the optimal scaling from the selected values. For details
		see 'Scaling per division'. \n
			:param value: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(value)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:PDIVision {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe:Y[:SCALe]:PDIVision \n
		Snippet: value: float = driver.applications.k60Transient.display.window.trace.y.scale.pdivision.get(window = repcap.Window.Default) \n
		Determines the values shown for each division on the x-axis or y-axis in the specified window. One or more multiples of
		10n can be selected. The R&S FSW WLAN application then selects the optimal scaling from the selected values. For details
		see 'Scaling per division'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: value: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe:Y:SCALe:PDIVision?')
		return Conversions.str_to_float(response)
