from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaclrCls:
	"""Caclr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caclr", core, parent)

	def set(self, state: float or bool) -> None:
		"""SCPI: CONFigure[:NR5G]:CACLr \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.caclr.set(state = 1.0) \n
		No command help available \n
			:param state: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(state)
		self._core.io.write(f'CONFigure:NR5G:CACLr {param}')

	def get(self) -> float or bool:
		"""SCPI: CONFigure[:NR5G]:CACLr \n
		Snippet: value: float or bool = driver.applications.k14Xnr5G.configure.nr5G.caclr.get() \n
		No command help available \n
			:return: state: (float or boolean) No help available"""
		response = self._core.io.query_str(f'CONFigure:NR5G:CACLr?')
		return Conversions.str_to_float_or_bool(response)
