def get_todos(path,type,todos=None):
  """
  Função para ler arquivos e gravar em arquivos
  path - é o caminho do arquivos
  type - é o tipo de operação no arquivo r ou w
  opcionais: 'todos' é um parâmetro opcional para setar a lista que deseja gravar no arquivo
  """
  if type == "r":
    with open(path, type) as file:
      return file.readlines()
  else:
    with open(path, type) as file:
      return file.writelines(todos)
