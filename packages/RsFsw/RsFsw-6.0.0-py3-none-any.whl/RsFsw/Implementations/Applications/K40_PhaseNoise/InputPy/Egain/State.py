from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, arg_0: bool) -> None:
		"""SCPI: INPut:EGAin[:STATe] \n
		Snippet: driver.applications.k40PhaseNoise.inputPy.egain.state.set(arg_0 = False) \n
		Before this command can be used, the external preamplifier must be connected to the FSW. See the preamplifier's
		documentation for details. When activated, the FSW automatically compensates the magnitude and phase characteristics of
		the external preamplifier in the measurement results. Note that when an optional external preamplifier is activated, the
		internal preamplifier is automatically disabled, and vice versa. For FSW85 models with two RF inputs, you must enable
		correction from the external preamplifier for each input individually. Correction cannot be enabled for both inputs at
		the same time. When deactivated, no compensation is performed even if an external preamplifier remains connected. \n
			:param arg_0: ON | OFF | 0 | 1 OFF | 0 No data correction is performed based on the external preamplifier ON | 1 Performs data corrections based on the external preamplifier
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'INPut:EGAin:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:EGAin[:STATe] \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.inputPy.egain.state.get() \n
		Before this command can be used, the external preamplifier must be connected to the FSW. See the preamplifier's
		documentation for details. When activated, the FSW automatically compensates the magnitude and phase characteristics of
		the external preamplifier in the measurement results. Note that when an optional external preamplifier is activated, the
		internal preamplifier is automatically disabled, and vice versa. For FSW85 models with two RF inputs, you must enable
		correction from the external preamplifier for each input individually. Correction cannot be enabled for both inputs at
		the same time. When deactivated, no compensation is performed even if an external preamplifier remains connected. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'INPut:EGAin:STATe?')
		return Conversions.str_to_bool(response)
