from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChannelCls:
	"""Channel commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Channel, default value after init: Channel.Ch1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channel", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channel_get', 'repcap_channel_set', repcap.Channel.Ch1)

	def repcap_channel_set(self, channel: repcap.Channel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Channel.Default
		Default value after init: Channel.Ch1"""
		self._cmd_group.set_repcap_enum_value(channel)

	def repcap_channel_get(self) -> repcap.Channel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, bandwidth: float, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth[:CHANnel<ch>] \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.bandwidth.channel.set(bandwidth = 1.0, channel = repcap.Channel.Default) \n
		Defines the channel bandwidth of the transmission channels. Steep-edged channel filters are available for fast ACLR
		measurements. \n
			:param bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe:POWer:ACHannel:BWIDth:CHANnel{channel_cmd_val} {param}')

	def get(self, channel=repcap.Channel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth[:CHANnel<ch>] \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.achannel.bandwidth.channel.get(channel = repcap.Channel.Default) \n
		Defines the channel bandwidth of the transmission channels. Steep-edged channel filters are available for fast ACLR
		measurements. \n
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:return: bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:BWIDth:CHANnel{channel_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'ChannelCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChannelCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
