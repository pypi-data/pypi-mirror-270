from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlenCls:
	"""Rlen commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlen", core, parent)

	def get(self) -> float:
		"""SCPI: TRACe:IQ:RLEN \n
		Snippet: value: float = driver.applications.k149Uwb.trace.iq.rlen.get() \n
		Returns the sweep length or capture length. \n
			:return: sample_rate: numeric value"""
		response = self._core.io.query_str(f'TRACe:IQ:RLEN?')
		return Conversions.str_to_float(response)
