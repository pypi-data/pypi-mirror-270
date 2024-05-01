from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TriggerCls:
	"""Trigger commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:ADJust:CONFigure:TRIGger \n
		Snippet: driver.applications.k70Vsa.sense.adjust.configure.trigger.set(state = False) \n
		Defines the behavior of a triggered measurement when adjusting a setting automatically (using SENS:ADJ:LEV ON, for
		example) . See 'Adjusting settings automatically during triggered measurements'. \n
			:param state: ON | OFF | 0 | 1 ON | 1 (default:) The measurement for adjustment waits for the next trigger. To abort the measurement, use [CMDLINKRESOLVED #Abort CMDLINKRESOLVED]. OFF | 0 The measurement for adjustment is performed without waiting for a trigger (corresponds to 'Continue' in manual operation) .
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADJust:CONFigure:TRIGger {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADJust:CONFigure:TRIGger \n
		Snippet: value: bool = driver.applications.k70Vsa.sense.adjust.configure.trigger.get() \n
		Defines the behavior of a triggered measurement when adjusting a setting automatically (using SENS:ADJ:LEV ON, for
		example) . See 'Adjusting settings automatically during triggered measurements'. \n
			:return: state: ON | OFF | 0 | 1 ON | 1 (default:) The measurement for adjustment waits for the next trigger. To abort the measurement, use [CMDLINKRESOLVED #Abort CMDLINKRESOLVED]. OFF | 0 The measurement for adjustment is performed without waiting for a trigger (corresponds to 'Continue' in manual operation) ."""
		response = self._core.io.query_str(f'SENSe:ADJust:CONFigure:TRIGger?')
		return Conversions.str_to_bool(response)
