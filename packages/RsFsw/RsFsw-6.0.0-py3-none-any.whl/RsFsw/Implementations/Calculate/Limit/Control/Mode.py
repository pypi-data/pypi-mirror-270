from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.ReferenceMode, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:CONTrol:MODE \n
		Snippet: driver.calculate.limit.control.mode.set(mode = enums.ReferenceMode.ABSolute, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Selects the horizontal limit line scaling. \n
			:param mode: ABSolute Limit line is defined by absolute physical values (Hz or s) . RELative Limit line is defined by relative values related to the center frequency (frequency domain) or the left diagram border (time domain) .
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ReferenceMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CONTrol:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> enums.ReferenceMode:
		"""SCPI: CALCulate<n>:LIMit<li>:CONTrol:MODE \n
		Snippet: value: enums.ReferenceMode = driver.calculate.limit.control.mode.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Selects the horizontal limit line scaling. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: mode: ABSolute Limit line is defined by absolute physical values (Hz or s) . RELative Limit line is defined by relative values related to the center frequency (frequency domain) or the left diagram border (time domain) ."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CONTrol:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceMode)
