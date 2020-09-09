from abc import ABC, abstractmethod
class tv(ABC):
    def paySlip(self, amount):
        print('Your purchase amount: ', amount)
#this function is telling us to pass in an argument, but we won't tell you how or what kind of data it will be
    @abstractmethod
    def debit(self,amount):
        pass
    def gift(self,amount):
        pass

class DebitCardPayment(tv):
#Here we've defined how to implement the payment function from its parent paySlip class
    def debit(self,amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))
    def gift(self,amount):
        print('Your gift card of {} was enough to cover your purchase.'.format(amount))

obj = DebitCardPayment()
obj.paySlip('$850')
obj.debit('$850')
obj.gift('$1000')
