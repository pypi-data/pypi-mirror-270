from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ValueCls:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, seg_cap_events_count: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:VALue \n
		Snippet: driver.applications.k149Uwb.calculate.limit.espectrum.value.set(seg_cap_events_count = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Activates the manual limit line selection as and specifies the expected power as a value. Depending on the entered value,
		the associated predefined limit lines is selected. Has the same effect as a combination of the CALC:LIM:ESP:MODE MAN and
		the method RsFsw.Calculate.Limit.Espectrum.Pclass.Exclusive.set commands; however, the power class to be used is not
		defined directly, but via the expected power. As opposed to CALC:LIM:ESP:MODE AUTO, the power class is not re-assigned to
		the input signal power dynamically, but only once when the command is executed. \n
			:param seg_cap_events_count: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(seg_cap_events_count)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:VALue {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:VALue \n
		Snippet: value: float = driver.applications.k149Uwb.calculate.limit.espectrum.value.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Activates the manual limit line selection as and specifies the expected power as a value. Depending on the entered value,
		the associated predefined limit lines is selected. Has the same effect as a combination of the CALC:LIM:ESP:MODE MAN and
		the method RsFsw.Calculate.Limit.Espectrum.Pclass.Exclusive.set commands; however, the power class to be used is not
		defined directly, but via the expected power. As opposed to CALC:LIM:ESP:MODE AUTO, the power class is not re-assigned to
		the input signal power dynamically, but only once when the command is executed. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: seg_cap_events_count: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:VALue?')
		return Conversions.str_to_float(response)
