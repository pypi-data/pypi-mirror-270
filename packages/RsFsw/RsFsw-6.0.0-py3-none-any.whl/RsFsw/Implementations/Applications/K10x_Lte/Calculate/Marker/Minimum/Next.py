from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NextCls:
	"""Next commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("next", core, parent)

	def set(self, window=repcap.Window.Default, marker=repcap.Marker.Default, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:MINimum:NEXT \n
		Snippet: driver.applications.k10Xlte.calculate.marker.minimum.next.set(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Moves a marker to the next minimum peak value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:MINimum:NEXT', opc_timeout_ms)
