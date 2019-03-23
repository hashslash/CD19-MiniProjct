# CD19-MiniProjct

A LL(1) Parser for a code snippet already

### About Lex Tool:
The default tokens are 'eoc' and 'null' which all cases should include it can be used for any kind of regular languages

## Usage:
``` python
lex = LexicalAnalyser(token_identifiers,code_data)
lex.get_next_token()
```
### About Parser:
The default grammer are St=>S eoc (Acceptance Grammer) which all cases should include it can be used for any kind of Context-free Grammars

#### Usage:
``` python
parser = parser(token_identifiers,grammar)
parser.parse(code_data)
```


## example:

Grammar
```
St S eoc
S a
S hat
S obrac T cbrac
T S Tt
Tt c S Tt
Tt null
```

Tokens
```
a a
hat ^
obrac \(
cbrac \)
null ~
eoc \$
c ,
```

Input 1
```buildoutcfg
(a))$
```

Output 1
```buildoutcfg

----------------***Tokens***----------------
|   a
|   hat
|   obrac
|   cbrac
|   null
|   eoc
|   c
--------------------------------------------


--------------***Grammar***-----------------
|   St =>> S eoc 
|   S =>> a 
|   S =>> hat 
|   S =>> obrac T cbrac 
|   T =>> S Tt 
|   Tt =>> c S Tt 
|   Tt =>> null 
--------------------------------------------


-----------***parse table***--------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
variables ||                    a                   ||                    c                   ||                  obrac                 ||                   eoc                  ||                  cbrac                 ||                   hat                  |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Tt    ||                                        ||             Tt =>> c S Tt              ||                                        ||                                        ||              Tt =>> null               ||                                        |
    S     ||                S =>> a                 ||                                        ||          S =>> obrac T cbrac           ||                                        ||                                        ||               S =>> hat                |
    T     ||              T =>> S Tt                ||                                        ||              T =>> S Tt                ||                                        ||                                        ||              T =>> S Tt                |
    St    ||             St =>> S eoc               ||                                        ||             St =>> S eoc               ||                                        ||                                        ||             St =>> S eoc               |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Grammer is LL1
Parsing...
                      stack                       |                      Input                       |                      Action                      |
--------------------------------------------------------------------------------------------------------------------------------------------------------

                       St                         |                        (                         |                  St =>> S eoc                    |
                      eoc S                       |                        (                         |               S =>> obrac T cbrac                |
                eoc cbrac T obrac                 |                        (                         |                   match obrac                    |
                   eoc cbrac T                    |                        a                         |                   T =>> S Tt                     |
                 eoc cbrac Tt S                   |                        a                         |                     S =>> a                      |
                 eoc cbrac Tt a                   |                        a                         |                     match a                      |
                  eoc cbrac Tt                    |                        )                         |                   Tt =>> null                    |
                 eoc cbrac null                   |                       null                       |                    match null                    |
                    eoc cbrac                     |                        )                         |                   match cbrac                    |
                       eoc                        |                        )                         |
Expected eoc Found cbrac
```


Input 2
```buildoutcfg
(a)$
```

Output 2
```buildoutcfg
----------------***Tokens***----------------
|   a
|   hat
|   obrac
|   cbrac
|   null
|   eoc
|   c
--------------------------------------------


--------------***Grammar***-----------------
|   St =>> S eoc 
|   S =>> a 
|   S =>> hat 
|   S =>> obrac T cbrac 
|   T =>> S Tt 
|   Tt =>> c S Tt 
|   Tt =>> null 
--------------------------------------------


-----------***parse table***--------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
variables ||                    a                   ||                    c                   ||                  obrac                 ||                   eoc                  ||                  cbrac                 ||                   hat                  |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Tt    ||                                        ||             Tt =>> c S Tt              ||                                        ||                                        ||              Tt =>> null               ||                                        |
    S     ||                S =>> a                 ||                                        ||          S =>> obrac T cbrac           ||                                        ||                                        ||               S =>> hat                |
    T     ||              T =>> S Tt                ||                                        ||              T =>> S Tt                ||                                        ||                                        ||              T =>> S Tt                |
    St    ||             St =>> S eoc               ||                                        ||             St =>> S eoc               ||                                        ||                                        ||             St =>> S eoc               |
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Grammer is LL1
Parsing...
                      stack                       |                      Input                       |                      Action                      |
--------------------------------------------------------------------------------------------------------------------------------------------------------

                       St                         |                        (                         |                  St =>> S eoc                    |
                      eoc S                       |                        (                         |               S =>> obrac T cbrac                |
                eoc cbrac T obrac                 |                        (                         |                   match obrac                    |
                   eoc cbrac T                    |                        a                         |                   T =>> S Tt                     |
                 eoc cbrac Tt S                   |                        a                         |                     S =>> a                      |
                 eoc cbrac Tt a                   |                        a                         |                     match a                      |
                  eoc cbrac Tt                    |                        )                         |                   Tt =>> null                    |
                 eoc cbrac null                   |                       null                       |                    match null                    |
                    eoc cbrac                     |                        )                         |                   match cbrac                    |
                       eoc                        |                        $                         |                    match eoc                     |
                                                  |
Parsing Successfull
Valid
```

Examples are provided for help.
copy files in examples to source and check...