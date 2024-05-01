from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImaginaryCls:
	"""Imaginary commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("imaginary", core, parent)

	def set(self, imaginary: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:CSWeight:SHFRame<fr>:IMAGinary \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.sync.csWeight.shFrame.imaginary.set(imaginary = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param imaginary: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(imaginary)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:CSWeight:SHFRame50:IMAGinary {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:CSWeight:SHFRame<fr>:IMAGinary \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.sync.csWeight.shFrame.imaginary.get(carrierComponent = repcap.CarrierComponent.Default) \n
		No command help available \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: imaginary: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:CSWeight:SHFRame50:IMAGinary?')
		return Conversions.str_to_float(response)
