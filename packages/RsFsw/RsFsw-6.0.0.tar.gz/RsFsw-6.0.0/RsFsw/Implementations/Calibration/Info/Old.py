from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OldCls:
	"""Old commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("old", core, parent)

	def get(self) -> bool:
		"""SCPI: CALibration:INFO:OLD \n
		Snippet: value: bool = driver.calibration.info.old.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'CALibration:INFO:OLD?')
		return Conversions.str_to_bool(response)
