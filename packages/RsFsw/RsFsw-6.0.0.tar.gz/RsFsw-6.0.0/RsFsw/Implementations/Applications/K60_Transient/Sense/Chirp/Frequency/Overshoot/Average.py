from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self, query_range: enums.SelectionRangeB) -> float:
		"""SCPI: [SENSe]:CHIRp:FREQuency:OVERshoot:AVERage \n
		Snippet: value: float = driver.applications.k60Transient.sense.chirp.frequency.overshoot.average.get(query_range = enums.SelectionRangeB.ALL) \n
		No command help available \n
			:param query_range: CURRent | ALL
			:return: result: CURRent | ALL"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRangeB)
		response = self._core.io.query_str(f'SENSe:CHIRp:FREQuency:OVERshoot:AVERage? {param}')
		return Conversions.str_to_float(response)
