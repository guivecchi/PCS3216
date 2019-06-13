# PCS3216
Repositório para o desenvolvimento do projeto da disciplina PCS3216 - 

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

## Blocos Funcionais
* Unidade Lógica Aritmética (ULA): Operações
* Unidade de Controle (UC): Instruções
