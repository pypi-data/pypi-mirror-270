import os

def importModels(path = ""):
    models = []
    valid, path = validatePath(0, path)
    if valid:
        modelsFile = open(path, "r")
        for line in modelsFile:
            if "class" in line:
                models.append(line[6:line.index("(")])
        modelsFile.close()

        return(models)
    else:
        return([])

def importViews(path = ""):
    templates = []
    templatePath = path
    inputs = []
    templateInputs = []
    saves = []
    currentFunction = ""
    valid, path = validatePath(1, path)
    if valid:
        
        viewsFile = open(path, "r")
        for line in viewsFile:
            if "template_name" in line:
                position = line[(line.index("name") + 8):line.index('"\n')]
                templates.append(position)
            elif "class" in line:
                currentFunction = line[(line.index("class") + 6):line.index("(")]
            elif "def" in line:
                currentFunction = line[(line.index("def") + 4):line.index("(")]
            elif "POST" in line:
                currentInput = line[(line.index("POST") + 6):line.index('"])')]
                inputs.append((currentInput, currentFunction))
            elif ".save()" in line:
                currentSave = line[:line.index(".save()")].replace(" ", "")
                saves.append((currentSave, currentFunction))
            
        viewsFile.close()
        for template in templates:
            currentTemplatePath = templatePath + "\\templates\\" + template
            try:
                currentTemplate = open(currentTemplatePath, "r")
            except:
                print("Non existent template referenced in views.py: " + currentTemplatePath)
                continue
            else:
                for line in currentTemplate:
                    if "input" and "name" in line:
                        name = line[(line.index('name=') + 6):].split('" ', 1)[0]
                        templateInputs.append((template, name))
                currentTemplate.close()
          
        return(inputs, templateInputs, saves)
    return([], [], [])
            
def validatePath(goal, path = ""):
    valid = False
    if goal == 0:
        if path == "":
            print("Please specficy the folder that models.py is in")
        else:
            if "models.py" not in path:
                if path[-1] == '\\': 
                    path += "models.py"
                else:
                    path += "\\models.py"
            try:
                modelsFile = open(path, "r")
            except IOError:
                print("Could not find models.py in " + str(path))
            else:
                valid = True
                modelsFile.close()
                
    elif goal == 1:
        if path == "":
            print("Please specficy the folder that views.py is in")
        else:
            if "views.py" not in path:
                if path[-1] == '\\': 
                    path += "views.py"
                else:
                    path += "\\views.py"
            try:
                viewsFile = open(path, "r")
            except IOError:
                print("Could not find views.py in " + str(path))
            else:
                valid = True
                viewsFile.close()

    return(valid, path)

def connectInputs(models, functions, templates, saves):
    for save in saves:
        currentFunction = save[1]
        currentModel = save[0]
        if "selected_" in currentModel:
            currentModel = currentModel.replace("selected_", "")
        links = []
        print("The model " + currentModel + " is affected by the function " + currentFunction)
        for request in functions:
            if request[1] == currentFunction:
                links.append(request[0])
        if links:
            for link in links:
                for template in templates:
                    if template[1] == link:
                        print('Potential vulnerability where the function "' + currentFunction + '" takes user input with the name "' + link + '" from the page "' + template[0] + '"')            
        else:
            print("no user inputs for " + currentFunction)
            continue

def vulidentify():
    models = []
    templates = []
    while not models:
        print("Please enter file path for models.py")
        path = input(">")
        models = importModels(path)

    while not templates:
        print("Please enter file path for views.py(this will likley be the same path)")
        path = input(">")
        functions, templates, saves = importViews(path)

    connectInputs(models, functions, templates, saves)
        
    
