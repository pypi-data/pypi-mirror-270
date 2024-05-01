from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Types import DataType
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowerCls:
	"""Lower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lower", core, parent)

	def set(self, sb_gaps: enums.SubBlockGaps, alpha: float, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:GAP<gap>:MANual:LOWer \n
		Snippet: driver.sense.power.achannel.filterPy.alpha.gap.manual.lower.set(sb_gaps = enums.SubBlockGaps.AB, alpha = 1.0, gapChannel = repcap.GapChannel.Default) \n
		Defines the roll-off factor for the specified lower gap channel's weighting filter. Is only available for for
		asymmetrical (manual) configuration of gap channels (see [SENSe:]POWer:ACHannel:GAP<gap>:MODE) . \n
			:param sb_gaps: AB | BC | CD | DE | EF | FG | GH Name of the gap, defined by the letters of the surrounding sub blocks (e.g. 'AB' for the gap between sub blocks A and B) .
			:param alpha: Roll-off factor Range: 0 to 1
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sb_gaps', sb_gaps, DataType.Enum, enums.SubBlockGaps), ArgSingle('alpha', alpha, DataType.Float))
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:ALPHa:GAP{gapChannel_cmd_val}:MANual:LOWer {param}'.rstrip())

	def get(self, sb_gaps: enums.SubBlockGaps, gapChannel=repcap.GapChannel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:GAP<gap>:MANual:LOWer \n
		Snippet: value: float = driver.sense.power.achannel.filterPy.alpha.gap.manual.lower.get(sb_gaps = enums.SubBlockGaps.AB, gapChannel = repcap.GapChannel.Default) \n
		Defines the roll-off factor for the specified lower gap channel's weighting filter. Is only available for for
		asymmetrical (manual) configuration of gap channels (see [SENSe:]POWer:ACHannel:GAP<gap>:MODE) . \n
			:param sb_gaps: AB | BC | CD | DE | EF | FG | GH Name of the gap, defined by the letters of the surrounding sub blocks (e.g. 'AB' for the gap between sub blocks A and B) .
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: alpha: Roll-off factor Range: 0 to 1"""
		param = Conversions.enum_scalar_to_str(sb_gaps, enums.SubBlockGaps)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:ALPHa:GAP{gapChannel_cmd_val}:MANual:LOWer? {param}')
		return Conversions.str_to_float(response)
