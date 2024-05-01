from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ShiftCls:
	"""Shift commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shift", core, parent)

	def set(self, distance: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:UPPer:SHIFt \n
		Snippet: driver.applications.k30NoiseFigure.calculate.limit.upper.shift.set(distance = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Moves a complete upper limit line vertically. Compared to defining an offset, this command actually changes the limit
		line definition points by the value you define. \n
			:param distance: Defines the distance that the limit line moves.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.decimal_value_to_str(distance)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:UPPer:SHIFt {param}')
