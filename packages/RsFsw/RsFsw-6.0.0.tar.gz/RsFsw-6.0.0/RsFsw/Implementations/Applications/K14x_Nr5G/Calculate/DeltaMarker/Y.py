from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class YCls:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> float:
		"""SCPI: CALCulate<n>:DELTamarker<m>:Y \n
		Snippet: value: float = driver.applications.k14Xnr5G.calculate.deltaMarker.y.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Queries the relative position of a delta marker on the y-axis. If necessary, the command activates the delta marker first.
		To get a valid result, you have to perform a complete measurement with synchronization to the end of the measurement
		before reading out the result. This is only possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.
		Initiate.Continuous.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: result: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:Y?')
		return Conversions.str_to_float(response)
