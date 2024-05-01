from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SourceCls:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, if_source: enums.IfSource) -> None:
		"""SCPI: OUTPut:IF[:SOURce] \n
		Snippet: driver.applications.k18AmplifierEt.output.ifreq.source.set(if_source = enums.IfSource.HVIDeo) \n
		Defines the type of signal available at one of the output connectors of the FSW. For restrictions and more information
		see 'IF and video signal output'. \n
			:param if_source: IF The measured IF value is available at the IF/VIDEO/DEMOD output connector. The frequency at which the IF value is provided is defined using the method RsFsw.Applications.K9x_11ad.Output.Ifreq.IfFrequency.set command. IF2 The measured IF value is available at the 'IF OUT 2 GHz/ IF OUT 5 GHz' output connector at a frequency of 2 GHz. This setting is only available if the 'IF OUT 2 GHz/ IF OUT 5 GHz' connector or the optional 2 GHz / 5 GHz bandwidth extension (FSW-B2000/B5000) is available. It is automatically set if the optional 2 GHz / 5 GHz bandwidth extension (FSW-B2000/B5000) is installed and active. For details see 'Basics on the R&S FSW bandwidth extensions (R&S FSW-B2000/B5000 options) '. VIDeo The displayed video signal (i.e. the filtered and detected IF signal, 200mV) is available at the IF/VIDEO/DEMOD output connector. This setting is required to provide demodulated audio frequencies at the output.
		"""
		param = Conversions.enum_scalar_to_str(if_source, enums.IfSource)
		self._core.io.write(f'OUTPut:IF:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IfSource:
		"""SCPI: OUTPut:IF[:SOURce] \n
		Snippet: value: enums.IfSource = driver.applications.k18AmplifierEt.output.ifreq.source.get() \n
		Defines the type of signal available at one of the output connectors of the FSW. For restrictions and more information
		see 'IF and video signal output'. \n
			:return: if_source: No help available"""
		response = self._core.io.query_str(f'OUTPut:IF:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.IfSource)
