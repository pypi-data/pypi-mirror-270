from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImaginaryCls:
	"""Imaginary commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("imaginary", core, parent)

	def set(self, imaginary: float, carrierComponent=repcap.CarrierComponent.Default, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:CSWeight:ANTenna<ant>:FHFRame<fr>:IMAGinary \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.sync.csWeight.antenna.fhFrame.imaginary.set(imaginary = 1.0, carrierComponent = repcap.CarrierComponent.Default, antenna = repcap.Antenna.Default) \n
		Defines the signal weight for the imaginary part of the signal in the first half frame.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on custom sync signal weight (method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.Sync.CsWeight.State.set) . \n
			:param imaginary: Range: -1 to 1
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
		"""
		param = Conversions.decimal_value_to_str(imaginary)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:CSWeight:ANTenna{antenna_cmd_val}:FHFRame50:IMAGinary {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, antenna=repcap.Antenna.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:CSWeight:ANTenna<ant>:FHFRame<fr>:IMAGinary \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.sync.csWeight.antenna.fhFrame.imaginary.get(carrierComponent = repcap.CarrierComponent.Default, antenna = repcap.Antenna.Default) \n
		Defines the signal weight for the imaginary part of the signal in the first half frame.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on custom sync signal weight (method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.Sync.CsWeight.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: imaginary: Range: -1 to 1"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:CSWeight:ANTenna{antenna_cmd_val}:FHFRame50:IMAGinary?')
		return Conversions.str_to_float(response)
