from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import XCls
			self._x = XCls(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import YCls
			self._y = YCls(self._core, self._cmd_group)
		return self._y

	def set(self, yaxis: enums.AxisFreqItems, xaxis: enums.ChirpXaxisItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:CHIRp:FREQuency \n
		Snippet: driver.applications.k60Transient.calculate.trend.chirp.frequency.set(yaxis = enums.AxisFreqItems.AVGFm, xaxis = enums.ChirpXaxisItems.AVGFm, window = repcap.Window.Default) \n
		Configures the x-axis and y-axis of the Parameter Trend result display for chirp trends over time. \n
			:param yaxis: AVGFm | AVGNonlinear | BWIDth | CHERror | FREQuency | MAXFm | MAXNonlinear | RMSFm | RMSNonlinear CHERror Chirp state deviation FREQuency Average frequency MAXFm Maximum Frequency Deviation RMSFm RMS Frequency Deviation AVGFm Average Frequency Deviation BWIDth Bandwidth AVGNonlinear Average frequency non-linearity RMSNonlinear RMS frequency non-linearity MAXNonlinear Peak frequency non-linearity
			:param xaxis: AVGFm | AVGNonlinear | CHERror | FREQuency | MAXFm | MAXNonlinear | RMSFm | RMSNonlinear | FMSLength | FMSPoint | FMSTime | AVPHm | MXPHm | RMSPm | PMSLength | PMSPoint | PMSTime | AVGPower | MAXPower | MINPower | PWRRipple | INDex | BEGin CHERror Chirp state deviation FREQuency Average frequency MAXFm Maximum Frequency Deviation RMSFm RMS Frequency Deviation AVGFm Average Frequency Deviation FMSPoint FM settling point FMSTime FM settling time FMSLength FM settled length BWIDth Bandwidth AVGNonlinear Average frequency non-linearity RMSNonlinear RMS frequency non-linearity MAXNonlinear Peak frequency non-linearity PMSPoint PM settling point PMSTime PM settling time PMSLength PM settled length BEGin Chirp Begin LENGth Chirp length RATe Chirp rate AVGPower Average power MINPower Minimum power MAXPower Maximum power PWRRipple Power ripple PWRRipple Power ripple
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('yaxis', yaxis, DataType.Enum, enums.AxisFreqItems), ArgSingle('xaxis', xaxis, DataType.Enum, enums.ChirpXaxisItems))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:CHIRp:FREQuency {param}'.rstrip())

	def clone(self) -> 'FrequencyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FrequencyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
