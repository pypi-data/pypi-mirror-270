from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodCls:
	"""Demod commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:BWIDth:DEMod \n
		Snippet: driver.applications.k6Pulse.sense.bandwidth.demod.set(bandwidth = 1.0) \n
		No command help available \n
			:param bandwidth: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:BWIDth:DEMod {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth:DEMod \n
		Snippet: value: float = driver.applications.k6Pulse.sense.bandwidth.demod.get() \n
		No command help available \n
			:return: bandwidth: Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:BWIDth:DEMod?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'DemodCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DemodCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
