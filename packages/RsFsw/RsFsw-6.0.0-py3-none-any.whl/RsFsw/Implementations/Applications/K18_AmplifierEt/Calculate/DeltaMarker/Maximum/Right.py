from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RightCls:
	"""Right commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("right", core, parent)

	def set(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MAXimum:RIGHt \n
		Snippet: driver.applications.k18AmplifierEt.calculate.deltaMarker.maximum.right.set(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Moves a delta marker to the next positive peak value on the trace. The search includes only measurement values to the
		right of the current marker position. In the spectrogram, the command moves a marker horizontally to the maximum level in
		the currently selected frame. The vertical marker position remains the same. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MAXimum:RIGHt', opc_timeout_ms)
