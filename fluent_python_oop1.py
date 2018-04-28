# class Gizmo:
# 	def __init__( self ):
# 		print('Gizmo id:', id(self) )
# 		#return id(self) 

# #x = Gizmo()

# #y = Gizmo() * 10
# dir(Gizmo.__dict__)

#Identity, Equality, and Aliases
charles = {
			'name' : 'Charles L. Dodgson' , 
			'born' : '1832' ,
		  }
print(charles)
lewis = charles

print(lewis is charles)
print(charles is lewis)
print("id(charles)=",id(charles))
print("id(lewis)=",id(lewis))

lewis['balance'] = 950
print(charles)

alex = {'name': 'Charles L. Dodgson', 'born': '1832', 'balance': 950}
print(alex == charles)
print(alex is not charles)

