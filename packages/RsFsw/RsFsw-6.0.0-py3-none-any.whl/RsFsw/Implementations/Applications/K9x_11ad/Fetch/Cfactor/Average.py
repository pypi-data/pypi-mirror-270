from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:CFACtor:AVERage \n
		Snippet: value: float = driver.applications.k9X11Ad.fetch.cfactor.average.get() \n
		Returns the average, maximum or minimum crest factor for the PPDU in dB. For details see 'Crest factor [dB]'. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:CFACtor:AVERage?')
		return Conversions.str_to_float(response)
