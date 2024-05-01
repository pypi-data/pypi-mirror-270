from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RrateCls:
	"""Rrate commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rrate", core, parent)

	@property
	def stepsize(self):
		"""stepsize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stepsize'):
			from .Stepsize import StepsizeCls
			self._stepsize = StepsizeCls(self._core, self._cmd_group)
		return self._stepsize

	def set(self, rate: float) -> None:
		"""SCPI: TRIGger[:SEQuence]:TIME:RRATe \n
		Snippet: driver.trigger.sequence.time.rrate.set(rate = 1.0) \n
		No command help available \n
			:param rate: No help available
		"""
		param = Conversions.decimal_value_to_str(rate)
		self._core.io.write(f'TRIGger:SEQuence:TIME:RRATe {param}')

	def get(self) -> float:
		"""SCPI: TRIGger[:SEQuence]:TIME:RRATe \n
		Snippet: value: float = driver.trigger.sequence.time.rrate.get() \n
		No command help available \n
			:return: rate: No help available"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:TIME:RRATe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'RrateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RrateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
