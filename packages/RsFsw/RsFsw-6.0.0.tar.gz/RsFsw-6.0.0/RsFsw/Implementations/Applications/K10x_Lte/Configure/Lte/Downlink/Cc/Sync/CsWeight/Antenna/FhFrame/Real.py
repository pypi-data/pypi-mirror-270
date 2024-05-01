from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RealCls:
	"""Real commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("real", core, parent)

	def set(self, real: float, carrierComponent=repcap.CarrierComponent.Default, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:CSWeight:ANTenna<ant>:FHFRame<fr>:REAL \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.sync.csWeight.antenna.fhFrame.real.set(real = 1.0, carrierComponent = repcap.CarrierComponent.Default, antenna = repcap.Antenna.Default) \n
		Defines the signal weight for the real part of the signal in the first half frame.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on custom sync signal weight (method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.Sync.CsWeight.State.set) . \n
			:param real: Range: -1 to 1
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
		"""
		param = Conversions.decimal_value_to_str(real)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:CSWeight:ANTenna{antenna_cmd_val}:FHFRame50:REAL {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:CSWeight:ANTenna<ant>:FHFRame<fr>:REAL \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.sync.csWeight.antenna.fhFrame.real.get(carrierComponent = repcap.CarrierComponent.Default, antenna = repcap.Antenna.Default) \n
		Defines the signal weight for the real part of the signal in the first half frame.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on custom sync signal weight (method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.Sync.CsWeight.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: real: Range: -1 to 1"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:CSWeight:ANTenna{antenna_cmd_val}:FHFRame50:REAL?')
		return Conversions.str_to_float(response)
