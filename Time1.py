class Time:
	""" Time ADT"""

	def __init__( self ):
		""" Initialize hour min and sec to zero"""
		self.hour = 0
		self.min =  0
		self.sec =  0 

	def printMilitary( self ):
		"""Print object of class Time in military format """
		print(" %2d:%2d:%2d" % ( self.hour , self.min ,self.sec ))

	def printStandard( self ):
		"""Print Object of class Time in standard format """

		standarTime = ""

		if self.hour == 0 or self.hour == 12:
			standarTime += '12:'
		else:
			standarTime += "%d:" % ( self.hour % 12 )

		standarTime += "%.2d:%.2d" % ( self.minute , self.second )

		if self.hour < 12 :
			standarTime += " AM"
		else :
			standarTime += " PM" 

		print(standarTime,)

print(Time.printStandard.__doc__)