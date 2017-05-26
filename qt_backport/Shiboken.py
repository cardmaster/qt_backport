'''
Back ports for shiboken functions with PyQt sip module functions
'''
import sip


class ShibokenPortWithSip:
    def __init__(self):
        self.isValid = sip.isdeleted
        self.ownedByPython = lambda x: sip.ispyowned(x)
        self.createdByPython = sip.ispycreated
        self.getCppPointer = sip.unwrapinstance
        self.dump = sip.dump


shiboken = ShibokenPortWithSip()