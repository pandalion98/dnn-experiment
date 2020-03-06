import xmltodict as xD

root = xD.parse(open('arxiv-eess/oai2-11.xml', mode='rb'))
records = root['OAI-PMH']['ListRecords']['record']
file = open('eess-oai10-delimited.txt', "a+")

for record in records:
    # print(record['metadata']['arXiv']['title'].replace('\n ', '') + '\n')
    # print(record['metadata']['arXiv']['abstract'].replace('\n ', '') + '\n\n\n')
    file.write('< | start | >\n')
    file.write(record['metadata']['arXiv']['title'].replace('\n ', '') + '\n\n')
    file.write(record['metadata']['arXiv']['abstract'] + '\n')
    file.write('< | end | >\n\n')

file.close()  # This close() is important

# for record in root.find('.//{http://www.openarchives.org/OAI/2.0/}record'):
# for child in root[2]:
#     print(child[1][0][4].tag)
