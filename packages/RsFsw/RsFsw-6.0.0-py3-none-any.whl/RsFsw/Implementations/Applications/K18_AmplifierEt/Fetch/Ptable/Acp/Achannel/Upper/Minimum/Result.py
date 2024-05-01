from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResultCls:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: FETCh:PTABle:ACP:ACHannel<ch>:UPPer:MINimum[:RESult] \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.ptable.acp.achannel.upper.minimum.result.get(window = repcap.Window.Default) \n
		These commands query the minimum result values for the parameter as shown in the 'Parameter Sweep' table. For details on
		the parameters, see 'Amplifier parameters'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Fetch')
			:return: results: numeric value"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'FETCh:PTABle:ACP:ACHannel{window_cmd_val}:UPPer:MINimum:RESult?')
		return Conversions.str_to_float(response)
