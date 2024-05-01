from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrototypeCls:
	"""Prototype commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prototype", core, parent)

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import UnitCls
			self._unit = UnitCls(self._core, self._cmd_group)
		return self._unit

	def set(self, param_name: bool) -> None:
		"""SCPI: DIAGnostic:SERVice:PROTotype \n
		Snippet: driver.diagnostic.service.prototype.set(param_name = False) \n
		No command help available \n
			:param param_name: No help available
		"""
		param = Conversions.bool_to_str(param_name)
		self._core.io.write(f'DIAGnostic:SERVice:PROTotype {param}')

	def get(self) -> bool:
		"""SCPI: DIAGnostic:SERVice:PROTotype \n
		Snippet: value: bool = driver.diagnostic.service.prototype.get() \n
		No command help available \n
			:return: param_name: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:PROTotype?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'PrototypeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrototypeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
