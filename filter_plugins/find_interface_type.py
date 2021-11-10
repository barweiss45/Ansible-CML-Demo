#!/usr/bin/python

# The 'FilterModule' class is required for all custom filters
class FilterModule:
    # This function is needed to map the filter in the playbook to the python fuction below. This is also another required function.
    @staticmethod  #The staticmethod decorator is used because this Class is uninstantiated, and we don't need the (self).
    def filters():
        '''This maps ansible filter names to Python function names'''
        return {
            'find_interface_type': FilterModule.find_interface_type
        }
    @staticmethod
    def find_interface_type(interface):
        '''Returns the interface type of an interface.'''
        if interface.startswith("L"):
            interface_type = "loopback"
        elif interface.startswith("G"):
            interface_type = "gigabitEthernet"
        else:
            interface_type = None
        return interface_type
