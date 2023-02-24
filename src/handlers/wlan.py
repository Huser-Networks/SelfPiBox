import logging

import psutil
from PyAccessPoint import pyaccesspoint

from ..config.wlan_config import WlanConfig


class Wlan:
    """
    Class containing all the function related to the SelfyBox Wlan
    """
    @classmethod
    def configure_wlan(cls):
        """
        This method check if the pi is connected to a wlan interface and if no it will set up an Access Point (AP)
        """
        cls.is_eth_up()
        if cls.is_wlan_up():
            cls.create_access_point()

    @classmethod
    def is_eth_up(cls):
        """
        Check if the ethernet interface is up and running
        :return boolean: if the ethernet interface is up and running
        """
        addrs = psutil.net_if_stats()
        is_eth_up = addrs['eth0'].isup
        if is_eth_up:
            logging.info("You are connected to Ethernet")
            return True
        logging.info("You are not connected to Ethernet")
        return False

    @classmethod
    def is_wlan_up(cls):
        """
        Check if the wireless interface is up and running
        :return boolean: if the ethernet interface is up and running
        """
        addrs = psutil.net_if_stats()
        is_wlan_up = addrs['wlan0'].isup
        if is_wlan_up:
            logging.info("You are connected to WLan")
            return True
        logging.info("You are not connected to WLan, we will set up an access point")
        return False

    @classmethod
    def create_access_point(cls):
        """
        Create an Access Point (AP) for the raspberry PI
        """
        # TODO: library seems not to work
        access_point = pyaccesspoint.AccessPoint(
            wlan=WlanConfig.NETWORK_INTERFACE,
            inet=WlanConfig.INET,
            ssid=WlanConfig.SSID,
            password=WlanConfig.PASSWORD)
        logging.info("Access Point configured")
        if access_point.is_running():
            logging.info("Access Point up")
        else:
            logging.info("Access Point down")
        access_point.start()
        logging.info("Access Point started")
        if access_point.is_running():
            logging.info("Access Point up")
        else:
            logging.info("Access Point down")
        access_point.stop()
        logging.info("Access Point stopped")
        if access_point.is_running():
            logging.info("Access Point up")
        else:
            logging.info("Access Point down")
