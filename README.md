# PCS3216
Repositório para o desenvolvimento do projeto da disciplina PCS3216 - 

## Processador Hospedeiro
O processador desenvolvido é uma máquina virtual desenvolvida na linguagem Python que roda sobre um processador hospedeiro em uma máquina real. A grande vantagem desta abordagem é a simplicidade de desenvolvimento enquanto que a desvantagem é a perda de performance devido ao fato de que o processador virtual roda sobre um software. 
Características de Memória, Registradores, Operações etc são descritas abaixo

## Memória 
* 16 bits por palavra, ou seja, palavras de 2 bytes. 
* 16 bits de endereçamento, ou seja, 4 dígitos hexadecimais formam cada endereço
* 2<sup>12</sup> = 4096 bytes = 2048 palavras = 4 Kbytes

## Registradores
* Acumulador (ACC) = 2 bytes
* Program Counter (PC) = 2 bytes
* Aritméticos/lógicos (2 bytes / Registrador)
  * A0 a A7: Registradores de endereço
  * D0 a D7: Registradores de dados

## Equipamentos de Entrada/Saída/Armazenamento
* **Entrada**: O equipamento de entrada usado pelo processador é o _stdin_ do processador hospedeiro. Neste caso, a entrada será um arquivo de texto com instruções ou instruções inseridas diretamente no terminal
* **Saída**: O equipamento de saída usado pelo processador é o _stdout_ do processador hospedeiro. Neste caso a saída será a impressão, no temrinal, dos valores dos registradores
* **Armazenamento**: Memória. Esta é implementada como um vetor de words com valor hexadecimal

## Blocos Funcionais
* Unidade Lógica Aritmética (ULA): Operações
* Unidade de Controle (UC): Instruções

## Operações 
* `JP xxx` (código hexa: /0xxx): salto incodicional para o endereço `xxx` (endereços detonados em número hexadecimal)
* `JZ xxx` (código hexa: /1xxx): salta para o endereço `xxx` se o valor no acumulador for igual a zero.
* `JN xxx` (código hexa: /2xxx): salta para o endereço `xxx` se o valor no acumulador for negativo.
* `+ xxx` (código hexa: /3xxx): soma acumulador + conteúdo do endereço `xxx`.
* `- xxx`(código hexa: /4xxx): subtrai acumulador - conteúdo do endereço `xxx`.
* `* xxx` (código hexa: /5xxx): multiplica acumulador * conteúdo do endereço `xxx`.
* `/ xxx` (código hexa: /6xxx): divide acumulador / conteúdo do endereço `xxx`.
* `LD xxx` (código hexa: /7xxx): carrega acumulador com dado presente no endereço `xxx`.
* `MM xxx` (código hexa: /8xxx): move o valor do acumulador para o endereço `xxx`.
* `SC xxx` (código hexa: /9xxx): desvia para a sub-rotina que se inicia no endereço `xxx`.
