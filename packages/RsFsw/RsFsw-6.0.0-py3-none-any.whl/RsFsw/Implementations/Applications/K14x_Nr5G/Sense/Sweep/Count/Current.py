from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:COUNt:CURRent \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.sweep.count.current.get() \n
		Queries the current statistics counter value which indicates how many result ranges have been evaluated. For results that
		use the capture buffer as a source, the number of used capture buffers can be queried. \n
			:return: sweep_count: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:COUNt:CURRent?')
		return Conversions.str_to_float(response)
