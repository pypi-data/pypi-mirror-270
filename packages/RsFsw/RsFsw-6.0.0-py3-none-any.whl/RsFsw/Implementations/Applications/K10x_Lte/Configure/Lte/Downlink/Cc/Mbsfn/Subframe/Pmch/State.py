from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MBSFn:SUBFrame<sf>:PMCH:STATe \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.mbsfn.subframe.pmch.state.set(state = False, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		Turns the PMCH in an MBSFN subframe on and off. Note that you first have to turn a subframe into an MBSFN subframe with
		method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.Mbsfn.Subframe.State.set. \n
			:param state: ON | OFF | 1 | 0
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MBSFn:SUBFrame{subframe_cmd_val}:PMCH:STATe {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> bool:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MBSFn:SUBFrame<sf>:PMCH:STATe \n
		Snippet: value: bool = driver.applications.k10Xlte.configure.lte.downlink.cc.mbsfn.subframe.pmch.state.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		Turns the PMCH in an MBSFN subframe on and off. Note that you first have to turn a subframe into an MBSFN subframe with
		method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.Mbsfn.Subframe.State.set. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:return: state: ON | OFF | 1 | 0"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MBSFn:SUBFrame{subframe_cmd_val}:PMCH:STATe?')
		return Conversions.str_to_bool(response)
