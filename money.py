from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
  def test():
    pass

class Money():
  def __init__(self, amount: int, currency: str):
    self.amount = amount
    self.currency = currency

  def equals(self, another: Money) -> bool:
    return (self.amount == another.amount) and (self.currency == another.currency)

  def times(self, multiplication:int, currency: int) -> Money:
    result = self.amount * multiplication
    return Money(result, currency)

  def reduce(self, currency: str, bank: Bank):
    rate = bank.getRate(self.currency, currency)
    amount = self.amount * rate
    return Money(amount, currency)

  #def plus(self, another: Money) -> Money:
  #  result = self.amount + another.amount
  #  return Money(result, self.currency)

  def plus(self, another: Money) -> Expression:
    return Sum(self, another)

  @staticmethod
  def doller(amount) -> Money:
    return Money(amount, "USD")

  @staticmethod
  def franc(amount) -> Money:
    return Money(amount, "CHF")

class Bank:
  def __init__(self, rates=[]) -> None:
    self.rates = rates

  def addRate(self, from_currency, to_currency, rate):
    h = {"from": from_currency, "to": to_currency, "rate": rate}
    self.rates.append(h)

  def getRate(self, from_currency, to_currency) -> int:
    if(from_currency == to_currency):
      return 1

    rates = list(filter(
      lambda x: x["from"] == from_currency and x["to"] == to_currency, self.rates))
    return rates[-1]["rate"]

  def reduce(self, source: Expression, currency) -> Money:
    return source.reduce(currency, self)

class Sum(Expression):
  def __init__(self, augend: Money, addend: Money):
    self.augend = augend
    self.addend = addend

  def reduce(self, currency, bank: Bank):
    amount = self.addend.reduce(currency, bank).amount + self.augend.reduce(currency, bank).amount
    return Money(amount, currency)

class Multiple(Expression):
  def __init__(self, augend: Money, addend: Money):
    self.augend = augend
    self.addend = addend

  def reduce(self, currency, bank: Bank):
    amount = self.addend.reduce(currency, bank).amount * self.augend.reduce(currency, bank).amount
    return Money(amount, currency)
