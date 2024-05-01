from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SareaCls:
	"""Sarea commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sarea", core, parent)

	def set(self, search_area: enums.SearchArea, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer:SPECtrogram:SARea \n
		Snippet: driver.applications.k60Transient.calculate.marker.spectrogram.sarea.set(search_area = enums.SearchArea.MEMory, window = repcap.Window.Default) \n
		Defines the marker search area for all spectrogram markers in the channel. \n
			:param search_area: VISible Performs a search within the visible frames. Note that the command does not work if the spectrogram is not visible for any reason (e.g. if the display update is off) . MEMory Performs a search within all frames in the memory.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(search_area, enums.SearchArea)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer:SPECtrogram:SARea {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.SearchArea:
		"""SCPI: CALCulate<n>:MARKer:SPECtrogram:SARea \n
		Snippet: value: enums.SearchArea = driver.applications.k60Transient.calculate.marker.spectrogram.sarea.get(window = repcap.Window.Default) \n
		Defines the marker search area for all spectrogram markers in the channel. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: search_area: VISible Performs a search within the visible frames. Note that the command does not work if the spectrogram is not visible for any reason (e.g. if the display update is off) . MEMory Performs a search within all frames in the memory."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer:SPECtrogram:SARea?')
		return Conversions.str_to_scalar_enum(response, enums.SearchArea)
