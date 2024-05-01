from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SaTransientCls:
	"""SaTransient commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("saTransient", core, parent)

	def set(self, symbol: str) -> None:
		"""SCPI: [SENSe]:NR5G:DEMod:SATRansient \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.demod.saTransient.set(symbol = 'abc') \n
		Selects the symbol right after the transient period.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a transient period != 10 us ([SENSe:]NR5G:DEMod:TPERiod) . \n
			:param symbol: String containing the symbol numbers as a comma separated list.
		"""
		param = Conversions.value_to_quoted_str(symbol)
		self._core.io.write(f'SENSe:NR5G:DEMod:SATRansient {param}')

	def get(self) -> str:
		"""SCPI: [SENSe]:NR5G:DEMod:SATRansient \n
		Snippet: value: str = driver.applications.k14Xnr5G.sense.nr5G.demod.saTransient.get() \n
		Selects the symbol right after the transient period.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a transient period != 10 us ([SENSe:]NR5G:DEMod:TPERiod) . \n
			:return: symbol: String containing the symbol numbers as a comma separated list."""
		response = self._core.io.query_str(f'SENSe:NR5G:DEMod:SATRansient?')
		return trim_str_response(response)
