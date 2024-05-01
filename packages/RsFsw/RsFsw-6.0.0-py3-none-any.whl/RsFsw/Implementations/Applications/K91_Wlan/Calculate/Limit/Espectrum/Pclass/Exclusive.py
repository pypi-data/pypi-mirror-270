from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExclusiveCls:
	"""Exclusive commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("exclusive", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, powerClass=repcap.PowerClass.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:PCLass<pc>[:EXCLusive] \n
		Snippet: driver.applications.k91Wlan.calculate.limit.espectrum.pclass.exclusive.set(state = False, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, powerClass = repcap.PowerClass.Default) \n
		Selects the power class used by the measurement if method RsFsw.Calculate.Limit.Espectrum.Mode.set is set to manual. Note
		that:
			INTRO_CMD_HELP: Prerequisites for this command: \n
			- You can only use power classes for which limits are defined. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:PCLass{powerClass_cmd_val}:EXCLusive {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, powerClass=repcap.PowerClass.Default) -> bool:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:PCLass<pc>[:EXCLusive] \n
		Snippet: value: bool = driver.applications.k91Wlan.calculate.limit.espectrum.pclass.exclusive.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, powerClass = repcap.PowerClass.Default) \n
		Selects the power class used by the measurement if method RsFsw.Calculate.Limit.Espectrum.Mode.set is set to manual. Note
		that:
			INTRO_CMD_HELP: Prerequisites for this command: \n
			- You can only use power classes for which limits are defined. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:PCLass{powerClass_cmd_val}:EXCLusive?')
		return Conversions.str_to_bool(response)
