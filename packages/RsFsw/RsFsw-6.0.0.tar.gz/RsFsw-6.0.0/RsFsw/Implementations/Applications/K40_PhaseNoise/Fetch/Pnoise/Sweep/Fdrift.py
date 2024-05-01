from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FdriftCls:
	"""Fdrift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fdrift", core, parent)

	def get(self, trace=repcap.Trace.Default) -> List[float]:
		"""SCPI: FETCh:PNOise<t>:SWEep:FDRift \n
		Snippet: value: List[float] = driver.applications.k40PhaseNoise.fetch.pnoise.sweep.fdrift.get(trace = repcap.Trace.Default) \n
		Queries the frequency drift in each half decade. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Pnoise')
			:return: frequency_drifts: No help available"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_bin_or_ascii_float_list(f'FETCh:PNOise{trace_cmd_val}:SWEep:FDRift?')
		return response
