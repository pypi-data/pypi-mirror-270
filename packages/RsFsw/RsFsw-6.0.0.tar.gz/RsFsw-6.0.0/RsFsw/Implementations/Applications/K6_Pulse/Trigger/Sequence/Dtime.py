from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DtimeCls:
	"""Dtime commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtime", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:DTIMe \n
		Snippet: driver.applications.k6Pulse.trigger.sequence.dtime.set(time = 1.0) \n
		Defines the time the input signal must stay below the trigger level before a trigger is detected again. For input from
		the 'Analog Baseband' interface using the baseband power trigger (BBP) , the default drop out time is set to 100 ns to
		avoid unintentional trigger events (as no hysteresis can be configured in this case) . \n
			:param time: Dropout time of the trigger. Range: 0 s to 10.0 s , Unit: S
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'TRIGger:SEQuence:DTIMe {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:DTIMe \n
		Snippet: value: float = driver.applications.k6Pulse.trigger.sequence.dtime.get() \n
		Defines the time the input signal must stay below the trigger level before a trigger is detected again. For input from
		the 'Analog Baseband' interface using the baseband power trigger (BBP) , the default drop out time is set to 100 ns to
		avoid unintentional trigger events (as no hysteresis can be configured in this case) . \n
			:return: time: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:DTIMe?')
		return Conversions.str_to_float(response)
