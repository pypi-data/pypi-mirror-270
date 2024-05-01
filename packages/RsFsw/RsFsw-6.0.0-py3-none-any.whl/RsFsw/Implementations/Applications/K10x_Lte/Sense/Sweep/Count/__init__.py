from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CountCls:
	"""Count commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import CurrentCls
			self._current = CurrentCls(self._core, self._cmd_group)
		return self._current

	def set(self, sweep_count: float) -> None:
		"""SCPI: [SENSe]:SWEep:COUNt \n
		Snippet: driver.applications.k10Xlte.sense.sweep.count.set(sweep_count = 1.0) \n
		Defines the number of sweeps that the application uses to average traces. (For Pulse measurements, ) . In continuous
		sweep mode, the application calculates the moving average over the average count. In single sweep mode, the application
		stops the measurement and calculates the average after the average count has been reached. \n
			:param sweep_count: When you set a sweep count of 0 or 1, the FSW performs one single sweep in single sweep mode. In continuous sweep mode, if the sweep count is set to 0, a moving average over 10 sweeps is performed. Range: 0 to 200000
		"""
		param = Conversions.decimal_value_to_str(sweep_count)
		self._core.io.write(f'SENSe:SWEep:COUNt {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:SWEep:COUNt \n
		Snippet: value: float = driver.applications.k10Xlte.sense.sweep.count.get() \n
		Defines the number of sweeps that the application uses to average traces. (For Pulse measurements, ) . In continuous
		sweep mode, the application calculates the moving average over the average count. In single sweep mode, the application
		stops the measurement and calculates the average after the average count has been reached. \n
			:return: sweep_count: When you set a sweep count of 0 or 1, the FSW performs one single sweep in single sweep mode. In continuous sweep mode, if the sweep count is set to 0, a moving average over 10 sweeps is performed. Range: 0 to 200000"""
		response = self._core.io.query_str(f'SENSe:SWEep:COUNt?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'CountCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CountCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
