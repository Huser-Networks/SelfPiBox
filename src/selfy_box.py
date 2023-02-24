import threading

from .config.selfy_config import SelfyConfig
from .handlers.camera import Camera
from .handlers.event import Event
from .handlers.screen import Screen
from .handlers.wlan import Wlan


class SelfyBox:
    """
    Entry method for managing the SelfyBox
    """
    @classmethod
    def run_program(cls):
        """
        Run a thread that wait for the user input
        """
        try:
            SelfyConfig.set_up(with_gpio=True, with_pygame=True)
            Screen.display_image(file=SelfyConfig.EVENT_IMAGE)
            while True:
                Event.wait_for_event()
                Camera.take_picture()
        except KeyboardInterrupt:
            Event.shutdown()

    @classmethod
    def start_box(cls):
        # configure the WLAN by setting up an AP if no WLAN connection exists
        Wlan.configure_wlan()

        # creating threads
        selfy_box_thread = threading.Thread(target=cls.run_program, name='selfy_box_thread')

        # starting threads
        selfy_box_thread.start()

        # if the thread finish or is exited, we launch a smooth shutdown
        selfy_box_thread.join()
        Event.shutdown()
