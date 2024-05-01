from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, number: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:TXCHannel:COUNt \n
		Snippet: driver.applications.k10Xlte.sense.power.achannel.txChannel.count.set(number = 1.0) \n
		Defines the number of transmission channels. The command works for measurements in the frequency domain. \n
			:param number: Range: 1 to 18
		"""
		param = Conversions.decimal_value_to_str(number)
		self._core.io.write(f'SENSe:POWer:ACHannel:TXCHannel:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:TXCHannel:COUNt \n
		Snippet: value: float = driver.applications.k10Xlte.sense.power.achannel.txChannel.count.get() \n
		Defines the number of transmission channels. The command works for measurements in the frequency domain. \n
			:return: number: Range: 1 to 18"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:TXCHannel:COUNt?')
		return Conversions.str_to_float(response)
