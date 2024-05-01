from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeleteCls:
	"""Delete commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delete", core, parent)

	def set(self, standard: str, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:STANdard:DELete \n
		Snippet: driver.applications.k14Xnr5G.calculate.marker.function.power.standard.delete.set(standard = 'abc', window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Deletes a file containing an ACLR standard. \n
			:param standard: String containing the file name of the standard.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.value_to_quoted_str(standard)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:STANdard:DELete {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> str:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:STANdard:DELete \n
		Snippet: value: str = driver.applications.k14Xnr5G.calculate.marker.function.power.standard.delete.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Deletes a file containing an ACLR standard. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: standard: String containing the file name of the standard."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:STANdard:DELete?')
		return trim_str_response(response)
