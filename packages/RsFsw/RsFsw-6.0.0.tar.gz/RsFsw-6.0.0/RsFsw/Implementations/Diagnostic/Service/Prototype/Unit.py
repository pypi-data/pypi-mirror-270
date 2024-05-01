from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UnitCls:
	"""Unit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	def set(self, unit_test: float) -> None:
		"""SCPI: DIAGnostic:SERVice:PROTotype:UNIT \n
		Snippet: driver.diagnostic.service.prototype.unit.set(unit_test = 1.0) \n
		No command help available \n
			:param unit_test: No help available
		"""
		param = Conversions.decimal_value_to_str(unit_test)
		self._core.io.write(f'DIAGnostic:SERVice:PROTotype:UNIT {param}')

	def get(self) -> float:
		"""SCPI: DIAGnostic:SERVice:PROTotype:UNIT \n
		Snippet: value: float = driver.diagnostic.service.prototype.unit.get() \n
		No command help available \n
			:return: unit_test: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:PROTotype:UNIT?')
		return Conversions.str_to_float(response)
