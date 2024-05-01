from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChipsCls:
	"""Chips commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chips", core, parent)

	def get(self) -> float:
		"""SCPI: [SENSe]:CAPTure:LENGth:CHIPs \n
		Snippet: value: float = driver.applications.k149Uwb.sense.capture.length.chips.get() \n
		Returns the capture length in chips. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'SENSe:CAPTure:LENGth:CHIPs?')
		return Conversions.str_to_float(response)
