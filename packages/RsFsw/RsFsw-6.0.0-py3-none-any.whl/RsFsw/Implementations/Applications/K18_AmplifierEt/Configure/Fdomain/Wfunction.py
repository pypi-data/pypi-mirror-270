from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WfunctionCls:
	"""Wfunction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wfunction", core, parent)

	def set(self, method: enums.NoiseFigure) -> None:
		"""SCPI: CONFigure:FDOMain:WFUNction \n
		Snippet: driver.applications.k18AmplifierEt.configure.fdomain.wfunction.set(method = enums.NoiseFigure.BLACkharris) \n
		Defines the FFT window type. \n
			:param method: FLATtop | GAUSsian | RECTangular | P5 | BLACkharris
		"""
		param = Conversions.enum_scalar_to_str(method, enums.NoiseFigure)
		self._core.io.write(f'CONFigure:FDOMain:WFUNction {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.NoiseFigure:
		"""SCPI: CONFigure:FDOMain:WFUNction \n
		Snippet: value: enums.NoiseFigure = driver.applications.k18AmplifierEt.configure.fdomain.wfunction.get() \n
		Defines the FFT window type. \n
			:return: method: FLATtop | GAUSsian | RECTangular | P5 | BLACkharris"""
		response = self._core.io.query_str(f'CONFigure:FDOMain:WFUNction?')
		return Conversions.str_to_scalar_enum(response, enums.NoiseFigure)
