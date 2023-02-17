import os
import json
from StaticEplusEngine import run_eplus_model, convert_json_idf

class Two_parameter_parametric:

	def __init__(self):
		self.Key_1 = None
		self.Vals_1 = None
		self.Key_2 = None
		self.Vals_2 = None
	def Key1_set(self,key_1):
		self.Key_1 = key_1
		return Key_1
	def Key2_set(self,key_2):
		self.Key_2 = key_2
		return Key_2
	def Vals1_set(self,val_1):
		self.Vals_1 = val_1
	def Vals1_set(self,val_2):
		self.Vals_2 = val_2
	def Val1_get(self):
		for parameter_val1 in self.Vals_1:
			if parameter_val1 == min(Vals_1): 
				return self.parameter_val1
			else: return None
	def Val2_get(self,key_2):
		for parameter_val2 in self.Vals_2:
			if parameter_val2 == max(Vals_2):
				return self.parameter_val1
			else: 
				return None

	def double_simulation_helper(eplus_run_path, idf_path, output_dir,
									parameter_key1, parameter_key2, 
									parameter_val1, parameter_val2):

		convert_json_idf(eplus_run_path, idf_path)
		epjson_path = idf_path.split('.idf')[0] + '.epJSON'

		with open(epjson_path) as epJSON:
			epjson_dict = json.load(epJSON)

		inner_dict = epjson_dict
		for i in range(len(parameter_key1)):
			if i < len(parameter_key1) - 1:
				inner_dict = inner_dict[parameter_key1[i]]
		inner_dict[parameter_key1[-1]] = parameter_val1
		inner_dict[parameter_key2[-1]] = parameter_val2

		with open(epjson_path, 'w') as epjson:
			json.dump(epjson_dict, epjson)

		convert_json_idf(eplus_run_path, epjson_path)

		run_eplus_model(eplus_run_path, idf_path, output_dir)
		return output_dir


	def run_two_parameter_parametric(eplus_run_path, idf_path, output_dir,
									Key_1, Vals_1, Key_2, Vals_2):
		
		output_paths=[]
		i=1
		if not os.path.isdir(output_dir):
			os.mkdir(output_dir)
		for parameter_val1 in Vals_1:
			for parameter_val2 in Vals_2:
				this_output_dir = output_dir+'/run_{}'.format(i)
				this_res_path = double_simulation_helper(eplus_run_path, idf_path,
										this_output_dir, self.Key_1, self.Key_2,
										parameter_val1, parameter_val2)
				parameter_val = parameter_val1 + parameter_val2
				output_paths.append('{}:'.format(parameter_val)+this_res_path)
				i= i+1								
		return output_paths

import numpy as np
window_u = Two_parameter_parametric()
window_u.Vals_1 = []
window_SHGC = Two_parameter_parametric()
window_SHGC.Vals_2 = []
eplus_run_path = './energyplus9.5/energyplus'
idf_path = './1ZoneUncontrolled_win_1.idf'
output_dir = 'exp'
Key_1 = Two_parameter_parametric()
Key_1.Key1_set(['WindowMaterial:SimpleGlazingSystem',
               'SimpleWindow:DOUBLE PANE WINDOW',
               'u factor'])
Key_2 = Two_parameter_parametric()
Key_2.Key2_set(['WindowMaterial:SimpleGlazingSystem',
               'SimpleWindow:DOUBLE PANE WINDOW',
               'Solar_heat_gain_coefficient'])
output_paths = Two_parameter_parametric()
output_paths = output_paths.run_two_parameter_parametric(eplus_run_path, 
													idf_path, output_dir, 
	                          				  Key_1, Vals_1, Key_2, Vals_2)
