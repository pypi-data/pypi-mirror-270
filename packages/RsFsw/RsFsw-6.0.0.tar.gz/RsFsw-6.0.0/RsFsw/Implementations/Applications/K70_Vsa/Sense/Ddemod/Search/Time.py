from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimeCls:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, time: float) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:TIME \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.time.set(time = 1.0) \n
		No command help available \n
			:param time: No help available
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SENSe:DDEMod:SEARch:TIME {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DDEMod:SEARch:TIME \n
		Snippet: value: float = driver.applications.k70Vsa.sense.ddemod.search.time.get() \n
		No command help available \n
			:return: time: No help available"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:TIME?')
		return Conversions.str_to_float(response)
