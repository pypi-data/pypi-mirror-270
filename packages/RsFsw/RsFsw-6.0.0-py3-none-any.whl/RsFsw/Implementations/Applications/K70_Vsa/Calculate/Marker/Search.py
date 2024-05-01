from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SearchCls:
	"""Search commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("search", core, parent)

	def set(self, mark_real_imag: enums.MarkerRealImagB, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:SEARch \n
		Snippet: driver.applications.k70Vsa.calculate.marker.search.set(mark_real_imag = enums.MarkerRealImagB.IMAG, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Selects the trace type a marker search is performed on. \n
			:param mark_real_imag: REAL Marker search functions are performed on the real trace of the 'I/Q' measurement. IMAG Marker search functions are performed on the imaginary trace of the 'I/Q' measurement. MAGN Marker search functions are performed on the magnitude of the I and Q data.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_scalar_to_str(mark_real_imag, enums.MarkerRealImagB)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SEARch {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> enums.MarkerRealImagB:
		"""SCPI: CALCulate<n>:MARKer<m>:SEARch \n
		Snippet: value: enums.MarkerRealImagB = driver.applications.k70Vsa.calculate.marker.search.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Selects the trace type a marker search is performed on. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: mark_real_imag: REAL Marker search functions are performed on the real trace of the 'I/Q' measurement. IMAG Marker search functions are performed on the imaginary trace of the 'I/Q' measurement. MAGN Marker search functions are performed on the magnitude of the I and Q data."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SEARch?')
		return Conversions.str_to_scalar_enum(response, enums.MarkerRealImagB)
