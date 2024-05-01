from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, auto_auto_level: enums.AutoManualMode) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure[:LEVel]:DURation:MODE \n
		Snippet: driver.applications.k70Vsa.sense.adjust.configure.level.duration.mode.set(auto_auto_level = enums.AutoManualMode.AUTO) \n
		To determine the ideal reference level, the FSW performs a measurement on the current input data. This command selects
		the way the FSW determines the length of the measurement . \n
			:param auto_auto_level: AUTO The FSW determines the measurement length automatically according to the current input data. MANual The FSW uses the measurement length defined by [SENSe:]ADJust:CONFigure:LEVel:DURation.
		"""
		param = Conversions.enum_scalar_to_str(auto_auto_level, enums.AutoManualMode)
		self._core.io.write(f'SENSe:ADJust:CONFigure:LEVel:DURation:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoManualMode:
		"""SCPI: [SENSe]:ADJust:CONFigure[:LEVel]:DURation:MODE \n
		Snippet: value: enums.AutoManualMode = driver.applications.k70Vsa.sense.adjust.configure.level.duration.mode.get() \n
		To determine the ideal reference level, the FSW performs a measurement on the current input data. This command selects
		the way the FSW determines the length of the measurement . \n
			:return: auto_auto_level: No help available"""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:LEVel:DURation:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
