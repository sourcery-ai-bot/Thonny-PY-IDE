from pybricks.parameters import Port


class TemperatureSensor:
    """
    LEGO® MINDSTORMS® NXT Temperature Sensor.

    Args:
        port (Port): Port to which the sensor is connected.
    """

    def __init__(self, port: Port):
        if port in [Port.A, Port.B, Port.C, Port.D]:
            raise ValueError("Sensors must use Port S1, S2, S3, or S4.")

    def temperature(self) -> float:
        """
        Measures the temperature.

        Returns:
            Measured temperature in degrees Celsius.
        """
        return 0.0
