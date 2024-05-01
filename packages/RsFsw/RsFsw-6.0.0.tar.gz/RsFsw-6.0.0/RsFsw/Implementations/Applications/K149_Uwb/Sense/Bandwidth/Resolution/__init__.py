from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResolutionCls:
	"""Resolution commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("resolution", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth[:RESolution] \n
		Snippet: value: float = driver.applications.k149Uwb.sense.bandwidth.resolution.get() \n
		Defines the resolution bandwidth and decouples the resolution bandwidth from the span. In the Real-Time application, the
		resolution bandwidth is always coupled to the span. For statistics measurements, this command defines the demodulation
		bandwidth. The 6 MHz Gaussian filter is provided for special measurements, such as 5G NR spurious emissions measurements.
		It is only available if you enter the value manually, not using the BAND:RES MAX command. It is not supported by all
		applications. \n
			:return: span: No help available"""
		response = self._core.io.query_str(f'SENSe:BWIDth:RESolution?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'ResolutionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResolutionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
