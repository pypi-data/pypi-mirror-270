from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.AutoManualUserMode, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<m>:ESPectrum:MODE \n
		Snippet: driver.applications.k149Uwb.calculate.limit.espectrum.mode.set(mode = enums.AutoManualUserMode.AUTO, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Which limit line is to be used for an SEM measurement depends on the power class the input signal power belongs to. This
		command defines wether the power class is determined automatically or manually. \n
			:param mode: AUTO The power class (and thus the limit line) is assigned dynamically according to the currently measured channel power. MANUAL One of the specified power classes is selected manually for the entire measurement. The selection is made with the method RsFsw.Calculate.Limit.Espectrum.Pclass.Exclusive.set command.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualUserMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> enums.AutoManualUserMode:
		"""SCPI: CALCulate<n>:LIMit<m>:ESPectrum:MODE \n
		Snippet: value: enums.AutoManualUserMode = driver.applications.k149Uwb.calculate.limit.espectrum.mode.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Which limit line is to be used for an SEM measurement depends on the power class the input signal power belongs to. This
		command defines wether the power class is determined automatically or manually. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: mode: AUTO The power class (and thus the limit line) is assigned dynamically according to the currently measured channel power. MANUAL One of the specified power classes is selected manually for the entire measurement. The selection is made with the method RsFsw.Calculate.Limit.Espectrum.Pclass.Exclusive.set command."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualUserMode)
