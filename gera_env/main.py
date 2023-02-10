import os
import json

arquivo = "captura.json"
outputsTF = list()
global_model = os.environ.get('GLOBAL_MODEL')

os.system(f'echo $(terraform output -json) >> {arquivo}')
with open(arquivo) as file:
    data = json.load(file)


def separarJson():
    quant_array = len(data)
    for keyName in data:
        outputsTF.insert(quant_array, keyName)
    criarTfvars(outputsTF)
    os.system('terraform fmt --recursive')
    # os.system(f'cp {global_model}.tfvars teste.tfvars')
    os.system(f'echo -e $(cat {global_model}.tfvars) >> $(pwd)/../front/terraform.tfvars')
    os.system('cat $(find $(pwd)/../front -name "*.tfvars")')


def criarTfvars(procurar: list):
    tamanho = len(procurar)
    if tamanho >= 0:
        for value in range(0, tamanho, 1):
            itens = procurar[value]
            res = data[f"{itens}"]["value"]
            tfvars = open(f"{global_model}.tfvars", '+a')
            write_model = (f'\n{itens} = \"{res}\"#\\n')
            tfvars.write(write_model)
    else:
        print("!!PROBLEMA!!")


if __name__ == '__main__':
    separarJson()
