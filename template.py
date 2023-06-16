# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 20:17:47 2023

@author: ACER
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from pathlib import Path #paths editor for different os or ide
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')
project_name = 'textSummarizer'
list_of_files = ['.github/workflows/.gitkeep',
                 f'src/{project_name}/__init__.py',
                 f"src/{project_name}/conponents/__init__.py",
                 f"src/{project_name}/utils/__init__.py",
                 f"src/{project_name}/conponents/common.py",
                 f"src/{project_name}/logging/__init__.py",
                 f"src/{project_name}/config/__init__.py",
                 f"src/{project_name}/config/configuration.py",
                 f"src/{project_name}/pipeline/__init__.py",
                 f"src/{project_name}/entity/__init__.py",
                 f"src/{project_name}/constants/__init__.py",
                 'config/config.yaml',
                 'params.yaml',
                 'app.py',
                 'main.py',
                 'Dockerfile',
                 'requirements.txt',
                 'setup.py',
                 'research/trials.ipynb'
                 ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) #splits directory path and filename
    
    if filedir != '': #checks if the file is not empty
        os.makedirs(filedir, exist_ok = True)
        logging.info(f'Creating directory: {filedir} for the file {filename}') #returns string with logging info
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating empty file: {filepath}')
        
    else:
        logging.info(f'{filename} already exists')