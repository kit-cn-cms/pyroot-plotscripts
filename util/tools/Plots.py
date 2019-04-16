import ROOT

class Plot:
	def __init__(self, histo, variable, label = '', color= '', typ=''):
		self.histo=histo
		self.variable=variable
		self.label=label
		self.color=color
		self.typ=typ
