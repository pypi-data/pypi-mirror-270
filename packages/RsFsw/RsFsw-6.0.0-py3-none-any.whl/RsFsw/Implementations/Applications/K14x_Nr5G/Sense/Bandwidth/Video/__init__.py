from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VideoCls:
	"""Video commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("video", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import AutoCls
			self._auto = AutoCls(self._core, self._cmd_group)
		return self._auto

	@property
	def ratio(self):
		"""ratio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ratio'):
			from .Ratio import RatioCls
			self._ratio = RatioCls(self._core, self._cmd_group)
		return self._ratio

	def set(self, bandwidth: float) -> None:
		"""SCPI: [SENSe]:BWIDth:VIDeo \n
		Snippet: driver.applications.k14Xnr5G.sense.bandwidth.video.set(bandwidth = 1.0) \n
		Defines the video bandwidth. The command decouples the video bandwidth from the resolution bandwidths. \n
			:param bandwidth: refer to specifications document Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'SENSe:BWIDth:VIDeo {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:BWIDth:VIDeo \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.bandwidth.video.get() \n
		Defines the video bandwidth. The command decouples the video bandwidth from the resolution bandwidths. \n
			:return: bandwidth: refer to specifications document Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:BWIDth:VIDeo?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'VideoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = VideoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
