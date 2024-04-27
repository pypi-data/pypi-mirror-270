from datetime import datetime, timezone
import pprint
import re  # noqa: F401


from ya_payment.configuration import Configuration



class Deposit(object):
    openapi_types = {
        'id': 'str',
        'contract': 'str'
    }
    attribute_map = {
        'id': 'id',
        'contract': 'contract'
    }

    def __init__(self, id=None, contract=None, local_vars_configuration=None):
        self.local_vars_configuration = local_vars_configuration
        self._id = None
        self._contract = None

        self.id = id
        self.contract = contract

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def contract(self):
        return self._contract

    @contract.setter
    def contract(self, contract):
        self._contract = contract
