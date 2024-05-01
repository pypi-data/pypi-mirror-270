from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: TRACe:IQ[:STATe] \n
		Snippet: driver.applications.iqAnalyzer.trace.iq.state.set(state = False) \n
		Activates the simple I/Q data acquisition mode (see 'Different remote modes available') . Executing this command also has
		the following effects:
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- The sweep, amplitude, input and trigger settings from the measurement are retained.
			- All measurements are turned off.
			- All traces are set to 'Blank' mode.
			- The I/Q data analysis mode is turned off (TRAC:IQ:EVAL OFF) .
		Note: To turn trace display back on or to enable the evaluation functions of the I/Q Analyzer, execute the TRAC:IQ:EVAL
		ON command (see method RsFsw.Trace.Iq.Eval.set) . \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TRACe:IQ:STATe {param}')

	def get(self) -> bool:
		"""SCPI: TRACe:IQ[:STATe] \n
		Snippet: value: bool = driver.applications.iqAnalyzer.trace.iq.state.get() \n
		Activates the simple I/Q data acquisition mode (see 'Different remote modes available') . Executing this command also has
		the following effects:
			INTRO_CMD_HELP: For triggered gated measurements,only the following gate trigger sources are supported: \n
			- The sweep, amplitude, input and trigger settings from the measurement are retained.
			- All measurements are turned off.
			- All traces are set to 'Blank' mode.
			- The I/Q data analysis mode is turned off (TRAC:IQ:EVAL OFF) .
		Note: To turn trace display back on or to enable the evaluation functions of the I/Q Analyzer, execute the TRAC:IQ:EVAL
		ON command (see method RsFsw.Trace.Iq.Eval.set) . \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'TRACe:IQ:STATe?')
		return Conversions.str_to_bool(response)
