#! /usr/bin/python

import pdfplumber
import pandas as pd

with pdfplumber.open("/home/wuzefeng/Zotero/storage/E6EDD3T7/mmc1.pdf") as pdf:
    page = pdf.pages[9] #带有表格的页面
    #text = page.extract_text()
    #print (text)
    
    tables = page.extract_tables()
    for t in tables:
        df = pd.DataFrame(t[1:],columns=t[0])
        df.to_csv("~/Desktop/AM_genes1.csv")
        print (df)
    
with pdfplumber.open("/home/wuzefeng/Zotero/storage/E6EDD3T7/mmc1.pdf") as pdf:
    page = pdf.pages[10] #带有表格的页面
    #text = page.extract_text()
    #print (text)
    
    tables = page.extract_tables()
    for t in tables:
        df = pd.DataFrame(t[1:],columns=t[0])
        df.to_csv("~/Desktop/AM_genes2.csv")
        print (df)