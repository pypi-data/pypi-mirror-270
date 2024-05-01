from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:BURSt:SELect \n
		Snippet: driver.applications.k91Wlan.sense.burst.select.set(value = 1.0) \n
		If single PPDU analysis is enabled (see [SENSe:]BURSt:SELect:STATe) , the WLAN 802.11 I/Q results are based on the
		specified PPDU. If disabled, all detected PPDUs in the current capture buffer are evaluated. \n
			:param value: integer
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:BURSt:SELect {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BURSt:SELect \n
		Snippet: value: float = driver.applications.k91Wlan.sense.burst.select.get() \n
		If single PPDU analysis is enabled (see [SENSe:]BURSt:SELect:STATe) , the WLAN 802.11 I/Q results are based on the
		specified PPDU. If disabled, all detected PPDUs in the current capture buffer are evaluated. \n
			:return: value: integer"""
		response = self._core.io.query_str(f'SENSe:BURSt:SELect?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'SelectCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SelectCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
