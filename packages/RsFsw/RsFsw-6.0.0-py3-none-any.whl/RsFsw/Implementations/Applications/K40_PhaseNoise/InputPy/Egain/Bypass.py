from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BypassCls:
	"""Bypass commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bypass", core, parent)

	def set(self, arg_0: bool) -> None:
		"""SCPI: INPut:EGAin:BYPass \n
		Snippet: driver.applications.k40PhaseNoise.inputPy.egain.bypass.set(arg_0 = False) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'INPut:EGAin:BYPass {param}')

	def get(self) -> bool:
		"""SCPI: INPut:EGAin:BYPass \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.inputPy.egain.bypass.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'INPut:EGAin:BYPass?')
		return Conversions.str_to_bool(response)
