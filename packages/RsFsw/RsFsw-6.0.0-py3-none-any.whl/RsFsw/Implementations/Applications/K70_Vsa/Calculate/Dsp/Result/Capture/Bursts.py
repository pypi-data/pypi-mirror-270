from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BurstsCls:
	"""Bursts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bursts", core, parent)

	def get(self, window=repcap.Window.Default) -> int:
		"""SCPI: CALCulate<n>:DSP:RESult:CAPTure:BURSts \n
		Snippet: value: int = driver.applications.k70Vsa.calculate.dsp.result.capture.bursts.get(window = repcap.Window.Default) \n
		Queries the number of bursts found across the internal capture buffer. Note that the internal capture buffer is slightly
		larger than the displayed capture buffer in order to allow for sufficient filter settling times for further processing. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: bursts: integer Number of bursts"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DSP:RESult:CAPTure:BURSts?')
		return Conversions.str_to_int(response)
