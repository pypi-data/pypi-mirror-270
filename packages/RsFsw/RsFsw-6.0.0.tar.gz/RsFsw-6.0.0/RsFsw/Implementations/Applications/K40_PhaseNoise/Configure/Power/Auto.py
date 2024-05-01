from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AutoCls:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, arg_0: bool) -> None:
		"""SCPI: CONFigure:POWer:AUTO \n
		Snippet: driver.applications.k40PhaseNoise.configure.power.auto.set(arg_0 = False) \n
		Is used to switch on or off automatic power level detection. \n
			:param arg_0: ON Automatic power level detection is performed at the start of each measurement sweep, and the reference level is adapted accordingly. OFF The reference level must be defined manually (see method RsFsw.Applications.K60_Transient.Display.Window.Trace.Y.Scale.RefLevel.set) ONCE Automatic power level detection is performed once at the start of the next measurement sweep, and the reference level is adapted accordingly. The command with this parameter corresponds to [SENSe:]ADJust:LEVel.
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'CONFigure:POWer:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:POWer:AUTO \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.configure.power.auto.get() \n
		Is used to switch on or off automatic power level detection. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'CONFigure:POWer:AUTO?')
		return Conversions.str_to_bool(response)
