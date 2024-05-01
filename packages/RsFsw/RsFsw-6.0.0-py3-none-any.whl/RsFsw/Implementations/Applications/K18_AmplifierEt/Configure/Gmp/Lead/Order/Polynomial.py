from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PolynomialCls:
	"""Polynomial commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("polynomial", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:GMP:LEAD:ORDer:POLYnomial \n
		Snippet: driver.applications.k18AmplifierEt.configure.gmp.lead.order.polynomial.set(level = 1.0) \n
		Sets the leading cross-terms polynomial order of the generalized memory polynomial. \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:GMP:LEAD:ORDer:POLYnomial {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GMP:LEAD:ORDer:POLYnomial \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.gmp.lead.order.polynomial.get() \n
		Sets the leading cross-terms polynomial order of the generalized memory polynomial. \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'CONFigure:GMP:LEAD:ORDer:POLYnomial?')
		return Conversions.str_to_float(response)
