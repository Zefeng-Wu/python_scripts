from Bio import Entrez
from lxml import etree
import re
Entrez.email = "835102330@qq.com"

"""
search_handle = Entrez.esearch(db="sra",term="Arabidopsis")
search_record = Entrez.read(search_handle)
print search_record["IdList"]
"""

handle = Entrez.efetch(db="sra",term="Arabidopsis")
record = handle.read() #contain detailed information about RNA-seq sample

regexes = {
    'accession': '<EXPERIMENT\s+.*?accession="(?P<accession>.*?)".*?>',
    'title': '<EXPERIMENT\s+.*?>.*?<TITLE>(?P<title>.*?)<\/TITLE>',
    'study_title': '<STUDY_TITLE>(?P<study_title>.*?)<\/STUDY_TITLE>',
    'library_strategy': '<LIBRARY_STRATEGY>(?P<library_strategy>.*?)<\/LIBRARY_STRATEGY>',
    'library_layout': '<LIBRARY_LAYOUT>\s*<(?P<library_layout>SINGLE|PAIRED)',
    'instrument_model': '<INSTRUMENT_MODEL>(?P<instrument_model>.*?)<\/INSTRUMENT_MODEL>',
    'taxon_id': '<TAXON_ID>(?P<taxon_id>.*?)<\/TAXON_ID>',
    'scientific_name': '<SCIENTIFIC_NAME>(?P<scientific_name>.*?)<\/SCIENTIFIC_NAME>',
    'run_accession': '<RUN\s+.*?accession="(?P<run_accession>.*?)"\s+.*?total_spots="(?P<total_spots>.*?)"\s+.*?total_bases="(?P<total_bases>.*?)"\s+.*?size="(?P<size>.*?)"\s+.*?published="(?P<published>.*?)"\s+.*?>',
    'nreads': '<Statistics\s+.*?nreads="(?P<nreads>.*?)"\s+.*?>',
    'read_average': '<Read\s+.*?average="(?P<read_average>.*?)"\s+.*?\/>',
}

fields = {}

for field, regex in regexes.iteritems():
    re_search = re.search(regex, record)
    if re_search:
        re_groups = re_search.groupdict()
        if re_groups:
            for k, v in re_groups.iteritems():
                fields[k] = v
        else:
            if field in ['taxon_id', 'nreads', 'read_average',
                         'total_spots', 'total_bases', 'size']:
                fields[field] = 0
            else:
                fields[field] = ''
    else:
        if field in ['taxon_id', 'nreads', 'read_average',
                     'total_spots', 'total_bases', 'size']:
            fields[field] = 0
        else:
            fields[field] = ''

print(int(float(fields['read_average'])))
print fields


"""

handle = Entrez.einfo() #xml: list all database in ncbi
record = Entrez.read(handle) #parse xml to dictionary
print record.keys()
print record["DbList"]
"""

"""
handle = Entrez.einfo(db="sra")
record = Entrez.read(handle)
print record["DbInfo"]["Count"]
print record["DbInfo"]["LastUpdate"]
"""
