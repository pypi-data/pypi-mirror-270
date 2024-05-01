from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: enums.LimitState, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:LIMit:STATe \n
		Snippet: driver.applications.k14Xnr5G.sense.espectrum.range.limit.state.set(state = enums.LimitState.ABSolute, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Selects the limit check mode for all SEM ranges (<range> is irrelevant) . \n
			:param state: ABSolute | RELative | AND | OR ABSolute Checks only the absolute limits defined. RELative Checks only the relative limits. Relative limits are defined as relative to the measured power in the reference range. AND Combines the absolute and relative limit. The limit check fails when both limits are violated. OR Combines the absolute and relative limit. The limit check fails when one of the limits is violated.
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.enum_scalar_to_str(state, enums.LimitState)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit:STATe {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> enums.LimitState:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<range>:LIMit:STATe \n
		Snippet: value: enums.LimitState = driver.applications.k14Xnr5G.sense.espectrum.range.limit.state.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		Selects the limit check mode for all SEM ranges (<range> is irrelevant) . \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: state: ABSolute | RELative | AND | OR ABSolute Checks only the absolute limits defined. RELative Checks only the relative limits. Relative limits are defined as relative to the measured power in the reference range. AND Combines the absolute and relative limit. The limit check fails when both limits are violated. OR Combines the absolute and relative limit. The limit check fails when one of the limits is violated."""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.LimitState)
