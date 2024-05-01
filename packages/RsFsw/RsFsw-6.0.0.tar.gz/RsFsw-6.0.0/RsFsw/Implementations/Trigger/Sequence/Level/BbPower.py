from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbPowerCls:
	"""BbPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbPower", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:LEVel:BBPower \n
		Snippet: driver.trigger.sequence.level.bbPower.set(level = 1.0) \n
		Sets the level of the baseband power trigger. Is available for the optional 'Digital Baseband' interface. Is available
		for the optional 'Analog Baseband' interface. \n
			:param level: Range: -50 dBm to +20 dBm, Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'TRIGger:SEQuence:LEVel:BBPower {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:LEVel:BBPower \n
		Snippet: value: float = driver.trigger.sequence.level.bbPower.get() \n
		Sets the level of the baseband power trigger. Is available for the optional 'Digital Baseband' interface. Is available
		for the optional 'Analog Baseband' interface. \n
			:return: level: Range: -50 dBm to +20 dBm, Unit: DBM"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:LEVel:BBPower?')
		return Conversions.str_to_float(response)
