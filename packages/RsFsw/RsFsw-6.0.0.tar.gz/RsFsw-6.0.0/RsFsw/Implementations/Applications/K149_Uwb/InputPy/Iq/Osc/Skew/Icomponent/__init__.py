from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IcomponentCls:
	"""Icomponent commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("icomponent", core, parent)

	@property
	def inverted(self):
		"""inverted commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inverted'):
			from .Inverted import InvertedCls
			self._inverted = InvertedCls(self._core, self._cmd_group)
		return self._inverted

	def set(self, value: float) -> None:
		"""SCPI: INPut:IQ:OSC:SKEW:I \n
		Snippet: driver.applications.k149Uwb.inputPy.iq.osc.skew.icomponent.set(value = 1.0) \n
		Compensates for skewed values in the positive I path, e.g. due to different input cables. \n
			:param value: Unit: S
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'INPut:IQ:OSC:SKEW:I {param}')

	def get(self) -> float:
		"""SCPI: INPut:IQ:OSC:SKEW:I \n
		Snippet: value: float = driver.applications.k149Uwb.inputPy.iq.osc.skew.icomponent.get() \n
		Compensates for skewed values in the positive I path, e.g. due to different input cables. \n
			:return: value: Unit: S"""
		response = self._core.io.query_str(f'INPut:IQ:OSC:SKEW:I?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'IcomponentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IcomponentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
