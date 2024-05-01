from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:GIMBalance:MINimum \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.gimbalance.minimum.get() \n
		Returns the average, maximum or minimum I/Q imbalance in dB. For details see 'Modulation accuracy, flatness and tolerance
		parameters'. \n
			:return: result: list"""
		response = self._core.io.query_str(f'FETCh:BURSt:GIMBalance:MINimum?')
		return trim_str_response(response)
