from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StopCls:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:FREQuency:STOP \n
		Snippet: value: float = driver.applications.k60Transient.sense.mixer.frequency.stop.get() \n
		Sets or queries the frequency at which the external mixer band stops. \n
			:return: frequency: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:FREQuency:STOP?')
		return Conversions.str_to_float(response)
