from sys import argv
def run(string : str, variables = {}):
    string = string.strip()
    if string[0] == '$':
        index = 1
        character = string
        while index < len(string):
            character = string[index]
            if character != '{':
                print(character,end="")
            else:
                print(run(string[index+1:string.index('}',index+1)],variables),end="")
                index = string.index('}',index+1)
            index += 1      
        print(flush=True)
    elif string[0] == '@':
        if len(string) == 1 :
            return input()
        else:
            variables[string[1:]] = input()
    elif string[0] == '?':
        if getVal(string[1:string.index('>')],variables):
            return run(string[string.index('>')+1:string.index('~')],variables)
        else:
            return run(string[string.index('~')+1:],variables)
    elif string[0] == '[':
        variables["__this"] = string
        string = string[1:-1]
        paramList = []
        params = []
        
        paramList = string[:string.index('&')].split(',')
        for param in paramList:
            params.append((param[param.index('|')+1:],param[:param.index('|')]))
        for key,value in params:
            variables[key] = value
        string = string[string.index('&')+1:]
        run(string,variables)
        
    elif string[0] == '(':
        
        params = [x for x in map(lambda x:x.split('|')[1],variables["__this"].split('&')[0].split(','))]
        for index, param in enumerate(string[1:string.index(')')].split(',')):
            variables[params[index]] = getVal(param,variables)
        run(variables["__this"][variables["__this"].index('&')+1:-1],variables)
    elif string[0] == '\'':
        return string[1:]
    elif string[0] == '#':
        return len(run(string[1:],variables))
    elif string[0] == '.':
        if string[1] == '@':
            if len(string[1:]) == 1 :
                return input()
            else:
                variables[string[2:]] = input()
                return variables[string[2:]]
        elif '|' in string:
            variables[string[string.index('|')+1:]] = string[1:string.index('|')]
            return variables[string[string.index('|')+1:]]
    elif '|' in string:
        variables[string[string.index('|')+1:]] = string[:string.index('|')]
    elif True in list(map(lambda letter: letter in ['+','-','*','/','='], string)):
        
        string = string.replace('=','==')
        for key in variables.keys():
            if key in string:
                string = string.replace(key,variables[key])
        return eval(string)
    elif string[0].islower():
        return variables[string]
    else:
        return string
    return ""
def getVal(string : str, variables : dict):
    try:
        return eval(run(string,variables))
    except:
        return run(string, variables)
def main(file_path : str):
    if file_path[file_path.index(".")+1:] != "ap" :
        raise Exception("error : fuck off")
    with open(file_path,"r") as file1:
        for line in file1.readlines():
            run(line)

if __name__ == "__main__":
    main(argv[1])