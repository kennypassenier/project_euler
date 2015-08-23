import os
import webbrowser

series = []
dosearch = ['south park',
            'american dad',
            'anger management',
            'elementary',
            'family guy',
            'modern family',
            'the big bang theory',
            'the simpsons',]
def librarynames(series):
    for i in os.listdir('I:\Series'):
        series.append(i)
        if i.lower() in dosearch:
            for j in os.listdir('I:\Series\%s' % (i)):
                if "Season" in str(j):
                    print(j)
            print('...')
    for i in os.listdir('L:\Series 2'):
        series.append(i)
        if i.lower() in dosearch:
            for j in os.listdir('L:\Series 2\%s' % (i)):
                if 'Season' in str(j):
                    print(j)
            print('...')
    else:
        series.sort()

def printinfo(series):
    print('There are currently %s series' % (len(series)))

def kickassopen(dosearch):
    for i in dosearch:
        url = 'http://kickass.so/usearch/' + str(i) + ' 1080 seeds:1/?field=seeders&sorder=desc'
        print(url)
"""
        webbrowser.open_new_tab(url)
"""

#-------------------------

librarynames(series)
for i in series:
    print(i)
printinfo(series)
for i in dosearch:
    print(i)
printinfo(dosearch)
print('...')
kickassopen(dosearch)