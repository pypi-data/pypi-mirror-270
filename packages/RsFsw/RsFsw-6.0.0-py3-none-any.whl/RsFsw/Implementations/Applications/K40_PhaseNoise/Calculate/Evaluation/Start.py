from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StartCls:
	"""Start commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("start", core, parent)

	def set(self, offset_frequency: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:EVALuation:STARt \n
		Snippet: driver.applications.k40PhaseNoise.calculate.evaluation.start.set(offset_frequency = 1.0, window = repcap.Window.Default) \n
		Defines the start point of the residual noise integration range. Before you can use the command, you have to turn on the
		measurement range integration with method RsFsw.Applications.K40_PhaseNoise.Calculate.Evaluation.State.set. \n
			:param offset_frequency: The minimum offset is 1 Hz. The maximum offset depends on the hardware you are using. Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(offset_frequency)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:EVALuation:STARt {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:EVALuation:STARt \n
		Snippet: value: float = driver.applications.k40PhaseNoise.calculate.evaluation.start.get(window = repcap.Window.Default) \n
		Defines the start point of the residual noise integration range. Before you can use the command, you have to turn on the
		measurement range integration with method RsFsw.Applications.K40_PhaseNoise.Calculate.Evaluation.State.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: offset_frequency: The minimum offset is 1 Hz. The maximum offset depends on the hardware you are using. Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:EVALuation:STARt?')
		return Conversions.str_to_float(response)
