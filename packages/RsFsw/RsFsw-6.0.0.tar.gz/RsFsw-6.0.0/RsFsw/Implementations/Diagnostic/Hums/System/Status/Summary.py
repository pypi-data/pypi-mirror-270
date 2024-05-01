from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SummaryCls:
	"""Summary commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("summary", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.SystemStatus:
		"""SCPI: DIAGnostic:HUMS:SYSTem:STATus:SUMMary \n
		Snippet: value: enums.SystemStatus = driver.diagnostic.hums.system.status.summary.get() \n
		No command help available \n
			:return: system_status: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:HUMS:SYSTem:STATus:SUMMary?')
		return Conversions.str_to_scalar_enum(response, enums.SystemStatus)
