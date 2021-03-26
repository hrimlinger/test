import os, sys
import re
import json

def parse_results(file_path_results, file_path_variables):

    with open(file_path_results,"r") as json_file :
        
        data = json.load(json_file)

        variables_file = open(file_path_variables,"r") 
        variables_list = variables_file.readlines()

        print(variables_list)

        for entry in data:
            if data[entry] == "Success":
                print("Test : " +entry+" passed.")

file_path_results = '../data/results.json'
file_path_variables = '../bash_script/variables.sh'

parse_results(file_path_results,file_path_variables)