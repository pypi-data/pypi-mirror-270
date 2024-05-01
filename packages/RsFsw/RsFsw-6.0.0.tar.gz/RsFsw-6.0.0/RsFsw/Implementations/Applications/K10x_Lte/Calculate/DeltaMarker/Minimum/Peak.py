from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeakCls:
	"""Peak commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peak", core, parent)

	def set(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MINimum[:PEAK] \n
		Snippet: driver.applications.k10Xlte.calculate.deltaMarker.minimum.peak.set(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Moves a delta marker to the minimum level. If the marker is not yet active, the command first activates the marker. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MINimum:PEAK', opc_timeout_ms)
