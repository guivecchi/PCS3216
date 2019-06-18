# PCS3216
Repositório para o desenvolvimento do projeto da disciplina PCS3216 - 

## Processador Hospedeiro
O processador desenvolvido é uma máquina virtual desenvolvida na linguagem Python que roda sobre um processador hospedeiro em uma máquina real. A grande vantagem desta abordagem é a simplicidade de desenvolvimento enquanto que a desvantagem é a perda de performance devido ao fato de que o processador virtual roda sobre um software. 
Características de Memória, Registradores, Operações etc são descritas abaixo

## Memória 
* 16 bits por palavra, ou seja, palavras de 2 bytes. 
* 16 bits de endereçamento, ou seja, 4 dígitos hexadecimais formam cada endereço
* 2<sup>16</sup> = 65536 bytes = 32768 palavras = 64 Kbytes

## Registradores
* Acumulador (AC) = 2 bytes
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
* `JP xxxx` (código hexa: /0xxxx): salto incodicional para o endereço `xxxx` (endereços detonados em número hexadecimal)
* `JZ xxxx` (código hexa: /1xxxx): salta para o endereço `xxxx` se o valor no acumulador for igual a zero.
* `JN xxxx` (código hexa: /2xxxx): salta para o endereço `xxxx` se o valor no acumulador for negativo.
* `+ xxxx` (código hexa: /3xxxx): soma acumulador + conteúdo do endereço `xxxx`.
* `- xxxx`(código hexa: /4xxxx): subtrai acumulador - conteúdo do endereço `xxxx`.
* `* xxxx` (código hexa: /5xxxx): multiplica acumulador * conteúdo do endereço `xxxx`.
* `/ xxxx` (código hexa: /6xxxx): divide acumulador / conteúdo do endereço `xxxx`.
* `LD xxxx` (código hexa: /7xxxx): carrega acumulador com dado presente no endereço `xxxx`.
* `MM xxxx` (código hexa: /8xxxx): move o valor do acumulador para o endereço `xxxx`.
* `SC xxxx` (código hexa: /9xxxx): desvia para a sub-rotina que se inicia no endereço `xxxx`.
