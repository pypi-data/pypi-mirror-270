from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:FRSPan:AUTO \n
		Snippet: driver.applications.k18AmplifierEt.configure.frSpan.auto.set(state = False) \n
		Defines how the span is determined that the frequency response is applied to for FSW-K18F result displays. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Defines the span manually using method RsFsw.Applications.K18_AmplifierEt.Configure.FrSpan.set. ON | 1 Defines the span automatically according to the calculated OBW of the reference file.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:FRSPan:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:FRSPan:AUTO \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.frSpan.auto.get() \n
		Defines how the span is determined that the frequency response is applied to for FSW-K18F result displays. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Defines the span manually using method RsFsw.Applications.K18_AmplifierEt.Configure.FrSpan.set. ON | 1 Defines the span automatically according to the calculated OBW of the reference file."""
		response = self._core.io.query_str(f'CONFigure:FRSPan:AUTO?')
		return Conversions.str_to_bool(response)
