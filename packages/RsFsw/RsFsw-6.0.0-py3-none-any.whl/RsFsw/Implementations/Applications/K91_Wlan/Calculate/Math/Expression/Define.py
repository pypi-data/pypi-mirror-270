from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DefineCls:
	"""Define commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("define", core, parent)

	def set(self, expression: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MATH[:EXPRession][:DEFine] \n
		Snippet: driver.applications.k91Wlan.calculate.math.expression.define.set(expression = rawAbc, window = repcap.Window.Default) \n
		Selects the mathematical expression for trace mathematics. Before you can use the command, you have to turn trace
		mathematics on. \n
			:param expression: (TRACE1-TRACE2) Subtracts trace 2 from trace 1. (TRACE1-TRACE3) Subtracts trace 3 from trace 1. (TRACE1-TRACE4) Subtracts trace 4 from trace 1.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_str(expression)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MATH:EXPRession:DEFine {param}')

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: CALCulate<n>:MATH[:EXPRession][:DEFine] \n
		Snippet: value: str = driver.applications.k91Wlan.calculate.math.expression.define.get(window = repcap.Window.Default) \n
		Selects the mathematical expression for trace mathematics. Before you can use the command, you have to turn trace
		mathematics on. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: expression: (TRACE1-TRACE2) Subtracts trace 2 from trace 1. (TRACE1-TRACE3) Subtracts trace 3 from trace 1. (TRACE1-TRACE4) Subtracts trace 4 from trace 1."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MATH:EXPRession:DEFine?')
		return trim_str_response(response)
