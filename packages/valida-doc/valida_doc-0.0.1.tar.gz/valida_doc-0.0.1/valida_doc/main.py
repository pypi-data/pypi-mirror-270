"""Validador de Documentos

Realiza a validação de documentos de acordo com os algorítimos estabelecidos
em cada órgão.

---Utilização
    - Se o documento não apresentar todas as características pertinentes a ele
    como número de caracteres ou somente números, ele retornará uma str com
    erro;
    - Se um documento for válido ele retornará um bool True;
    - Se um documento for inválido ele retornará um bool False;

---Documentos para validação
    - CPF
    - RG 
        - Secretaria de Seguraça Pública de São Paulo
"""

class Documento:
    def cpf(self, cpf: str):
        if not isinstance(cpf, str):
            return "CPF deve ser uma string."
        cpf = cpf.replace('.', '').replace('-', '').strip()
        if not cpf.isdigit():
            return "CPF deve conter apenas dígitos."
        if len(cpf) != 11:
            return "CPF deve ter exatamente 11 dígitos."
        if cpf == cpf[0] * 11:
            return "CPF inválido - todos os dígitos são iguais"
        dig1 = dig2 = 0
        for i, j in zip(range(9), range(10, 1, -1)):
            dig1 += int(cpf[i]) * j
        dig1 = (dig1 * 10 % 11) % 10
        for i, j in zip(range(10), range(11, 1, -1)):
            dig2 += int(cpf[i]) * j
        dig2 = (dig2 * 10 % 11) % 10
        if cpf[-2:] == f"{dig1}{dig2}":
            return True
        else:
            return False

    def rg_sp(self, rg: str):
        if not isinstance(rg, str):
            return "RG deve ser uma string."
        rg = rg.replace('.', '').replace('-', '').strip().lower()
        if len(rg) != 9:
            return "RG deve ter exatamente 9 dígitos."
        if rg == rg[0] * 9:
            return "RG inválido - todos os dígitos são iguais"
        dig1 = 0
        for i, j in zip(range(9), range(9, 1, -1)):
            dig1 += int(rg[i]) * j
        dig1 = dig1 % 11
        if dig1 == 10:
            dig1 = "x"
        if rg[-1:] == f"{dig1}":
            return True
        else:
            return False

        
_inst = Documento()
cpf = _inst.cpf
rg_sp = _inst.rg_sp