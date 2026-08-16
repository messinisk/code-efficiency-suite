# Code efficiency suite


suite_test  είναι decorator για τη μέτρηση της απόδοσης των συναρτήσεων.<br/>

user code:<br/>

@suite_test()<br/>
def fsum(n: int) -> float:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;return sum(i for i in range(n))<br/>

run :<br/>
print("fsum(100)", fsum(100))<br/>
print("fsum(1_000)", fsum(1_000))<br/>
print("fsum(10_000)", fsum(10_000))<br/>
print("fsum(100_000)", fsum(100_000))<br/>
print("fsum(1_000_000)", fsum(1_000_000))<br/>

output:

  fsum(100) {'speed': Decimal('0.00004940000053466065'), 'memory': Decimal('0.00037384033203125'), 'size': Decimal('28')}<br/>
  fsum(1_000) {'speed': Decimal('0.0006408089993783506'), 'memory': Decimal('0.00043487548828125'), 'size': Decimal('28')}<br/>
  fsum(10_000) {'speed': Decimal('0.00752489099977538'), 'memory': Decimal('0.0008249282836914062'), 'size': Decimal('28')}<br/>
  fsum(100_000) {'speed': Decimal('0.08154692100015382'), 'memory': Decimal('0.0025577545166015625'), 'size': Decimal('32')}<br/>
  fsum(1_000_000) {'speed': Decimal('0.7673067390005599'), 'memory': Decimal('0.0036478042602539062'), 'size': Decimal('32')}<br/>

