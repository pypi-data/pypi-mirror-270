from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RelativeCls:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> int:
		"""SCPI: CALCulate<n>:DELTamarker<m>:X:RELative \n
		Snippet: value: int = driver.applications.k70Vsa.calculate.deltaMarker.x.relative.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Queries the relative position of a delta marker on the x-axis. If necessary, the command activates the delta marker first. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: position: Position of the delta marker in relation to the reference marker."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:X:RELative?')
		return Conversions.str_to_int(response)
