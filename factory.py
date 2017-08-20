from jinja2 import Template
import json

def readFile(filename):
    with open(filename) as file:
        return file.read()

def writeFile(filename,content):
    with open(filename,'w') as file:
        file.write(content)

def FileToTemplate(filename):
    return Template(readFile(filename))

writeFile("container.conf",FileToTemplate("container.conf.tpl").render(containers = json.loads(readFile("config.json"))))