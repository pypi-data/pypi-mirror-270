from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LimitsCls:
	"""Limits commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limits", core, parent)

	def set(self, limits: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<m>:ESPectrum:LIMits \n
		Snippet: driver.applications.k149Uwb.calculate.limit.espectrum.limits.set(limits = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command sets or queries up to 4 power classes in one step. You can only define values for the number of power
		classes defined by method RsFsw.Calculate.Limit.Espectrum.Pclass.Count.set. \n
			:param limits: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(limits)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:LIMits {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<m>:ESPectrum:LIMits \n
		Snippet: value: float = driver.applications.k149Uwb.calculate.limit.espectrum.limits.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command sets or queries up to 4 power classes in one step. You can only define values for the number of power
		classes defined by method RsFsw.Calculate.Limit.Espectrum.Pclass.Count.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limits: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:LIMits?')
		return Conversions.str_to_float(response)
