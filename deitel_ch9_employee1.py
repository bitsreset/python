class Employee:
	"""Class to represent an employee """

	def __init__( self , first , last ):
		"""Employee Constructor takes first and last name """
		self.firstName = first
		self.lastName =  last 

	def __str__( self ):
		return "{} {}".format( self.firstName , self.lastName )

class HourlyWorker( Employee ):
	""" Constructor for  HourlyWorker , takes first and last name , inital number
	 of hours and inital wage"""
	def __init__( self , first , last , initHrs , initWg ):
	 	super().__init__( first , last )
	 	self.hours = float( initHrs ) 
	 	self.wage =  float( initWg )

	def getPay( self ):
	 	return self.hours * self.wage 

	def __str__( self ):
	 	"""String representation of HourlyWorker """
	 	print("HourlyWorker.__str__ is executing")
	 	return "{} is an hourly worker with pay of {}".format( super().__str__() , self.getPay() )

#main Program
hourly = HourlyWorker( "Bob" , "Smith" , 40.0 , 10.00 ) 

# invoke __str__ method several ways
print("Calling __str__ several ways...")
print(hourly)
print(hourly.__str__())
print(HourlyWorker.__str__( hourly ))

