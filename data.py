class data:
	def __init__(self, theat = None, infile='', outfile=''):
		self.set_theat(theat)
		self.set_infile(infile)
		self.set_outfile(outfile)

	def set_theat(self, theat):
		self.__theat = theat
	def set_infile(self, infile):
		self.__infile = infile
	def set_outfile(self, outfile):
		self.__outfile = outfile

	def get_theat(self):
		return self.__theat
	def get_infile(self):
		return self.__infile
	def get_outfile(self):
		return self.__outfile
