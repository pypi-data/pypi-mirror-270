from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeakCls:
	"""Peak commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peak", core, parent)

	def set(self, filename: str, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:PEAK \n
		Snippet: driver.applications.k10Xlte.massMemory.store.peak.set(filename = 'abc', store = repcap.Store.Default) \n
		Exports the marker peak list to a file. Secure User Mode In secure user mode, settings that are stored on the instrument
		are stored to volatile memory, which is restricted to 256 MB. Thus, a 'memory limit reached' error can occur although the
		hard disk indicates that storage space is still available. To store data permanently, select an external storage location
		such as a USB memory device. For details, see 'Protecting data using the secure user mode'. \n
			:param filename: String containing the path,name and extension of the target file.
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.value_to_quoted_str(filename)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:PEAK {param}')

	def get(self, store=repcap.Store.Default) -> str:
		"""SCPI: MMEMory:STORe<n>:PEAK \n
		Snippet: value: str = driver.applications.k10Xlte.massMemory.store.peak.get(store = repcap.Store.Default) \n
		Exports the marker peak list to a file. Secure User Mode In secure user mode, settings that are stored on the instrument
		are stored to volatile memory, which is restricted to 256 MB. Thus, a 'memory limit reached' error can occur although the
		hard disk indicates that storage space is still available. To store data permanently, select an external storage location
		such as a USB memory device. For details, see 'Protecting data using the secure user mode'. \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: filename: String containing the path,name and extension of the target file."""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		response = self._core.io.query_str(f'MMEMory:STORe{store_cmd_val}:PEAK?')
		return trim_str_response(response)
