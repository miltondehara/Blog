class A(object):

	def saludo(self,x):
		print "hola A"
		return x*x

class B(A):

	def saludo2(self,x):
		super(B,self).saludo(x)
		print "hola B"
		return x*x*x


a = A()
b = B()
x = a.saludo(2)
print x 

y = b.saludo2(2)
print y
