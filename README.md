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
* Ponteiro de pilha (SP) = 2 bytes
* Program Counter (PC) = 2 bytes
* Aritméticos/lógicos (2 bytes / Registrador)
  * A0 a A7: Registradores de endereço
  * D0 a D7: Registradores de dados
* Registrador de Status (SR) = 1 byte, mas apenas 3 bits serão utilizados indicando, respectivamente, Valor Zero, Valor Negativo e Overflow

## Equipamentos de Entrada/Saída/Armazenamento
* **Entrada**: O equipamento de entrada usado pelo processador é o _stdin_ do processador hospedeiro. Neste caso, a entrada será um arquivo de texto com instruções ou instruções inseridas diretamente no terminal
* **Saída**: O equipamento de saída usado pelo processador é o _stdout_ do processador hospedeiro. Neste caso a saída será a impressão, no temrinal, dos valores dos registradores
* **Armazenamento**: Memória. Esta é implementada como um vetor de words com valor hexadecimal

## Blocos Funcionais
* Unidade Lógica Aritmética (ULA): Operações
* Unidade de Controle (UC): Instruções

## Operações
* `JMP xxxx`: salto incodicional para o endereço `xxxx` (endereços detonados em número decimal)
* `JZR xxxx`: salta para o endereço `xxxx` se o indicador de Valor Zero do SR estiver ativo, ou seja, se uma operação anterior teve resultado igual à zero
* `JNG xxxx`: salta para o endereço `xxxx` se o indicador de Valor Negativo do SR estiver ativo, ou seja, se uma operação anterior teve resultado negativo
* `BSR xxxx`: salta para a subrotina que se inicia no endereço `xxxx`
* `SUM xxxx yyyy`: soma os valores presentes nos endereços `xxxx` e `yyyy` da memória e armazena a resposta em `xxxx`
* `SUB xxxx yyyy`: subtrai o valor presente no endereço `yyyy` de `xxxx` e armazena a resposta em `xxxx`
* `MUL xxxx yyyy`: multiplica os valores presentes nos endereços `xxxx` e `yyyy` e armazena em `xxxx`
* `DIV xxxx yyyy`: divide os valores presentes nos endereços `xxxx`e `yyyy` e armazena em `xxxx`
* `STR xxxx 0xZZZZZZZZ`: armazena a word hexadecimal `ZZZZZZZZ` no endereço `xxxx`
