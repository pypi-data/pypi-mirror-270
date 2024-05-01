from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XCls:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> List[float]:
		"""SCPI: CALCulate<n>:SNOise<m>:DECades:X \n
		Snippet: value: List[float] = driver.applications.k40PhaseNoise.calculate.snoise.decades.x.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Queries the horizontal poistion of the 10x offset frequency spot noise markers. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Snoise')
			:return: frequencies: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_bin_or_ascii_float_list(f'CALCulate{window_cmd_val}:SNOise{marker_cmd_val}:DECades:X?')
		return response
