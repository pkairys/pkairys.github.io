#!/usr/bin/env python

import os
import re
import subprocess
import shutil
import click

local_assets_path = '/home/paul/Documents/Personal/pkairys.github.io/assets/'

default_frontmatter = """ ---
layout: default
title: No Title Yet
Description: No description Yet
ispost: True
---
\n
"""

def nb_to_md(ipynb):
    
    ipynb_path = os.path.abspath(ipynb)
    ipynb_name = ipynb_path.split('/')[-1][:-6]
    post_path = ipynb_path[:ipynb_path.rfind('/')]
    post_name = post_path.split('/')[-1]
    md_path = post_path+'/index.md'
    files_path = ipynb_path[:-6]+'_files/'
    bokeh_path = post_path + '/bokeh_files/'

    asset_files_path = local_assets_path + post_name + '/' + ipynb_name+'_files/'    
    asset_post_path = local_assets_path + post_name + '/'

    execute = "jupyter nbconvert --to markdown {} --stdout".format(ipynb_path)
    get_files = "jupyter nbconvert --to markdown {}".format(ipynb_path)
    clean = "rm -rf " + ipynb_path[:-6]+'.md'
    
    md = subprocess.check_output(execute.split(' ')).decode('utf-8') 
    subprocess.run(get_files.split(' '))
    subprocess.run(clean.split(' '))


    if not os.path.exists(asset_post_path):
        os.mkdir(asset_post_path)
    if os.path.exists(asset_files_path):
        shutil.rmtree(asset_files_path)

    os.rename(files_path, asset_files_path)

    if os.path.exists(bokeh_path):
        for file in os.listdir(bokeh_path):
            os.rename(bokeh_path+file,asset_files_path+file)
    
    file_name_pattern = re.compile('(\(.*'+ipynb_name+'_files\/(.*)\))')
    
    file_names = re.findall(file_name_pattern, md)
    
    for pat, name in file_names:
        
        replacement = '{{ "/assets/'+post_name+'/'+ipynb_name+'_files/'+name+'" | absolute_url }}' 
        md = re.sub(pat, replacement, md) 
    
    with open(md_path, 'w') as f:
        md = default_frontmatter + md
        f.write(md)

if __name__ == '__main__':
    
    import sys
    nb_to_md(sys.argv[1])
