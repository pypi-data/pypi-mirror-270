from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GainCls:
	"""Gain commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def set(self, level: float) -> None:
		"""SCPI: INPut:GAIN \n
		Snippet: driver.applications.k149Uwb.inputPy.gain.set(level = 1.0) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'INPut:GAIN {param}')

	def get(self) -> float:
		"""SCPI: INPut:GAIN \n
		Snippet: value: float = driver.applications.k149Uwb.inputPy.gain.get() \n
		No command help available \n
			:return: level: No help available"""
		response = self._core.io.query_str(f'INPut:GAIN?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'GainCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GainCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
