import os
import sys
import pandas

class SystematicsForProcess:
	def __init__(self,name,process,typ,construction,Up=None,Down=None):
		self.name=name
	 	self.process=process 
	 	self.typ=typ 
	 	self.construction=construction 
	 	self.Up=Up
	 	self.Down=Down


class Systematics:
	def __init__(self,systematicconfig):
		print "loading systematics config ..."
		self.systematics=pandas.read_csv(systematicconfig)

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
					temp=SystematicsForProcess(name,process,typ,construction,Up,Down)
					self.processes[process][name]=temp

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


	#returns all weight systematics
	def get_all_weight_systs(self):
		weightsysts=[]
		for i,systematic in self.systematics.iterrows():
			if systematic["Construction"]=="weight":
				#adds variable name to list of weightsysts
				weightsysts.append(systematic["Uncertainty"])
		return weightsysts
	#returns all variation systematics
	def get_all_variation_systs(self):
		variationsysts=[]
		for i,systematic in self.systematics.iterrows():
			if systematic["Construction"]=="variation":
				#adds variable name to list of variationsysts
				variationsysts.append(systematic["Uncertainty"])
		return variationsysts
	#returns all rate systematics
	def get_all_rate_systs(self):
		ratesysts=[]
		for i,systematic in self.systematics.iterrows():
			if systematic["Construction"]=="rate":
				#adds variable name to list of ratesysts
				ratesysts.append(systematic["Uncertainty"])
		return ratesysts


