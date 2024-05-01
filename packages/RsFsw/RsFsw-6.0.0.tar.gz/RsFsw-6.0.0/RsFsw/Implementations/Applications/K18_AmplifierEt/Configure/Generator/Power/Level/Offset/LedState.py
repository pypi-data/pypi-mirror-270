from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LedStateCls:
	"""LedState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ledState", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.LedState:
		"""SCPI: CONFigure:GENerator:POWer:LEVel:OFFSet:LEDState \n
		Snippet: value: enums.LedState = driver.applications.k18AmplifierEt.configure.generator.power.level.offset.ledState.get() \n
		This command queries the level offset configuration state on the generator. \n
			:return: state: GREen Level offset configuration was successful. GREY Unknown level offset configuration state. RED Level offset configuration was not successful."""
		response = self._core.io.query_str(f'CONFigure:GENerator:POWer:LEVel:OFFSet:LEDState?')
		return Conversions.str_to_scalar_enum(response, enums.LedState)
