from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePyCls:
	"""TypePy commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	@property
	def used(self):
		"""used commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_used'):
			from .Used import UsedCls
			self._used = UsedCls(self._core, self._cmd_group)
		return self._used

	def set(self, type_py: enums.SweepType) -> None:
		"""SCPI: [SENSe]:SWEep:TYPE \n
		Snippet: driver.sense.sweep.typePy.set(type_py = enums.SweepType.AUTO) \n
		Selects the sweep type. \n
			:param type_py: AUTO Automatic selection of the sweep type between sweep mode and FFT. FFT FFT mode SWE Sweep list
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.SweepType)
		self._core.io.write(f'SENSe:SWEep:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepType:
		"""SCPI: [SENSe]:SWEep:TYPE \n
		Snippet: value: enums.SweepType = driver.sense.sweep.typePy.get() \n
		Selects the sweep type. \n
			:return: type_py: AUTO Automatic selection of the sweep type between sweep mode and FFT. FFT FFT mode SWE Sweep list"""
		response = self._core.io.query_str(f'SENSe:SWEep:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.SweepType)

	def clone(self) -> 'TypePyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TypePyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
