from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LedStateCls:
	"""LedState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ledState", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.LedState:
		"""SCPI: CONFigure:CFReduction:PFRequency:LEDState \n
		Snippet: value: enums.LedState = driver.applications.k18AmplifierEt.configure.cfReduction.pfrequency.ledState.get() \n
		Reads the LED status of crest factor reduction passband frequency. \n
			:return: state: GREY | RED | GREen"""
		response = self._core.io.query_str(f'CONFigure:CFReduction:PFRequency:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)
