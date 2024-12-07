(20 pts) Crie uma classe que representa um funcionário, registrando seu nome, salário e data de admissão. Em seguida, crie uma classe que represente um departamento de uma empresa, registrando o nome e os funcionários que nele trabalham (use lista ou dicionário, considere um máximo de 20 funcionários). Por fim, crie uma classe que representa uma empresa, registrando seu nome, CNPJ e departamentos (considere um máximo de 10 departamentos). As classes funcionário e departamento têm relacionamento de agregação, enquanto, departamento e empresa têm relacionamento de composição.
Faça um programa principal que:

- Crie uma empresa;
- Adicione a esta empresa alguns departamentos;
- Adicione aos departamentos alguns funcionários;
- Dê aumento de 10% a todos os funcionários de um determinado departamento;
- Transfira um funcionário de um departamento para outro.

É esperado que seu código seja bem encapsulado. Por exemplo, para adicionar um departamento em uma empresa (ou um funcionário a um departamento), não se deve acessar a lista (ou dicionário) de departamentos diretamente, mas sim ter um método para esse fim.
