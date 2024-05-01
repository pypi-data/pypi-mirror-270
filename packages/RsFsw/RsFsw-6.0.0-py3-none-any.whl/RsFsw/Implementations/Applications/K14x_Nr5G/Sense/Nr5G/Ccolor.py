from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcolorCls:
	"""Ccolor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccolor", core, parent)

	def set(self, state: enums.CcolorState) -> None:
		"""SCPI: [SENSe]:NR5G:CCOLor \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.ccolor.set(state = enums.CcolorState.ALLocation) \n
		Selects the information that the colors of the constellation points in the constellation diagram represent. \n
			:param state: ALLocation Colors represent allocation types. MODulation Colors represent modulation types.
		"""
		param = Conversions.enum_scalar_to_str(state, enums.CcolorState)
		self._core.io.write(f'SENSe:NR5G:CCOLor {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CcolorState:
		"""SCPI: [SENSe]:NR5G:CCOLor \n
		Snippet: value: enums.CcolorState = driver.applications.k14Xnr5G.sense.nr5G.ccolor.get() \n
		Selects the information that the colors of the constellation points in the constellation diagram represent. \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SENSe:NR5G:CCOLor?')
		return Conversions.str_to_scalar_enum(response, enums.CcolorState)
