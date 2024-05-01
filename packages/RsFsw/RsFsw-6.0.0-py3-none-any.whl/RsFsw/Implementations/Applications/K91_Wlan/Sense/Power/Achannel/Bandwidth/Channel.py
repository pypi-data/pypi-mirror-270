from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelCls:
	"""Channel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channel", core, parent)

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth[:CHANnel] \n
		Snippet: driver.applications.k91Wlan.sense.power.achannel.bandwidth.channel.set(bandwidth = 1.0) \n
		Defines the channel bandwidth of the transmission channels. Steep-edged channel filters are available for fast ACLR
		measurements. \n
			:param bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:POWer:ACHannel:BWIDth:CHANnel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth[:CHANnel] \n
		Snippet: value: float = driver.applications.k91Wlan.sense.power.achannel.bandwidth.channel.get() \n
		Defines the channel bandwidth of the transmission channels. Steep-edged channel filters are available for fast ACLR
		measurements. \n
			:return: bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:BWIDth:CHANnel?')
		return Conversions.str_to_float(response)
