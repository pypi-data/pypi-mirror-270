from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, arg_0: bool) -> None:
		"""SCPI: [SENSe]:MIXer:RFOVerrange[:STATe] \n
		Snippet: driver.applications.k40PhaseNoise.sense.mixer.rfOverrange.state.set(arg_0 = False) \n
		If enabled, the band limits are extended beyond 'RF Start' and 'RF Stop' due to the capabilities of the used harmonics. \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'SENSe:MIXer:RFOVerrange:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:MIXer:RFOVerrange[:STATe] \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.sense.mixer.rfOverrange.state.get() \n
		If enabled, the band limits are extended beyond 'RF Start' and 'RF Stop' due to the capabilities of the used harmonics. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:RFOVerrange:STATe?')
		return Conversions.str_to_bool(response)
