from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GmcFreqCls:
	"""GmcFreq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gmcFreq", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: CONFigure[:NR5G]:GMCFreq \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.gmcFreq.set(frequency = 1.0) \n
		Defines the global multicarrier frequency for component carrier setups. \n
			:param frequency: Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:NR5G:GMCFreq {param}')

	def get(self) -> float:
		"""SCPI: CONFigure[:NR5G]:GMCFreq \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.gmcFreq.get() \n
		Defines the global multicarrier frequency for component carrier setups. \n
			:return: frequency: Unit: Hz"""
		response = self._core.io.query_str(f'CONFigure:NR5G:GMCFreq?')
		return Conversions.str_to_float(response)
