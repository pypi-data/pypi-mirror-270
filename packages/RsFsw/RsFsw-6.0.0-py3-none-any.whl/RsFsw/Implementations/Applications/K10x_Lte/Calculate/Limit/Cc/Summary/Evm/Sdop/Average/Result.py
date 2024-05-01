from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.Utilities import trim_str_response
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, carrierComponent=repcap.CarrierComponent.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit<li>[:CC<cc>]:SUMMary:EVM:SDOP[:AVERage]:RESult \n
		Snippet: value: str = driver.applications.k10Xlte.calculate.limit.cc.summary.evm.sdop.average.result.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: limit_check: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CC{carrierComponent_cmd_val}:SUMMary:EVM:SDOP:AVERage:RESult?')
		return trim_str_response(response)
