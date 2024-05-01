from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmsCls:
	"""Rms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rms", core, parent)

	def get(self, trace=repcap.Trace.Default) -> float:
		"""SCPI: FETCh:PNOise<t>:RMS \n
		Snippet: value: float = driver.applications.k40PhaseNoise.fetch.pnoise.rms.get(trace = repcap.Trace.Default) \n
		Queries the residual RMS jitter for the first trace. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Pnoise')
			:return: value: No help available"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'FETCh:PNOise{trace_cmd_val}:RMS?')
		return Conversions.str_to_float(response)
