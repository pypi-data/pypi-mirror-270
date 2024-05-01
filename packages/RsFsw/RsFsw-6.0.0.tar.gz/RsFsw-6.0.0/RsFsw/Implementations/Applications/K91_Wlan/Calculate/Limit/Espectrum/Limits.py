from typing import List

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

	def set(self, limit: List[float], window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:LIMits \n
		Snippet: driver.applications.k91Wlan.calculate.limit.espectrum.limits.set(limit = [1.1, 2.2, 3.3], window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command sets or queries up to 4 power classes in one step. You can only define values for the number of power
		classes defined by method RsFsw.Calculate.Limit.Espectrum.Pclass.Count.set. \n
			:param limit: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.list_to_csv_str(limit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:LIMits {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> List[float]:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:LIMits \n
		Snippet: value: List[float] = driver.applications.k91Wlan.calculate.limit.espectrum.limits.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command sets or queries up to 4 power classes in one step. You can only define values for the number of power
		classes defined by method RsFsw.Calculate.Limit.Espectrum.Pclass.Count.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limit: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_bin_or_ascii_float_list(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:LIMits?')
		return response
