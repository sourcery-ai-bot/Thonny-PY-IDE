from pybricks.parameters import Port


class TouchSensor:
    """
    LEGO® MINDSTORMS® NXT Touch Sensor.

    Args:
        port (Port): Port to which the sensor is connected.
    """

    def __init__(self, port: Port):
        if port in [Port.A, Port.B, Port.C, Port.D]:
            raise ValueError("Sensors must use Port S1, S2, S3, or S4.")

    def pressed(self) -> bool:
        """
        Checks if the sensor is pressed.

        Returns:
            True if the sensor is pressed, False if it is not pressed.
        """
        return False
