class Students:

   def __init__(self, first, last, expedient, mail):
       self.first = first
       self.last = last
       self.expedient = expedient
       self.mail = mail

   @property
   def fullname(self):
       return '{} {}'.format(self.first, self.last)
