from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EventCls:
	"""Event commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("event", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: STATus:QUEStionable:MODulation<1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16>:EVM[:EVENt] \n
		Snippet: value: str = driver.applications.k70Vsa.status.questionable.modulation.evm.event.get(window = repcap.Window.Default) \n
		Reads out the EVENt section of the status register. The command also deletes the contents of the EVENt section. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Modulation')
			:return: channel_name: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'STATus:QUEStionable:MODulation{window_cmd_val}:EVM:EVENt?')
		return trim_str_response(response)
