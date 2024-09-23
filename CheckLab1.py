#!/usr/bin/env python3

"""
Name: CheckLab1.py
Author: Andrew Oatley-Willis
Date: November 2, 2016
Updated by: Raymond Chan
Date: September 5, 2019

Updated: Septemeber 25, 2019 by Raymond Chan
Reason: (1) package name changes: python36 --> python3
                                  python36-pip --> python3-pip
            for centos 7.7.1908 
        (2) add report header with user and system information

Updated: May 7, 2020 by Raymond Chan
Reason: (0) merging lab0 and lab1 into lab 1 for online delivery
        (1) check lab task done on matrix.senecacollege.ca 
        (2) check directory structure for labs and assignments
        (3) lab0a - check git hub repository
        (4) lab0b - check gitlog.txt and repo_tree.txt
        (5) lab0c - check directory structure for labs and assgs
        (6) lab1a - check lab1a.py script
        (7) lab1b - check lab1b.py script
        (8) lab1c - check lab1c.py script
        (9) lab1d - check lab1d.py script

Usage:
Check all sections for the labs
./CheckLab1-1 -f -v 
Check a specific lab section
./CheckLab1-1 -f -v lab1x 

Description:
This script is used to give students feedback, progress, and
assistance while working on labs. Labs and this script should be 
in the same directory. Labs must use the correct naming scheme for
each file(eg. lab1a.py, lab1b.py, ...).


"""
from __future__ import absolute_import, division, print_function, unicode_literals
import subprocess
import unittest
import sys
import os
import hashlib
import urllib.request
import socket
import time 



class lab1a(unittest.TestCase):
    """All test cases for lab1a - printing"""
    
    def test_0(self):
        """[Lab 1] - [Investigation 3] - [Part 2] - printing - Test for file creation: ./lab1a.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue(os.path.exists('./lab1a.py'), msg=error_output)
        

    def test_a(self):
        """[Lab 1] - [Investigation 3] - [Part 2] - printing - Test for errors running: ./lab1a.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see/read the error)'
        self.assertEqual(return_code, 0, msg=error_output)

    def test_a1(self):
        """[Lab 1] - [Investigation 3] - [Part 2] - printing - Test for correct shebang line: ./lab1a.py"""
        lab_file = open('./lab1a.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line, '#!/usr/bin/env python3\n', msg=error_output)


    def test_b(self):
        """[Lab 1] - [Investigation 3] - [Part 2] - printing - Test output for correct output "Hello world": ./lab1a.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1a.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Hello world\n'
        error_output = 'output is not correct(HINT: pay attention to uppercase letters, spaces, and symbols)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
class lab1b(unittest.TestCase):
    """All test cases for lab1b - string objects & printing"""
   
    def test_0(self):
        """[Lab 1] - [Investigation 4] - string objects & printing - Test for file creation: ./lab1b.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue( os.path.exists('./lab1b.py'), msg=error_output)

    def test_a(self):
        """[Lab 1] - [Investigation 4] - string objects & printing - Test for errors running: ./lab1b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 1] - [Investigation 4] - string objects & printing - Test for correct shebang line: ./lab1b.py"""
        lab_file = open('./lab1b.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line, '#!/usr/bin/env python3\n', msg=error_output)

    def test_b(self):
        """[Lab 1] - [Investigation 4] - string objects & printing - Test for correct output "How old are you Isaac?": ./lab1b.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1b.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'How old are you Isaac?\n'
        error_output = 'output is not correct(HINT: pay attention to uppercase letters, spaces, and punctuation)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    

class lab1c(unittest.TestCase):
    """All test cases for lab1c - integer objects & printing"""
    
    def test_0(self):
        """[Lab 1] - [Investigation 4] - integer objects & printing - Test for file creation: ./lab1c.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue( os.path.exists('./lab1c.py'), msg=error_output)

    def test_a(self):
        """[Lab 1] - [Investigation 4] - integer objects & printing - Test for errors running: ./lab1c.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1c.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 1] - [Investigation 4] - integer objects & printing - Test for correct shebang line: ./lab1c.py"""
        lab_file = open('./lab1c.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line, '#!/usr/bin/env python3\n', msg=error_output)

    def test_b(self):
        """[Lab 1] - [Investigation 4] - integer objects & printing - Test output for correct output "Isaac is 72 years old!": ./lab1c.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1c.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'Isaac is 72 years old!\n'
        error_output = 'output is not correct(HINT: pay attention to uppercase letters, spaces, and punctuation)'
        self.assertEqual(stdout, expected_output, msg=error_output)

class lab1d(unittest.TestCase):
    """All test cases for lab1d - Math Operators"""
    
    def test_0(self):
        """[Lab 1] - [Investigation 5] - math operators - Test for file creation: ./lab1d.py"""
        error_output = 'your file cannot be found(HINT: make sure you AND your file are in the correct directory)'
        self.assertTrue( os.path.exists('./lab1d.py'), msg=error_output)

    def test_a(self):
        """[Lab 1] - [Investigation 5] - math operators - Test for errors running: ./lab1d.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1d.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, err = p.communicate()
        # Fail test if process returns a no zero exit status
        return_code = p.wait()
        error_output = 'your program exited with a error(HINT: try running your program to see the error)'
        self.assertEqual(return_code, 0, msg=error_output)
    
    def test_a1(self):
        """[Lab 1] - [Investigation 5] - math operators - Test for correct shebang line: ./lab1d.py"""
        lab_file = open('./lab1d.py')
        first_line = lab_file.readline()
        lab_file.close()
        error_output = 'your program does not have a shebang line(HINT: what should the first line contain)'
        self.assertEqual(first_line, '#!/usr/bin/env python3\n', msg=error_output)

    def test_b(self):
        """[Lab 1] - [Investigation 5] - math operators - Test output for correct output "10 + 2 * 5 = 20": ./lab1d.py"""
        # Run students program
        p = subprocess.Popen(['/usr/bin/python3', './lab1d.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, _ = p.communicate()
        # Fail test if output is different from expected_output
        expected_output = b'10 + 2 * 5 = 20\n'
        error_output = 'output is not correct(HINT: the program must have the exact output, this includes every space and symbol)'
        self.assertEqual(stdout, expected_output, msg=error_output)
    
   
def ChecksumLatest(url=None):
    dat = ''
    with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            dat = dat + line
    checksum = hashlib.sha256(dat.encode('utf-8')).digest()
    #print("internet", checksum)
    return checksum

def ChecksumLocal(filename=None):
    fil = open(filename, 'r', encoding='utf-8')
    dat = fil.readlines()
    textdata = ''
    for line in dat:
        textdata = textdata + line
    checksum = hashlib.sha256(textdata.encode('utf-8')).digest()
    #print("local", checksum)
    return checksum

def CheckForUpdates():
    try:
        lab_name = 'CheckLab1.py'
        lab_num = 'lab1'
        print('Checking for updates...')
        if ChecksumLatest(url='https://ict.senecacollege.ca/~eric.brauer/ops445/labs/LabCheckScripts/' + lab_name) != ChecksumLocal(filename='./' + lab_name):
            print()
            print(' There is a update available for this' + lab_name + ' please consider updating:')
            print(' cd ~/ops445/' + lab_num + '/')
            print(' pwd  #   <-- i.e. confirm that you are in the correct directory')
            print(' rm ' + lab_name)
            print(' ls ' + lab_name + ' || wget https://ict.senecacollege.ca/~eric.brauer/ops445/labs/LabCheckScripts/' + lab_name)
            print()
            return
        print('Running latest version...')
        return
    except:
        # Cleanly skip updating if any errors occur for offline or matrix issues
        print('No connection made...')
        print('Skipping updates...')
        return

def github_email():
    cmd = 'git config --get user.email'
    try:
        out = os.popen(cmd).read().strip()
    except:
        out = 'none found'
    return out

def displayReportHeader():
    report_heading = 'OPS445 Lab Report - System Information for running '+sys.argv[0]
    print(report_heading)
    print(len(report_heading) * '=')
    import getpass
    print('    User login name:', getpass.getuser())
    print('    Git Email:', github_email())
    print('    Linux system name:', socket.gethostname())
    print('    Python executable:',sys.executable)
    print('    Python version: ',sys.version)
    print('    OS Platform:',sys.platform)
    print('    Working Directory:',os.getcwd())
    print('    Start at:',time.asctime())
    print(len(report_heading) * '=')
    return

if __name__ == '__main__':
    #CheckForUpdates()
    #wait = input('Press ENTER to run the Lab Check...')
    if len(sys.argv) == 3:
        x = displayReportHeader()
    unittest.main()

