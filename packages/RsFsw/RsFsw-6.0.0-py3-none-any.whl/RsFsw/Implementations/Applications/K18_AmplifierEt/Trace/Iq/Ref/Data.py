from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def get(self) -> List[float]:
		"""SCPI: TRACe:IQ:REF[:DATA] \n
		Snippet: value: List[float] = driver.applications.k18AmplifierEt.trace.iq.ref.data.get() \n
		This command queries the reference trace I/Q data. \n
			:return: ref_iq_data: No help available"""
		response = self._core.io.query_bin_or_ascii_float_list(f'FORMAT REAL,32;TRACe:IQ:REF:DATA?')
		return response
