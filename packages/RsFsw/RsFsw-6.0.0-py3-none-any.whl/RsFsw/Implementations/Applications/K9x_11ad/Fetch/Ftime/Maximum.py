from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:FTIMe:MAXimum \n
		Snippet: value: float = driver.applications.k9X11Ad.fetch.ftime.maximum.get() \n
		Returns the average, maximum or minimum fall time for the PPDU in s. For details see 'Fall Time [s]'. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:FTIMe:MAXimum?')
		return Conversions.str_to_float(response)
