from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BoundaryCls:
	"""Boundary commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("boundary", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: TRACe<n>:IQ:SCAPture:BOUNdary \n
		Snippet: value: str = driver.applications.k6Pulse.trace.iq.scapture.boundary.get(window = repcap.Window.Default) \n
		This remote control command returns an array of sample indices for the start of each captured data segment. The length of
		the array depends on the number of trigger events specified by [SENSe:]SWEep:SCAPture:EVENts. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: data: 1..n Window"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'TRACe{window_cmd_val}:IQ:SCAPture:BOUNdary?')
		return trim_str_response(response)
