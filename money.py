from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
  def plus():
    return "test"

class Money(Expression):
  def __init__(self, amount: int, currency: str):
    self.amount = amount
    self.currency = currency

  def equals(self, another: Money) -> bool:
    return (self.amount == another.amount) and (self.currency == another.currency)

  def times(self, multiplication:int, currency: int) -> Money:
    result = self.amount * multiplication
    return Money(result, currency)

  def plus(self, another: Money) -> Money:
    result = self.amount + another.amount
    return Money(result, self.currency)

  @staticmethod
  def doller(amount) -> Money:
    return Money(amount, "USD")

  @staticmethod
  def franc(amount) -> Money:
    return Money(amount, "CHF")

class Bank:
  def reduce():
    return "test"