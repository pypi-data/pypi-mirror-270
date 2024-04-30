"""
Parity Quantum Computing GmbH
Rennweg 1 Top 314
6020 Innsbruck, Austria

Copyright (c) 2020-2024.
All rights reserved.

Tools to export ParityOS circuits to Qiskit.
"""
from collections.abc import Iterable, Mapping

from parityos.base.circuit import CircuitElement
from parityos.base.gates import (
    CCNOT,
    CNOT,
    CRx,
    CRy,
    CRz,
    CY,
    CZ,
    Gate,
    H,
    ISwap,
    MultiControlMixin,
    MultiControlledH,
    MultiControlledRx,
    MultiControlledRy,
    MultiControlledRz,
    Qubit,
    RMixin,
    Rx,
    Rxx,
    Ry,
    Ryy,
    Rz,
    Rzz,
    Swap,
    X,
    Y,
    Z,
)
from parityos.base.exceptions import ParityOSImportError

try:
    import qiskit
    import qiskit.circuit.library as qiskit_library
except ImportError:
    raise ParityOSImportError("The Qiskit exporter requires the installation of Qiskit")

GATE_MAP: dict[type[Gate], type[qiskit.circuit.gate.Gate]] = {
    CCNOT: qiskit_library.CCXGate,
    CNOT: qiskit_library.CXGate,
    CRx: qiskit_library.CRXGate,
    CRy: qiskit_library.CRYGate,
    CRz: qiskit_library.CRZGate,
    CY: qiskit_library.CYGate,
    CZ: qiskit_library.CZGate,
    H: qiskit_library.HGate,
    ISwap: qiskit_library.iSwapGate,
    MultiControlledH: qiskit_library.HGate,  # Will be remapped by qiskit_library.MCMT.
    MultiControlledRx: qiskit_library.RXGate,  # Will be remapped by qiskit_library.MCMT.
    MultiControlledRy: qiskit_library.RYGate,  # Will be remapped by qiskit_library.MCMT.
    MultiControlledRz: qiskit_library.RZGate,  # Will be remapped by qiskit_library.MCMT.
    Rx: qiskit_library.RXGate,
    Rxx: qiskit_library.RXXGate,
    Ry: qiskit_library.RYGate,
    Ryy: qiskit_library.RYYGate,
    Rz: qiskit_library.RZGate,
    Rzz: qiskit_library.RZZGate,
    Swap: qiskit_library.SwapGate,
    X: qiskit_library.XGate,
    Y: qiskit_library.YGate,
    Z: qiskit_library.ZGate,
}


class QiskitExporter:
    """
    Tool to convert ParityOS circuits to Qiskit quantum circuits.

    Instantiate the QiskitExporter with a qubit map and a parameter map.
    Then use the `to_qiskit` method to convert a ParityOS circuit to Qiskit quantum circuit.

    EXAMPLE:
        from qiskit.circuit import Parameter
        parameter_map = {'theta': Parameter('$\\theta$'), 'gamma': Parameter('$\\gamma$')}
        qiskit_exporter = QiskitExporter(parameter_map)
        qiskit_circuit = qiskit_exporter.to_qiskit(parityos_circuit)
    """

    def __init__(
        self,
        parameter_map: Mapping[str, object] = None,
        qubit_map: Mapping[Qubit, int] = None,
        qubits: Iterable[Qubit] = None,
    ):
        """
        Converts the circuit to a Qiskit circuit.

        :param parameter_map: a mapping of the form {parameter_name: parameter_value}, where the
            parameter_name is a string that is used as a parameter_name in the ParityOS circuit,
            and parameter_value is a number like object (int, float, numpy float or a Qiskit
            Parameter object are all valid). Optional. If not given, then an empty dictionary is
            used instead.
        :param qubit_map: a mapping of the form {ParityOS_qubit: qubit_index}, where qubit_index is
            the integer index of the qubit in the Qiskit qubit register. Optional.
        :param qubits: an iterable of ParityOS qubits. This is used to generate a qubit_map where
            each qubit is mapped onto its index in the sequence. Optional.
            Either a `qubit_map` or a `qubits` iterable must be given.

        """
        self.parameter_map = {} if parameter_map is None else parameter_map
        if qubit_map:
            self.qubit_map = qubit_map
        elif qubits:
            self.qubit_map = {qubit: i for i, qubit in enumerate(qubits)}
        else:
            raise TypeError("QiskitExporter requires either a qubit_map or qubits argument")

    def to_qiskit(self, circuit: CircuitElement) -> qiskit.QuantumCircuit:
        """
        Converts the circuit to a Qiskit quantum circuit.

        :param circuit: a ParityOS circuit of quantum gates.
        :return: a Qiskit QuantumCircuit object.
        """
        qiskit_circuit = qiskit.QuantumCircuit(len(self.qubit_map))

        def _qiskit_circuit_append(element: CircuitElement):
            """Recursive helper method for the to_qiskit method."""
            if isinstance(element, Gate):
                self.append_qiskit_gate(qiskit_circuit, element)
            else:
                for item in element:
                    _qiskit_circuit_append(item)

        _qiskit_circuit_append(circuit)
        return qiskit_circuit

    def append_qiskit_gate(self, qiskit_circuit: qiskit.circuit, gate: Gate):
        """
        Creates a qiskit gate corresponding to the ParityOS Gate instance and appends it to the
        qiskit circuit.
        :param qiskit_circuit: the qiskit circuit to which we want to append the gate
        :param gate: the ParityOS Gate that is appended to the circuit
        """
        qiskit_class = GATE_MAP[type(gate)]
        qubits = [qiskit_circuit.qubits[self.qubit_map[qubit]] for qubit in gate.qubit_list]

        if isinstance(gate, MultiControlMixin):
            qiskit_gate = self._get_qiskit_instruction(gate, qiskit_class)
            qiskit_instruction = qiskit_library.MCMT(
                gate=qiskit_gate,
                num_ctrl_qubits=len(gate.control_qubits),
                num_target_qubits=len(gate.target_qubits),
            )
        else:
            qiskit_instruction = self._get_qiskit_instruction(gate, qiskit_class)

        qiskit_circuit.append(qiskit_instruction, qargs=qubits)

    def _get_qiskit_instruction(self, gate: Gate, qiskit_class: type) -> qiskit.circuit.gate.Gate:
        """
        Instantiates the qiskit instruction for a gate using the associated qiskit class.

        :param gate: A ParityOS gate instance
        :param qiskit_class: The qiskit gate class corresponding to the gate
        :return: A qiskit gate instance
        """
        if isinstance(gate, RMixin):
            angle = (
                gate.angle
                if gate.parameter_name is None
                else gate.angle * self.parameter_map[gate.parameter_name]
            )
            qiskit_instruction = qiskit_class(angle)
        else:
            qiskit_instruction = qiskit_class()

        return qiskit_instruction
