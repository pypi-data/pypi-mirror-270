from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.Utilities import trim_str_response
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import AbsoluteCls
			self._absolute = AbsoluteCls(self._core, self._cmd_group)
		return self._absolute

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import RelativeCls
			self._relative = RelativeCls(self._core, self._cmd_group)
		return self._relative

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, gapChannel=repcap.GapChannel.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit<li>:ACPower:GAP<gap>:ACLR:RESult \n
		Snippet: value: str = driver.applications.k14Xnr5G.calculate.limit.acPower.gap.aclr.result.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, gapChannel = repcap.GapChannel.Default) \n
		The command returns the ACLR power limit check results for the selected gap channel in an MSR ACLR measurement. To get a
		valid result, you have to perform a complete measurement with synchronization to the end of the measurement before
		reading out the result. This is only possible for single sweep mode. See also method RsFsw.Applications.K10x_Lte.Initiate.
		Continuous.set. For details on MSR signals see 'Measurement on multi-standard radio (MSR) signals'. The results of the
		power limit checks are also indicated in the method RsFsw.Status.Questionable.AcpLimit.Event.get_ status registry (see
		'STATus:QUEStionable:ACPLimit register') . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: limit_check: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ACPower:GAP{gapChannel_cmd_val}:ACLR:RESult?')
		return trim_str_response(response)

	def clone(self) -> 'ResultCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResultCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
