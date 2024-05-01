from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MtimeCls:
	"""Mtime commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtime", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	def set(self, meas_time: float) -> None:
		"""SCPI: [SENSe]:ADEMod:MTIMe \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.mtime.set(meas_time = 1.0) \n
		Defines the measurement time for Analog Modulation Analysis. \n
			:param meas_time: Unit: S
		"""
		param = Conversions.decimal_value_to_str(meas_time)
		self._core.io.write(f'SENSe:ADEMod:MTIMe {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:MTIMe \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.ademod.mtime.get() \n
		Defines the measurement time for Analog Modulation Analysis. \n
			:return: meas_time: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:MTIMe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'MtimeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MtimeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
