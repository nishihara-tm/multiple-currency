from money import Money, Expression, Bank 

def test_multiplication():
  five = Money.doller(5)
  result = five.times(2, "USD")
  assert result.equals(Money.doller(10))

def test_franc_multiplication():
  five = Money.franc(5)
  result = five.times(2, "CHF")
  assert result.equals(Money.franc(10))

def test_equality():
  assert Money(5, "USD").equals(Money(5, "USD"))
  assert not Money(5, "USD").equals(Money(5, "CHF"))

def test_currency():
  assert Money.doller(5).currency == "USD"
  assert Money.franc(6).currency == "CHF"

def test_add():
  sum: Expression = Money.doller(5).plus(Money.doller(5))
  bank: Bank = Bank()
  reduced: Money = bank.reduce(sum, "USD")
  assert Money.doller(10).equals(reduced)
