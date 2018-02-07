#!/usr/bin/env python

import os
import re
import subprocess
import shutil
import click

local_assets_path = '/home/paul/Documents/Personal/pkairys.github.io/assets/'

@click.command()
@click.argument('ipynb', type=click.Path(exists=True))
def nb_to_md(ipynb):
    
    ipynb_path = os.path.abspath(ipynb)
    md_path = ipynb_path[:ipynb_path.rfind('/')]+'/index.md'
    ipynb_name = ipynb_path.split('/')[-1][:-6]
    post_name = ipynb_path.split('/')[-2]
    files_path = ipynb_path[:-6]+'_files/'
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

    file_name_pattern = re.compile('(\(.*'+ipynb_name+'_files\/(.*)\))')
    
    file_names = re.findall(file_name_pattern, md)
    
    for pat, name in file_names:
        
        replacement = '{{ "/assets/'+post_name+'/'+ipynb_name+'_files/'+name+'" | absolute_url }}' 
        md = re.sub(pat, replacement, md) 
    
    with open(md_path, 'w') as f:
        f.write(md)

