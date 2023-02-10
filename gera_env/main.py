import os
import json

arquivo = "captura.json"
outputsTF = list()
globalModel = os.environ.get('GLOBAL_MODEL')

os.system(f'echo $(terraform output -json) >> {arquivo}')
with open(arquivo) as file:
    data = json.load(file)


def separarJson():
    quantArray = len(data)
    for keyName in data:
        outputsTF.insert(quantArray, keyName)
    criarTfvars(outputsTF)
    os.system('terraform fmt --recursive')
    # os.system(f'cp {globalModel}.tfvars teste.tfvars')
    os.system(
        f'echo -e $(cat {globalModel}.tfvars) >> $(pwd)/../front/terraform.tfvars')
    os.system('cat $(find $(pwd)/../front -name "*.tfvars")')


def criarTfvars(procurar: list):
    tamanho = len(procurar)
    if tamanho >= 0:
        for value in range(0, tamanho, 1):
            itens = procurar[value]
            res = data[f"{itens}"]["value"]
            tfvars = open(f"{globalModel}.tfvars", '+a')
            writeModel = (f'\n{itens} = \"{res}\"#\\n')
            tfvars.write(writeModel)
    else:
        print("!!PROBLEMA!!")


if __name__ == '__main__':
    separarJson()
