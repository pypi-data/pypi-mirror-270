from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CbIndexCls:
	"""CbIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbIndex", core, parent)

	def set(self, code_book_index: float, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:PRECoding:CBINdex \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.precoding.cbIndex.set(code_book_index = 1.0, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		Selects the codebook index for a PUSCH allocation. \n
			:param code_book_index: Range: 0 to 5
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
		"""
		param = Conversions.decimal_value_to_str(code_book_index)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:PRECoding:CBINdex {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:PRECoding:CBINdex \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.precoding.cbIndex.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		Selects the codebook index for a PUSCH allocation. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:return: code_book_index: Range: 0 to 5"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:PRECoding:CBINdex?')
		return Conversions.str_to_float(response)
