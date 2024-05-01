from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MreferenceCls:
	"""Mreference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mreference", core, parent)

	def set(self, ref_marker: int, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MREFerence \n
		Snippet: driver.applications.k18AmplifierEt.calculate.deltaMarker.mreference.set(ref_marker = 1, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Selects a reference marker for a delta marker other than marker 1. The reference may be another marker or the fixed
		reference. \n
			:param ref_marker: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.decimal_value_to_str(ref_marker)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MREFerence {param}')

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> int:
		"""SCPI: CALCulate<n>:DELTamarker<m>:MREFerence \n
		Snippet: value: int = driver.applications.k18AmplifierEt.calculate.deltaMarker.mreference.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Selects a reference marker for a delta marker other than marker 1. The reference may be another marker or the fixed
		reference. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: ref_marker: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:MREFerence?')
		return Conversions.str_to_int(response)
