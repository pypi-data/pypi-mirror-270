from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlengthCls:
	"""Rlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlength", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:RLENgth \n
		Snippet: value: float = driver.sense.rlength.get() \n
		No command help available \n
			:return: sample_count: No help available"""
		response = self._core.io.query_str(f'SENSe:RLENgth?')
		return Conversions.str_to_float(response)
