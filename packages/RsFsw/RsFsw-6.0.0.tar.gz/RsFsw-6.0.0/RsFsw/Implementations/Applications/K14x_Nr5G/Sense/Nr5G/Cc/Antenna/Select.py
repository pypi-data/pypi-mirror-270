from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SelectCls:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, antenna: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:ANTenna:SELect \n
		Snippet: driver.applications.k14Xnr5G.sense.nr5G.cc.antenna.select.set(antenna = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		Filters the constellation points by a certain antenna port.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Create the constellation diagram after MIMO decoding ([SENSe:]NR5G[:CC<cc>]:LOCation:SELect) . \n
			:param antenna: Number of the antenna port (for example 1001) .
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(antenna)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:ANTenna:SELect {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: [SENSe]:NR5G[:CC<cc>]:ANTenna:SELect \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.nr5G.cc.antenna.select.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Filters the constellation points by a certain antenna port.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Create the constellation diagram after MIMO decoding ([SENSe:]NR5G[:CC<cc>]:LOCation:SELect) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: antenna: Number of the antenna port (for example 1001) ."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:NR5G:CC{carrierComponent_cmd_val}:ANTenna:SELect?')
		return Conversions.str_to_float(response)
