from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:PASTe:ALL \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.paste.all.set(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default) \n
		Applies an existing frame configuration to all other frames.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Copy a frame configuration (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.copy) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
		"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:PASTe:ALL')

	def set_with_opc(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, opc_timeout_ms: int = -1) -> None:
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:PASTe:ALL \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.paste.all.set_with_opc(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default) \n
		Applies an existing frame configuration to all other frames.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Copy a frame configuration (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.copy) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:PASTe:ALL', opc_timeout_ms)
