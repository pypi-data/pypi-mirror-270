from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConditionCls:
	"""Condition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("condition", core, parent)

	def get(self) -> str:
		"""SCPI: STATus:QUEStionable:POWer:CONDition \n
		Snippet: value: str = driver.applications.k10Xlte.status.questionable.power.condition.get() \n
		These commands read out the CONDition section of the status register. The commands do not delete the contents of the
		CONDition section. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'STATus:QUEStionable:POWer:CONDition?')
		return trim_str_response(response)
