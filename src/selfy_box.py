from .config.selfy_config import SelfyConfig
from .handlers.camera import Camera
from .handlers.screen import Screen
from .handlers.event import Event


class SelfyBox:
    """
    Entry method for managing the SelfyBox
    """
    @classmethod
    def start_box(cls):
        """Launch the box"""
        SelfyConfig.set_up(with_gpio=True, with_pygame=True)
        Screen.display_image(file=SelfyConfig.EVENT_IMAGE)
        while True:
            Event.wait_for_event()
            Camera.take_picture()
