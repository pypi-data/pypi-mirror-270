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

	def get(self, power: enums.SelectionRangeB) -> float:
		"""SCPI: FETCh:STABle:BBPower:MIN:MINimum \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.stable.bbPower.min.minimum.get(power = enums.SelectionRangeB.ALL) \n
		Returns the statistical value for the minimum power. \n
			:param power: CURRent | ALL
			:return: result: CURRent | ALL"""
		param = Conversions.enum_scalar_to_str(power, enums.SelectionRangeB)
		response = self._core.io.query_str(f'FETCh:STABle:BBPower:MIN:MINimum? {param}')
		return Conversions.str_to_float(response)
