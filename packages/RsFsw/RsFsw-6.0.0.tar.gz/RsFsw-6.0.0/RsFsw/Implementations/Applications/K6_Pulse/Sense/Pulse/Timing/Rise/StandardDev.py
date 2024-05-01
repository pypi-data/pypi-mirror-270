from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDevCls:
	"""StandardDev commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standardDev", core, parent)

	def get(self, query_range: enums.SelectionRangeB) -> str:
		"""SCPI: [SENSe]:PULSe:TIMing:RISE:SDEViation \n
		Snippet: value: str = driver.applications.k6Pulse.sense.pulse.timing.rise.standardDev.get(query_range = enums.SelectionRangeB.ALL) \n
		Returns the statistical value for the rise time over the specified pulses. \n
			:param query_range: CURRent | ALL CURRent Detected pulses in the current capture buffer ALL All detected pulses in the entire measurement.
			:return: result: char_data"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRangeB)
		response = self._core.io.query_str(f'SENSe:PULSe:TIMing:RISE:SDEViation? {param}')
		return trim_str_response(response)
