from django.shortcuts import render
import sys

# Create your views here.
def compiler(request):
    return render(request, 'PythonCompiler/compiler.html')

def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']
        danger_lib = ['os', 'sys', 'subprocess']
        danger_func = ['import', 'from', '__import__("', 'system']
        for i in danger_lib:
            for j in danger_func:
                if (j + ' ' + i in codeareadata) or (j + i in codeareadata) or (i + '.' + j in codeareadata) or ('__builtins__' in codeareadata):
                    codeareadata = 'в компиляторе запрещено использование системных библиотек или переименование методов "import" и "from"'
        try:
            sys.stdout = open('file.txt', 'w')
            original_stdout = sys.stdout

            exec(codeareadata)

            sys.stdout.close()

            sys.stdout = original_stdout

            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout = original_stdout
            output = e
    return render(request, 'PythonCompiler/compiler.html', {"code":codeareadata, "output":output})