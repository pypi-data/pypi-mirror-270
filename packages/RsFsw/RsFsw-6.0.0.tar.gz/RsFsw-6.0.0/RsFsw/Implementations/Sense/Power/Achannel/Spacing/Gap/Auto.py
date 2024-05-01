from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, spacing: float, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:GAP<gap>[:AUTO] \n
		Snippet: driver.sense.power.achannel.spacing.gap.auto.set(spacing = 1.0, gapChannel = repcap.GapChannel.Default) \n
		Defines the distance from sub block to the specified gap channel. In 'Auto' gap mode, channels in the upper gap are
		identical to those in the lower gap. Thus, only 2 gap channels are configured. The spacing for gap channels is defined in
		relation to the outer edges of the surrounding sub blocks, i.e. Spacing = [CF of the gap channel] - [left sub block
		center] + ([RF bandwidth of left sub block] /2) (See also Figure 'MSR signal structure' and Figure 'Sub block definition'.
		) \n
			:param spacing: numeric value in Hz Unit: HZ
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = Conversions.decimal_value_to_str(spacing)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:SPACing:GAP{gapChannel_cmd_val}:AUTO {param}')
