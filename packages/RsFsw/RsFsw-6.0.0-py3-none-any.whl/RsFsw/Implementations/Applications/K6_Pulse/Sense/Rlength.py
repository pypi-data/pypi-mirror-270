from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RlengthCls:
	"""Rlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rlength", core, parent)

	def get(self) -> int:
		"""SCPI: [SENSe]:RLENgth \n
		Snippet: value: int = driver.applications.k6Pulse.sense.rlength.get() \n
		Returns the record length determined by the current measurement settings. \n
			:return: record_length: Number of samples captured in one sweep."""
		response = self._core.io.query_str(f'SENSe:RLENgth?')
		return Conversions.str_to_int(response)
