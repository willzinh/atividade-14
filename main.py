from conversor import cm_para_pol

cm = float(input('Digite um valor em centímetros: '))
print('O valor {} em centímetros correponde a {} em polegadas.'.format(cm, cm_para_pol(cm)))