from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PathCls:
	"""Path commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	def set(self, data: str) -> None:
		"""SCPI: CONFigure:POWer:AUTO:CALibration:DATA:PATH \n
		Snippet: driver.applications.k91Wlan.configure.power.auto.calibration.data.path.set(data = 'abc') \n
		No command help available \n
			:param data: No help available
		"""
		param = Conversions.value_to_quoted_str(data)
		self._core.io.write(f'CONFigure:POWer:AUTO:CALibration:DATA:PATH {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:POWer:AUTO:CALibration:DATA:PATH \n
		Snippet: value: str = driver.applications.k91Wlan.configure.power.auto.calibration.data.path.get() \n
		No command help available \n
			:return: data: No help available"""
		response = self._core.io.query_str(f'CONFigure:POWer:AUTO:CALibration:DATA:PATH?')
		return trim_str_response(response)
