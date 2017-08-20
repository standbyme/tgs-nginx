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

containers = json.loads(readFile("config.json"))

writeFile("Dockerfile",FileToTemplate("Dockerfile.tpl").render(containers = json.loads(readFile("config.json"))))
for container in containers:
    writeFile(container['name']+".conf",FileToTemplate("container.conf.tpl").render(container))