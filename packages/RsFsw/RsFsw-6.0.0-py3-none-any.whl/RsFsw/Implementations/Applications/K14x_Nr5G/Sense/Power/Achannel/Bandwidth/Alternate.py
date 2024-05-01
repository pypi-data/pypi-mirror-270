from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlternateCls:
	"""Alternate commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Channel, default value after init: Channel.Ch1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alternate", core, parent)
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
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:ALTernate<ch> \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.bandwidth.alternate.set(bandwidth = 1.0, channel = repcap.Channel.Default) \n
		Defines the channel bandwidth of the alternate channels. For MSR signals, this command defines the bandwidth of the lower
		alternate channels in asymmetrical configurations. To configure the bandwidth for the upper alternate channel, use the
		[SENSe:]POWer:ACHannel:BANDwidth:UALTernate<ch> command. If you set the channel bandwidth for the first alternate channel,
		the FSW sets the bandwidth of the other alternate channels to the same value, but not the other way round (not for MSR
		signals) . The command works hierarchically: to set a bandwidth of the 3rd and 4th channel, you have to set the bandwidth
		of the 3rd channel first. Steep-edged channel filters are available for fast ACLR measurements. \n
			:param bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe:POWer:ACHannel:BWIDth:ALTernate{channel_cmd_val} {param}')

	def get(self, channel=repcap.Channel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:ALTernate<ch> \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.achannel.bandwidth.alternate.get(channel = repcap.Channel.Default) \n
		Defines the channel bandwidth of the alternate channels. For MSR signals, this command defines the bandwidth of the lower
		alternate channels in asymmetrical configurations. To configure the bandwidth for the upper alternate channel, use the
		[SENSe:]POWer:ACHannel:BANDwidth:UALTernate<ch> command. If you set the channel bandwidth for the first alternate channel,
		the FSW sets the bandwidth of the other alternate channels to the same value, but not the other way round (not for MSR
		signals) . The command works hierarchically: to set a bandwidth of the 3rd and 4th channel, you have to set the bandwidth
		of the 3rd channel first. Steep-edged channel filters are available for fast ACLR measurements. \n
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
			:return: bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:BWIDth:ALTernate{channel_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'AlternateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AlternateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
