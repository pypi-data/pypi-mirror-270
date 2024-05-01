from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpacingCls:
	"""Spacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spacing", core, parent)

	def set(self, interpol_mode: enums.ScalingMode, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:CONTrol:SPACing \n
		Snippet: driver.calculate.limit.control.spacing.set(interpol_mode = enums.ScalingMode.LINear, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Selects linear or logarithmic interpolation for the calculation of limit lines from one horizontal point to the next. \n
			:param interpol_mode: LINear | LOGarithmic
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.enum_scalar_to_str(interpol_mode, enums.ScalingMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CONTrol:SPACing {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> enums.ScalingMode:
		"""SCPI: CALCulate<n>:LIMit<li>:CONTrol:SPACing \n
		Snippet: value: enums.ScalingMode = driver.calculate.limit.control.spacing.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Selects linear or logarithmic interpolation for the calculation of limit lines from one horizontal point to the next. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: interpol_mode: LINear | LOGarithmic"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CONTrol:SPACing?')
		return Conversions.str_to_scalar_enum(response, enums.ScalingMode)
