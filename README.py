# Company-Class
#English : This code is for better #understanding and learning of classes in #Python, and it uses multiple inheritance #and the effect of MRO is evident in it.

class fard :
	def __init__ (self,nam,sen):
		self.name = nam 
		self.sen = sen 
		
	def moarefi(self) :
		print(f"esm man {self.name} va sen man ham {self.sen} sal ast ")
		
		
class barname_nevis(fard):
	def __init__ (self,nam,sen,zaban=None,sathe_maharat=None):
		super().__init__(nam,sen)
		self.zaban_barname_nevisi = zaban
		self.sathe_maharat_barname_nevisi = sathe_maharat 
		
	def moarefi(self):
		super().moarefi()
		print(f"zaban barname nevisi man {self.zaban_barname_nevisi} va sathe mahart man {self.sathe_maharat_barname_nevisi} ast")
		
		
class modir(fard):
		def __init__(self,nam,sen,maharat_modirity):
			super().__init__(nam,sen)
			self.sathe_maharat_modirity=maharat_modirity
		
		def moarefi(self):
			super().moarefi()
			print(f"man modir hastem va sathe maharat man {self.sathe_maharat_modirity} ast")
			
	
class modir_fanavari(modir,barname_nevis):
	def __init__(self,nam,sen,maharat_modirity,zaban,sathe_maharat):
		super().__init__(nam,sen,maharat_modirity)
	
		self.zaban_barname_nevisi = zaban
		self.sathe_maharat_barname_nevisi = sathe_maharat 
		
	def moarefi(self):
		print("man modir fanavari hastam. ")
		super().moarefi()
	
	
		
p=modir_fanavari("amir",15,"khob","python","khob")
p.moarefi()
