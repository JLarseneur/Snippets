def decorator(cls):
    class NewClass(cls):
        attr = 100
    return NewClass

@decorator
class X:
    pass
  
a = X()
a.attr
