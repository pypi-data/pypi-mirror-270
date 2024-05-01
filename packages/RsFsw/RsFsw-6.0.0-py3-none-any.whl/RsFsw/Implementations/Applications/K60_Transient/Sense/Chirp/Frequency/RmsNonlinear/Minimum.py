from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MinimumCls:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def get(self, query_range: enums.SelectionRangeB) -> float:
		"""SCPI: [SENSe]:CHIRp:FREQuency:RMSNonlinear:MINimum \n
		Snippet: value: float = driver.applications.k60Transient.sense.chirp.frequency.rmsNonlinear.minimum.get(query_range = enums.SelectionRangeB.ALL) \n
		Queries chirp frequency overshoot from the result table. \n
			:param query_range: SELected | CURRent | ALL
			:return: result: numeric value"""
		param = Conversions.enum_scalar_to_str(query_range, enums.SelectionRangeB)
		response = self._core.io.query_str(f'SENSe:CHIRp:FREQuency:RMSNonlinear:MINimum? {param}')
		return Conversions.str_to_float(response)
