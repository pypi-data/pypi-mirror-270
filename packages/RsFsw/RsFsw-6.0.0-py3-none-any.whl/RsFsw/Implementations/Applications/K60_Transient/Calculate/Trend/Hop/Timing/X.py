from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class XCls:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def set(self, xaxis: enums.AxisHopTiming, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:HOP:TIMing:X \n
		Snippet: driver.applications.k60Transient.calculate.trend.hop.timing.x.set(xaxis = enums.AxisHopTiming.BEGin, window = repcap.Window.Default) \n
		Configures the x-axis of the Parameter Trend result display for hop timing parameters. \n
			:param xaxis: BEGin | DWELl | SWITching BEGin Hop Begin DWELl Hop dwell time SWITching Switching time
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(xaxis, enums.AxisHopTiming)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:HOP:TIMing:X {param}')
