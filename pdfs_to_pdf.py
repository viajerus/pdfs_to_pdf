#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:14:54 2021

@author: viajerus

#script to merge many pdfs

"""
import os 
import glob
from PyPDF2 import PdfFileMerger


os.chdir(os.getcwd())


pdfs = []
for file in glob.glob("*.pdf"):
    pdfs.append(file)


    
merger = PdfFileMerger()

for pdf in sorted(pdfs):
    merger.append(pdf)

merger.write("Uebung4.pdf")
merger.close()
