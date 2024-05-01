from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UalternateCls:
	"""Ualternate commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: UpperAltChannel, default value after init: UpperAltChannel.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ualternate", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_upperAltChannel_get', 'repcap_upperAltChannel_set', repcap.UpperAltChannel.Nr1)

	def repcap_upperAltChannel_set(self, upperAltChannel: repcap.UpperAltChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UpperAltChannel.Default
		Default value after init: UpperAltChannel.Nr1"""
		self._cmd_group.set_repcap_enum_value(upperAltChannel)

	def repcap_upperAltChannel_get(self) -> repcap.UpperAltChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, bandwidth: float, upperAltChannel=repcap.UpperAltChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:UALTernate<ch> \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.bandwidth.ualternate.set(bandwidth = 1.0, upperAltChannel = repcap.UpperAltChannel.Default) \n
		Defines the channel bandwidth of the upper alternate channels in asymmetrical configurations. To configure the bandwidth
		for the lower alternate channel, use the [SENSe:]POWer:ACHannel:BANDwidth:ALTernate<ch> command. Steep-edged channel
		filters are available for fast ACLR measurements. \n
			:param bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz
			:param upperAltChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ualternate')
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		upperAltChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(upperAltChannel, repcap.UpperAltChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:BWIDth:UALTernate{upperAltChannel_cmd_val} {param}')

	def get(self, upperAltChannel=repcap.UpperAltChannel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:BWIDth:UALTernate<ch> \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.achannel.bandwidth.ualternate.get(upperAltChannel = repcap.UpperAltChannel.Default) \n
		Defines the channel bandwidth of the upper alternate channels in asymmetrical configurations. To configure the bandwidth
		for the lower alternate channel, use the [SENSe:]POWer:ACHannel:BANDwidth:ALTernate<ch> command. Steep-edged channel
		filters are available for fast ACLR measurements. \n
			:param upperAltChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ualternate')
			:return: bandwidth: Range: 100 Hz to 1000 MHz, Unit: Hz"""
		upperAltChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(upperAltChannel, repcap.UpperAltChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:BWIDth:UALTernate{upperAltChannel_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'UalternateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UalternateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
