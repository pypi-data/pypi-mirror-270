from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DataCls:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, chirp_rate: List[float] = None, tolerance: List[float] = None, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:STATes[:DATA] \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.states.data.set(chirp_rate = [1.1, 2.2, 3.3], tolerance = [1.1, 2.2, 3.3], window = repcap.Window.Default) \n
		Sets and queries the chirp state detection table. It consists of a comma-separated list of value pairs, one for each
		possible chirp state. The parameters that can be set in the chirp state detection table depend on the chirp settings
		defined using method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.States.Auto.set and the chirp detection mode
		defined using method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.Detection.set:
			Table Header:  \n
			- Chirp Settings 'Auto' / Chirp Settings 'Manual'
			- Chirp Detection 'On' / All parameters are set automatically. / Manual setting of:
			- Chirp Detection 'Off' / Manual setting of: / Manual setting of: \n
			:param chirp_rate: numeric value Unit: Hz/us
			:param tolerance: numeric value Tolerance above or below the nominal chirp rate. Unit: Hz/us
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('chirp_rate', chirp_rate, DataType.FloatList, None, True, True, 1), ArgSingle('tolerance', tolerance, DataType.FloatList, None, True, True, 1))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:STATes:DATA {param}'.rstrip())

	# noinspection PyTypeChecker
	class DataStruct(StructBase):
		"""Response structure. Fields: \n
			- Chirp_Rate: List[float]: numeric value Unit: Hz/us
			- Tolerance: List[float]: numeric value Tolerance above or below the nominal chirp rate. Unit: Hz/us"""
		__meta_args_list = [
			ArgStruct('Chirp_Rate', DataType.FloatList, None, False, True, 1),
			ArgStruct('Tolerance', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Chirp_Rate: List[float] = None
			self.Tolerance: List[float] = None

	def get(self, window=repcap.Window.Default) -> DataStruct:
		"""SCPI: CALCulate<n>:CHRDetection:STATes[:DATA] \n
		Snippet: value: DataStruct = driver.applications.k60Transient.calculate.chrDetection.states.data.get(window = repcap.Window.Default) \n
		Sets and queries the chirp state detection table. It consists of a comma-separated list of value pairs, one for each
		possible chirp state. The parameters that can be set in the chirp state detection table depend on the chirp settings
		defined using method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.States.Auto.set and the chirp detection mode
		defined using method RsFsw.Applications.K60_Transient.Calculate.ChrDetection.Detection.set:
			Table Header:  \n
			- Chirp Settings 'Auto' / Chirp Settings 'Manual'
			- Chirp Detection 'On' / All parameters are set automatically. / Manual setting of:
			- Chirp Detection 'Off' / Manual setting of: / Manual setting of: \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: structure: for return value, see the help for DataStruct structure arguments."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		return self._core.io.query_struct(f'CALCulate{window_cmd_val}:CHRDetection:STATes:DATA?', self.__class__.DataStruct())
