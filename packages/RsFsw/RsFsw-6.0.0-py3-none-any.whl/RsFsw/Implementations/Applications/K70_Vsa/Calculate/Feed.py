from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FeedCls:
	"""Feed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("feed", core, parent)

	def set(self, feed: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:FEED \n
		Snippet: driver.applications.k70Vsa.calculate.feed.set(feed = 'abc', window = repcap.Window.Default) \n
		Selects the evaluation method of the measured data that is to be displayed in the specified window. Note that this
		command is maintained for compatibility reasons only. Use the LAYout commands for new remote control programs (see
		'Working with windows in the display') . \n
			:param feed: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(feed)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:FEED {param}')

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: CALCulate<n>:FEED \n
		Snippet: value: str = driver.applications.k70Vsa.calculate.feed.get(window = repcap.Window.Default) \n
		Selects the evaluation method of the measured data that is to be displayed in the specified window. Note that this
		command is maintained for compatibility reasons only. Use the LAYout commands for new remote control programs (see
		'Working with windows in the display') . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: feed: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:FEED?')
		return trim_str_response(response)
