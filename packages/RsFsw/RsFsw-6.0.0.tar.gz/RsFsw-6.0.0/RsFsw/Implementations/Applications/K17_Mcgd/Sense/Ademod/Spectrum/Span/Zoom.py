from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ZoomCls:
	"""Zoom commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zoom", core, parent)

	def set(self, value: float) -> None:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN:ZOOM \n
		Snippet: driver.applications.k17Mcgd.sense.ademod.spectrum.span.zoom.set(value = 1.0) \n
		Sets the span (around the center frequency) for RF spectrum result display. The span is limited to the demodulation
		bandwidth (see [SENSe:]BWIDth:DEMod) . \n
			:param value: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'SENSe:ADEMod:SPECtrum:SPAN:ZOOM {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:SPECtrum:SPAN:ZOOM \n
		Snippet: value: float = driver.applications.k17Mcgd.sense.ademod.spectrum.span.zoom.get() \n
		Sets the span (around the center frequency) for RF spectrum result display. The span is limited to the demodulation
		bandwidth (see [SENSe:]BWIDth:DEMod) . \n
			:return: value: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SPECtrum:SPAN:ZOOM?')
		return Conversions.str_to_float(response)
