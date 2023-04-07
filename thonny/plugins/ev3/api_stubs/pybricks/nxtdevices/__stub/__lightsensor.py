from pybricks.parameters import Port


class LightSensor:
    """
    LEGO® MINDSTORMS® NXT Color Sensor.

    Args:
        port (Port): Port to which the sensor is connected.
    """

    def __init__(self, port: Port):
        if port in [Port.A, Port.B, Port.C, Port.D]:
            raise ValueError("Sensors must use Port S1, S2, S3, or S4.")

    def ambient(self) -> int:
        """
        Measures the ambient light intensity.

        Returns:
            Ambient light intensity, ranging from 0 (dark) to 100 (bright).
        """
        return 0

    def reflection(self) -> int:
        """
        Measures the reflection of a surface using a red light.

        Returns:
            Reflection, ranging from 0 (no reflection) to 100 (high reflection).
        """
        return 0
