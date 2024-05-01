from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EventsCls:
	"""Events commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("events", core, parent)

	def set(self, count: float) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture:EVENts \n
		Snippet: driver.applications.k6Pulse.sense.sweep.scapture.events.set(count = 1.0) \n
		Specifies the number of trigger events for which data segments are to be captured. \n
			:param count: numeric value
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SENSe:SWEep:SCAPture:EVENts {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:SCAPture:EVENts \n
		Snippet: value: float = driver.applications.k6Pulse.sense.sweep.scapture.events.get() \n
		Specifies the number of trigger events for which data segments are to be captured. \n
			:return: count: numeric value"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:EVENts?')
		return Conversions.str_to_float(response)
