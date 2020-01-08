#It will consist of list of all the important topics that are part of a language
#java checklist

languages = ('java','python','django','html','css','javascript','bootstrap')
java=('classes','objects','methods','oops','exception handling','interface','collections','generics','wrapper class','multithreading')

#python checklist
python=('list','tupples','sets','dictionary','list comprehension','function','lambda expressions','oops','classes','objects','exception handling','regex','decorators','generators','multithreading','multiprocessing')

#django checklist
django=('models','views','forms','templates','function based views','class based views','django architecture','jinja template','oops','middleware','admin','deployments')

#html checklist
html5=('head','styles','images','css','tables','lists','id','class','forms','links')

#css checklist
css=('colors','borders','backgrounds','margins','padding','height','widths','texts','fonts','forms','attrs')

#javascripts checklist
javascript=('variables','comments','operators','assignments','data types','functions','objects','events','strings','numbers','arrays','dates')

#bootstrap
bootstrap=('typography','tables','images','jumbotrons','containers','navbar','modals')

dict1 = dict()
dict1 = dict.fromkeys(languages)

dict1['java'] = java
dict1['python'] = python
dict1['django'] = django
dict1['html5'] = html5
dict1['css'] = css
dict1['javascript'] = javascript
dict1['bootstrap'] = bootstrap
#print(dict1)