from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValueCls:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, hor_line_abs_pos: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:DLABs[:VALue] \n
		Snippet: driver.applications.k70Vsa.calculate.dlabs.value.set(hor_line_abs_pos = 1.0, window = repcap.Window.Default) \n
		Defines value of horizontal absolute line \n
			:param hor_line_abs_pos: Y-value of the absolute horizontal line.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(hor_line_abs_pos)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:DLABs:VALue {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:DLABs[:VALue] \n
		Snippet: value: float = driver.applications.k70Vsa.calculate.dlabs.value.get(window = repcap.Window.Default) \n
		Defines value of horizontal absolute line \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: hor_line_abs_pos: Y-value of the absolute horizontal line."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DLABs:VALue?')
		return Conversions.str_to_float(response)
