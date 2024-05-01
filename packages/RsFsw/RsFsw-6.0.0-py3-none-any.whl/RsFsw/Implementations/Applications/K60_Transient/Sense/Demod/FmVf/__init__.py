from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FmVfCls:
	"""FmVf commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmVf", core, parent)

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	def set(self, percentage: float) -> None:
		"""SCPI: [SENSe]:DEMod:FMVF \n
		Snippet: driver.applications.k60Transient.sense.demod.fmVf.set(percentage = 1.0) \n
		No command help available \n
			:param percentage: No help available
		"""
		param = Conversions.decimal_value_to_str(percentage)
		self._core.io.write(f'SENSe:DEMod:FMVF {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:FMVF \n
		Snippet: value: float = driver.applications.k60Transient.sense.demod.fmVf.get() \n
		No command help available \n
			:return: percentage: No help available"""
		response = self._core.io.query_str(f'SENSe:DEMod:FMVF?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'FmVfCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FmVfCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
