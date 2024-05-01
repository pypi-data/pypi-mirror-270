from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelCls:
	"""Channel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channel", core, parent)

	def set(self, spacing: float) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:CHANnel \n
		Snippet: driver.applications.k91Wlan.sense.power.achannel.spacing.channel.set(spacing = 1.0) \n
		Defines the distance between transmission channels. If you set the channel spacing for a transmission channel, the FSW
		sets the spacing of the lower transmission channels to the same value, but not the other way round. The command works
		hierarchically: to set a distance between the 2nd and 3rd and 3rd and 4th channel, you have to set the spacing between
		the 2nd and 3rd channel first. \n
			:param spacing: Range: 14 kHz to 2000 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(spacing)
		self._core.io.write(f'SENSe:POWer:ACHannel:SPACing:CHANnel {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:CHANnel \n
		Snippet: value: float = driver.applications.k91Wlan.sense.power.achannel.spacing.channel.get() \n
		Defines the distance between transmission channels. If you set the channel spacing for a transmission channel, the FSW
		sets the spacing of the lower transmission channels to the same value, but not the other way round. The command works
		hierarchically: to set a distance between the 2nd and 3rd and 3rd and 4th channel, you have to set the spacing between
		the 2nd and 3rd channel first. \n
			:return: spacing: Range: 14 kHz to 2000 MHz, Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SPACing:CHANnel?')
		return Conversions.str_to_float(response)
