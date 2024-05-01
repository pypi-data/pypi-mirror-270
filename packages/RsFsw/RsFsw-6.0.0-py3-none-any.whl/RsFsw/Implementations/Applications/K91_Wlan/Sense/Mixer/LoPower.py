from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LoPowerCls:
	"""LoPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("loPower", core, parent)

	def set(self, level: float) -> None:
		"""SCPI: [SENSe]:MIXer:LOPower \n
		Snippet: driver.applications.k91Wlan.sense.mixer.loPower.set(level = 1.0) \n
		Specifies the LO level of the external mixer's LO port. \n
			:param level: Range: 13.0 dBm to 17.0 dBm, Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SENSe:MIXer:LOPower {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:LOPower \n
		Snippet: value: float = driver.applications.k91Wlan.sense.mixer.loPower.get() \n
		Specifies the LO level of the external mixer's LO port. \n
			:return: level: Range: 13.0 dBm to 17.0 dBm, Unit: DBM"""
		response = self._core.io.query_str(f'SENSe:MIXer:LOPower?')
		return Conversions.str_to_float(response)
