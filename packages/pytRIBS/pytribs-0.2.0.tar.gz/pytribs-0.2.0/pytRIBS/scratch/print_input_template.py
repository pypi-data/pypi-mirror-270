import os
import sys

os.chdir('..')

from pytRIBS.tmodel import Model

m = Model()
data = m.options
m.write_input_file('scratch/template.in',detailed=True)
#time
#flow
#hydro
#spatial
#meterological
# output - options and paths
# forecast - suite
# stochastic
# restart - options
# # parallel
# tags = ['time','mesh', 'flow', 'hydro', 'spatial', 'meterological', 'output','forecast','stochastic','restart','parallel']
# headers = {'time':'Time Variables','mesh':'Mesh Options','flow':'Routing Variables','hydro':'Hydrologic Processes',
#            'spatial':'Spatial Data Inputs','meterological':'Meterological Options and Data','output':'Model Output Paths and Options',
#            'forecast':'Forecast Mode','stochastic':'Stochastic Mode', 'restart':'Restart Mode','parallel':'Parallel Mode'}
#
# path = 'scratch/template.in'
#
# meta = "This is a template input file for tRIBS 5.2.0\n" +\
# "Sections of the input file mirror documentation found at:\n" +\
# "https://tribshms.readthedocs.io/en/latest/man/Model%20Input%20File.html#input-file-options\n"+\
# "Some values are already provided in the line following the keyword, where keywords are shown in all caps.\n"+\
# "Where values are not provided are marked by the string \"Update!\". Following the value is a short description of \n"+\
# "what the keyword does, alongside available options. Note: only values required by given a option must be specified.\n\n"
#
# with open(path,'w') as file:
#
#     string = 'Input File Template for tRIBS Version 5.2'
#     underline = '=' * len(string)
#     file.write(f'{underline}\n{string}\n{underline}\n\n')
#     file.write(meta)
#
#     for tag in tags:
#         underline = '='*len(headers[tag])
#         file.write(f'{underline}\n{headers[tag].upper()}\n{underline}\n\n')
#         result = [item for item in data.values() if any(tag in _tag for _tag in item.get("tags", []))]
#
#         for dictionary in result:
#             keyword = dictionary['key_word']
#             file.write(f'{keyword}\n')
#             val = dictionary['value']
#             if val is not None:
#                 file.write(f"{dictionary['value']}\n\n")
#             else:
#                 file.write(f"Update!\n\n")
#
#             description = dictionary['describe']
#             if description is not None:
#                 file.write(f"Description:\n{description}\n")
#             else:
#                 file.write(f"None\n")
#             file.write(f" \n")
#


