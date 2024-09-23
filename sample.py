#!/usr/bin/env python3
'''Sample Python script for OPS435 Lab 1.
   Author: Raymond Chan
   Program name: sample.py
   Date Created: May 2020

   Usage: sample.py [base_name]

   A list of subdictories will be created under $HOME/[base_name]/dir_list
   '''

import sys
import os

def summary(s,k,e):
    '''Format and return summary information
       function parameters:
       s - success
       k - skipped
       e - error 
       function return a formatted string '''
    hc = '|'
    vc = '|'
    headers = {'Success':str(s),'Skipped':str(k),'Error':str(e)}
    for header in headers.keys():
        hc = hc + header.center(len(header)+4,'-') + '|'
        vc = vc + headers[header].center(len(header)+4,' ') + '|'
    return hc + '\n' + vc

if __name__ == '__main__':
    # check command line arguments
    if len(sys.argv) == 1:
        base_dir = os.getenv('HOME')
    else:
        base_dir = os.getenv('HOME')+'/'+sys.argv[1]

    print('Base Directory:',base_dir)

    dir_list = [ 'lab1',
                 'lab2',
                 'lab3',
                 'lab4',
                 'lab5',
                 'lab6',
                 'lab7',
                 'lab8',
                 'a1',
                 'a2' ]

    success_count = 0
    fail_count = 0
    error_count = 0

    for sub_dir in dir_list:
        sub_dir_path = base_dir + '/ops445/' + sub_dir
        if os.path.isdir(sub_dir_path) == True:
            print('Subdirectory',sub_dir_path,'already exist, skipped.',file=sys.stderr)
            fail_count += 1
        else:
            try:
                os.mkdir(sub_dir_path,mode=0o755)
                print('Subdirectory',sub_dir_path,'created.')
                success_count += 1
            except:
                print('Trouble creating',sub_dir_path,'- directory not created.',file=sys.stderr)
                error_count += 1
    
    print('Script execution summary:')
    print(summary(success_count,fail_count,error_count))
