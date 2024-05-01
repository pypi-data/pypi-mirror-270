from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ResolutionCls:
	"""Resolution commands group definition. 5 total commands, 4 Subgroups, 1 group commands"""

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

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def ratio(self):
		"""ratio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ratio'):
			from .Ratio import RatioCls
			self._ratio = RatioCls(self._core, self._cmd_group)
		return self._ratio

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:BWIDth[:RESolution] \n
		Snippet: driver.applications.k10Xlte.sense.bandwidth.resolution.set(bandwidth = 1.0) \n
		Defines the resolution bandwidth and decouples the resolution bandwidth from the span. In the Real-Time application, the
		resolution bandwidth is always coupled to the span. For statistics measurements, this command defines the demodulation
		bandwidth. The 6 MHz Gaussian filter is provided for special measurements, such as 5G NR spurious emissions measurements.
		It is only available if you enter the value manually, not using the BAND:RES MAX command. It is not supported by all
		applications. \n
			:param bandwidth: refer to specifications document Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:BWIDth:RESolution {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth[:RESolution] \n
		Snippet: value: float = driver.applications.k10Xlte.sense.bandwidth.resolution.get() \n
		Defines the resolution bandwidth and decouples the resolution bandwidth from the span. In the Real-Time application, the
		resolution bandwidth is always coupled to the span. For statistics measurements, this command defines the demodulation
		bandwidth. The 6 MHz Gaussian filter is provided for special measurements, such as 5G NR spurious emissions measurements.
		It is only available if you enter the value manually, not using the BAND:RES MAX command. It is not supported by all
		applications. \n
			:return: bandwidth: refer to specifications document Unit: Hz"""
		response = self._core.io.query_str(f'SENSe:BWIDth:RESolution?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'ResolutionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ResolutionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
