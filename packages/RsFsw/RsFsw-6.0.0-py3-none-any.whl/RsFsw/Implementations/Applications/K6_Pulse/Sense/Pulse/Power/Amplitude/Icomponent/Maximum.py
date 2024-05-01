from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def get(self, query_range: enums.SelectionRangeB) -> List[float]:
		"""SCPI: [SENSe]:PULSe:POWer:AMPLitude:I:MAXimum \n
		Snippet: value: List[float] = driver.applications.k6Pulse.sense.pulse.power.amplitude.icomponent.maximum.get(query_range = enums.SelectionRangeB.ALL) \n
		Returns the statistical value for the in-phase amplitude over the specified pulses. \n
			:param query_range: CURRent | ALL CURRent Detected pulses in the current capture buffer ALL All detected pulses in the entire measurement.
			:return: amplitudes: No help available"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRangeB)
		response = self._core.io.query_bin_or_ascii_float_list(f'SENSe:PULSe:POWer:AMPLitude:I:MAXimum? {param}')
		return response
