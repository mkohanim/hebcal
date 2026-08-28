import udi_interface, os, sys, json, time
LOGGER = udi_interface.LOGGER
Custom = udi_interface.Custom
class HebcalNode(udi_interface.Node):
    id = 'hebcal'
    """This is a list of properties that were defined in the nodedef"""
    drivers = [{'driver': 'ST', 'value': 0, 'uom': 145, 'name': 'Current Date'}
        ]

    def __init__(self, polyglot, plugin, controller='hebcalcontroll',
        address='hebcal', name='Hebcal'):
        super().__init__(polyglot, controller, address, name)
        self.plugin = plugin

    def getUOM(self, driver: str):
        try:
            for driver_def in self.drivers:
                if driver_def['driver'] == driver:
                    return driver_def['uom']
            return None
        except Exception as ex:
            return None

    def updateCurrentDate(self, value, force: bool=None, text: str=None):
        return self.setDriver("ST", value, 145, force, text)

    def getCurrentDate(self):
        return self.getDriver("ST")
    """This is a list of commands that were defined in the nodedef"""
    commands = {}
    """    """

    def queryAll(self):
        self.queryCurrentDate()

    """########WARNING: DO NOT MODIFY THIS LINE!!! NOTHING BELOW IS REGENERATED!#########"""

    def queryCurrentDate(self):
        try:
            return True
        except:
            return False