from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class YCls:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def set(self, yaxis: enums.XaXisPmSettling, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:HOP:PMSettling:Y \n
		Snippet: driver.applications.k60Transient.calculate.trend.hop.pmSettling.y.set(yaxis = enums.XaXisPmSettling.PMSLength, window = repcap.Window.Default) \n
		Configures the y-axis of the Parameter Trend result display for hop PM settling parameters. \n
			:param yaxis: PMSLength | PMSPoint | PMSTime PMSPoint PM settling point PMSTime PM settling time PMSLength PM settled length
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(yaxis, enums.XaXisPmSettling)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:HOP:PMSettling:Y {param}')
