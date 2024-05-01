from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HighCls:
	"""High commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("high", core, parent)

	def set(self, bias_high: float) -> None:
		"""SCPI: [SENSe]:MIXer:BIAS:HIGH \n
		Snippet: driver.applications.k9X11Ad.sense.mixer.bias.high.set(bias_high = 1.0) \n
		Defines the bias current for the high (last) range. . Is only available if the external mixer is active (see
		[SENSe:]MIXer<x>[:STATe]) . \n
			:param bias_high: No help available
		"""
		param = Conversions.decimal_value_to_str(bias_high)
		self._core.io.write(f'SENSe:MIXer:BIAS:HIGH {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:MIXer:BIAS:HIGH \n
		Snippet: value: float = driver.applications.k9X11Ad.sense.mixer.bias.high.get() \n
		Defines the bias current for the high (last) range. . Is only available if the external mixer is active (see
		[SENSe:]MIXer<x>[:STATe]) . \n
			:return: bias_high: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:BIAS:HIGH?')
		return Conversions.str_to_float(response)
