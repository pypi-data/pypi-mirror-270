from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import YCls
			self._y = YCls(self._core, self._cmd_group)
		return self._y

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import XCls
			self._x = XCls(self._core, self._cmd_group)
		return self._x

	def set(self, yaxis: enums.PulsePowerItems, xaxis: enums.PulseAxisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:POWer \n
		Snippet: driver.applications.k6Pulse.calculate.trend.power.set(yaxis = enums.PulsePowerItems.ADDB, xaxis = enums.PulseAxisItems.DCYCle, window = repcap.Window.Default) \n
		Configures the Parameter Trend result display for time trends. This command defines both x-axis and y-axis parameters in
		one step. It is equivalent to the two subsequent commands: CALCulate<n>:TRENd:TIMing:X TSTamp | PNUMber (see method RsFsw.
		Applications.K6_Pulse.Calculate.Trend.Timing.X.set) CALCulate<n>:TRENd:POWer:Y <YAxis> (see method RsFsw.Applications.
		K6_Pulse.Calculate.Trend.Power.Y.set) \n
			:param yaxis: TOP | BASE | AMPLitude | ON | AVG | MIN | MAX | PON | PAVG | PMIN | ADPercent | ADDB | RPERcent | RDB | OPERcent | ODB | POINt | PPRatio | I | Q Pulse parameter to be displayed on the y-axis. For a description of the available parameters see 'Power/amplitude parameters'. TOP Top Power BASE Base Power AMPLitude Pulse Amplitude ON Average ON Power AVG Average Tx Power MIN Minimum Power MAX Peak Power PON Peak-to-Avg ON Power Ratio PAVG Peak-to-Average Tx Power Ratio PMIN Peak-to-Min Power Ratio ADPercent Droop in % ADDB Droop in dB RPERcent Ripple in % RDB Ripple in dB OPERcent Overshoot in % ODB Overshoot in dB POINt Pulse power measured at measurement point PPRatio Pulse-to-Pulse Power Difference
			:param xaxis: PNUMber | TSTamp | SETTling | RISE | FALL | PWIDth | OFF | DRATio | DCYCle | PRI | PRF Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Timing parameters'. TSTamp Timestamp PNUMber The pulse numbers are represented on the x-axis (available numbers can be queried using [SENSe:]PULSe:NUMBer?) . Intervals without pulses are not displayed. SETTling Settling Time RISE Rise Time FALL Fall Time PWIDth Pulse Width (ON Time) OFF Off Time DRATio Duty Ratio DCYCle Duty Cycle (%) PRI Pulse Repetition Interval PRF Pulse Repetition Frequency (Hz)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('yaxis', yaxis, DataType.Enum, enums.PulsePowerItems), ArgSingle('xaxis', xaxis, DataType.Enum, enums.PulseAxisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:POWer {param}'.rstrip())

	def clone(self) -> 'PowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
