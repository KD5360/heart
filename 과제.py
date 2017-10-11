Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle as t
>>> t.shape("turtle")
>>> t.color("pink")
>>> t.begin
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.begin
AttributeError: module 'turtle' has no attribute 'begin'
>>> t.begin_fill()
>>> n=100
>>> for x in range(n):
	t.right(90)
	t.fd(n)
	t.circle(n/2,180)
	t.right(90)
	t.circle(n/2,180)
	t.fd(n)

	
>>> for x in range(n):
	t.right(90)
	t.fd(n)
	t.circle(n/2,180)
	t.right(90)
	t.circle(n/2,180)
	t.fd(n)
	t.right(5)

	
