import os
import sys
import pandas

class SystematicsForProcess:
	def __init__(self,name,process,typ,construction,expression=None):
		self.name=name
	 	self.process=process 
	 	self.typ=typ 
	 	self.construction=construction 
	 	self.expression=expression

class Systematics:
	def __init__(self,systematicconfig):
		print "loading systematics config ..."
		self.systematics=pandas.read_csv(systematicconfig,sep=";")

	def getSystematicsForProcesses(self,list_of_processes):
		self.processes={}
		for process in list_of_processes:
			self.processes[process]={}
		for i,systematic in self.systematics.iterrows():
			name=systematic["Uncertainty"]
			if name.startswith("#"):
				continue
			typ=systematic["Type"]
			construction=systematic["Construction"]
			Up=systematic["Up"]
			if Up=="-":
				Up=None
			Down=systematic["Down"]
			if Down=="-":
				Down=None
			for process in list_of_processes:
				if systematic[process] is not "-":
					if Up:
						up="_"+name+"Up"	
						self.processes[process][up]=SystematicsForProcess(up,process,typ,construction,Up)
					if Down:
						down="_"+name+"Down"
						self.processes[process][down]=SystematicsForProcess(down,process,typ,construction,Down)
					if not Up and not Down:
						self.processes[process][name]=SystematicsForProcess(name,process,typ,construction)

	#returns weight systematics for specific process
	def get_weight_systs(self,process):
		weightsysts=[]
		for systematic in self.processes[process]:
			if self.processes[process][systematic].construction=="weight":
				#adds variable name to list of weightsysts
				weightsysts.append(systematic)
		return weightsysts
	#returns variation systematics for specific process
	def get_variation_systs(self,process):
		variationsysts=[]
		for systematic in self.processes[process]:
			if self.processes[process][systematic].construction=="variation":
				#adds variable name to list of variationsysts
				variationsysts.append(systematic)
		return variationsysts
	#returns all rate systematics
	def get_rate_systs(self,process):
		ratesysts=[]
		for systematic in self.processes[process]:
			if self.processes[process][systematic].construction=="rate":
				#adds variable name to list of ratesysts
				ratesysts.append(systematic)
		return ratesysts
	#returns all shape systematics
	def get_shape_systs(self,process):
		shape_systs=self.get_weight_systs(process)+self.get_variation_systs(process)
		return shape_systs

	#returns all weight systematics
	def get_all_weight_systs(self):
		weightsysts=[]
		for i,systematic in self.systematics.iterrows():
			if systematic["Uncertainty"].startswith("#"):
				continue
			if systematic["Construction"]=="weight":
				#adds variable name to list of weightsysts
				systName=systematic["Uncertainty"]
				up="_"+systName+"Up"
				down="_"+systName+"Down"
				weightsysts.append(up)
				weightsysts.append(down)
		return weightsysts

	def get_all_weight_expressions(self):
		weightexp=[]
		weightsysts=[]
		for i,systematic in self.systematics.iterrows():
			if systematic["Uncertainty"].startswith("#"):
				continue
			if systematic["Construction"]=="weight":
				#adds variable name to list of weightsysts
				up=systematic["Up"]
				down=systematic["Down"]
				weightsysts.append(up)
				weightsysts.append(down)
		return weightsysts
	#returns all variation systematics
	def get_all_variation_systs(self):
		variationsysts=[]
		for i,systematic in self.systematics.iterrows():
			if systematic["Uncertainty"].startswith("#"):
				continue
			if systematic["Construction"]=="variation":
				#adds variable name to list of variationsysts
				systName=systematic["Uncertainty"]
				up="_"+systName+"Up"
				down="_"+systName+"Down"
				variationsysts.append(up)
				variationsysts.append(down)
		return variationsysts
	#returns all rate systematics
	def get_all_rate_systs(self):
		ratesysts=[]
		for i,systematic in self.systematics.iterrows():
			if systematic["Uncertainty"].startswith("#"):
				continue
			if systematic["Construction"]=="rate":
				#adds variable name to list of ratesysts
				ratesysts.append(systematic["Uncertainty"])
		return ratesysts

	def makeCSV(self,list_of_processes,outputpath):
		header=["Uncertainty","Type"]
		header+=list_of_processes
		#only get information for processes that are included
		newCSV=self.systematics[header]
		#delete all uncertainties that start with "#"
		newCSV=newCSV[~newCSV["Uncertainty"].astype(str).str.startswith("#")]
		newCSV.to_csv(outputpath, index=False)

	def plot_shapes(self):
		plotShapes=[]
		# add nominal
		plotShapes.append("")
		for i,systematic in self.systematics.iterrows():
			if systematic["Uncertainty"].startswith("#"):
				continue
			if str(systematic["Plot"])=="1":
				systName=systematic["Uncertainty"]
				up="_"+systName+"Up"
				down="_"+systName+"Down"
				plotShapes.append(up)
				plotShapes.append(down)
		return plotShapes





