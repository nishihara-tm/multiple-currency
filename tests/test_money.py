from money import Money, Expression, Bank, Multiple, Sum 

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
  sum: Sum = Sum(Money.doller(4), Money.doller(3))
  bank: Bank = Bank()
  result = bank.reduce(sum, "USD")
  assert result.equals(Money.doller(7))

def test_expression_money():
  money = Money.doller(5)
  bank: Bank = Bank()
  result = bank.reduce(money, "USD")
  assert result.equals(Money.doller(5))

def testBankRate():
  bank: Bank = Bank()
  bank.addRate("CHF", "USD", 2)
  rate = bank.getRate("CHF", "USD")
  assert rate == 2

def testAddDifferentCurrency():
  bank: Bank = Bank()
  bank.addRate("CHF", "USD", 2)
  result: Money = bank.reduce(Money.franc(2), "USD")
  assert result.equals(Money.doller(4))
  
  sum = Sum(Money.doller(5), Money.franc(5))
  result = bank.reduce(sum, "USD")
  assert result.equals(Money.doller(15))

def testMultipleDifferentCurrency():
  bank = Bank()
  bank.addRate("CHF", "USD", 2)
  times = Multiple(Money.doller(5), Money.franc(10))
  result = bank.reduce(times, "USD")
  assert result.equals(Money.doller(100))