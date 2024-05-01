from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CtModeCls:
	"""CtMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctMode", core, parent)

	def set(self, mode: enums.AutoManualMode) -> None:
		"""SCPI: [SENSe]:SWEep:CTMode \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.ctMode.set(mode = enums.AutoManualMode.AUTO) \n
		Selects the capture mode.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2-2 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.DfRange.set) . \n
			:param mode: AUTO Automatic determination of the capture time. MANual Manual definition of the capture time. Define the capture time with [SENSe:]SWEep:TIME.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualMode)
		self._core.io.write(f'SENSe:SWEep:CTMode {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoManualMode:
		"""SCPI: [SENSe]:SWEep:CTMode \n
		Snippet: value: enums.AutoManualMode = driver.applications.k14Xnr5G.sense.sweep.ctMode.get() \n
		Selects the capture mode.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select FR2-2 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.DfRange.set) . \n
			:return: mode: AUTO Automatic determination of the capture time. MANual Manual definition of the capture time. Define the capture time with [SENSe:]SWEep:TIME."""
		response = self._core.io.query_str(f'SENSe:SWEep:CTMode?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
