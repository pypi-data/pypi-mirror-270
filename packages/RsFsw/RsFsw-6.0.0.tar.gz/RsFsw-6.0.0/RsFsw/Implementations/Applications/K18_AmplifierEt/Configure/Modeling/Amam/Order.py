from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OrderCls:
	"""Order commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("order", core, parent)

	def set(self, order: str) -> None:
		"""SCPI: CONFigure:MODeling:AMAM:ORDer \n
		Snippet: driver.applications.k18AmplifierEt.configure.modeling.amam.order.set(order = 'abc') \n
		This command defines the order (or degree) of the 'AM/AM' model polynomials that are calculated by the application. \n
			:param order: String containing the polynomials to be calculated. You can either select a range of polynomials (e.g. '1-7') , a selection of polynomials (e.g. '1;3;5') or a combination of both (e.g. '1;3-5') . Range: 0 to 18
		"""
		param = Conversions.value_to_quoted_str(order)
		self._core.io.write(f'CONFigure:MODeling:AMAM:ORDer {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:MODeling:AMAM:ORDer \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.modeling.amam.order.get() \n
		This command defines the order (or degree) of the 'AM/AM' model polynomials that are calculated by the application. \n
			:return: order: String containing the polynomials to be calculated. You can either select a range of polynomials (e.g. '1-7') , a selection of polynomials (e.g. '1;3;5') or a combination of both (e.g. '1;3-5') . Range: 0 to 18"""
		response = self._core.io.query_str(f'CONFigure:MODeling:AMAM:ORDer?')
		return trim_str_response(response)
