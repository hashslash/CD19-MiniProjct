Output:

```

-------------------------------------------------------------------------------------------------------------------------------------
                      stack                       |            Input             |                      Action                      |
-------------------------------------------------------------------------------------------------------------------------------------

                       St                         |           datatype           |                  St > prog eoc                   |
                    eoc prog                      |           datatype           |    prog > datatype main ob cb begin code end     |
     eoc end code begin cb ob main datatype       |           datatype           |                  match datatype                  |
          eoc end code begin cb ob main           |             main             |                    match main                    |
            eoc end code begin cb ob              |              ob              |                     match ob                     |
              eoc end code begin cb               |              cb              |                     match cb                     |
               eoc end code begin                 |            begin             |                   match begin                    |
                  eoc end code                    |           datatype           |                 code > dec code                  |
                eoc end code dec                  |           datatype           |        dec > datatype id init varlist sc         |
    eoc end code sc varlist init id datatype      |           datatype           |                  match datatype                  |
         eoc end code sc varlist init id          |              id              |                     match id                     |
          eoc end code sc varlist init            |            comma             |                   init > null                    |
          eoc end code sc varlist null            |             null             |                    match null                    |
             eoc end code sc varlist              |            comma             |         varlist > comma id init varlist          |
      eoc end code sc varlist init id comma       |            comma             |                   match comma                    |
         eoc end code sc varlist init id          |              id              |                     match id                     |
          eoc end code sc varlist init            |             equ              |                 init > equ num                   |
         eoc end code sc varlist num equ          |             equ              |                    match equ                     |
           eoc end code sc varlist num            |             num              |                    match num                     |
             eoc end code sc varlist              |              sc              |                 varlist > null                   |
              eoc end code sc null                |             null             |                    match null                    |
                 eoc end code sc                  |              sc              |                     match sc                     |
                  eoc end code                    |            while             |              code > whileloop code               |
             eoc end code whileloop               |            while             |    whileloop > while ob R cb begin code end      |
    eoc end code end code begin cb R ob while     |            while             |                   match while                    |
       eoc end code end code begin cb R ob        |              ob              |                     match ob                     |
        eoc end code end code begin cb R          |              id              |                    R > F R'                      |
       eoc end code end code begin cb R' F        |              id              |                     F > id                       |
      eoc end code end code begin cb R' id        |              id              |                     match id                     |
        eoc end code end code begin cb R'         |             rop              |                  R' > rop F R'                   |
     eoc end code end code begin cb R' F rop      |             rop              |                    match rop                     |
       eoc end code end code begin cb R' F        |              id              |                     F > id                       |
      eoc end code end code begin cb R' id        |              id              |                     match id                     |
        eoc end code end code begin cb R'         |              cb              |                    R' > null                     |
       eoc end code end code begin cb null        |             null             |                    match null                    |
         eoc end code end code begin cb           |              cb              |                     match cb                     |
           eoc end code end code begin            |            begin             |                   match begin                    |
              eoc end code end code               |           datatype           |                 code > dec code                  |
            eoc end code end code dec             |           datatype           |        dec > datatype id init varlist sc         |
eoc end code end code sc varlist init id datatype |           datatype           |                  match datatype                  |
    eoc end code end code sc varlist init id      |              id              |                     match id                     |
      eoc end code end code sc varlist init       |             equ              |                 init > equ num                   |
    eoc end code end code sc varlist num equ      |             equ              |                    match equ                     |
      eoc end code end code sc varlist num        |             num              |                    match num                     |
        eoc end code end code sc varlist          |              sc              |                 varlist > null                   |
          eoc end code end code sc null           |             null             |                    match null                    |
            eoc end code end code sc              |              sc              |                     match sc                     |
              eoc end code end code               |              id              |                 code > eq code                   |
            eoc end code end code eq              |              id              |                eq > id equ E sc                  |
        eoc end code end code sc E equ id         |              id              |                     match id                     |
         eoc end code end code sc E equ           |             equ              |                    match equ                     |
           eoc end code end code sc E             |              id              |                    E > T E'                      |
          eoc end code end code sc E' T           |              id              |                     T > id                       |
         eoc end code end code sc E' id           |              id              |                     match id                     |
           eoc end code end code sc E'            |              op              |                  E' > op T E'                    |
        eoc end code end code sc E' T op          |              op              |                     match op                     |
          eoc end code end code sc E' T           |              id              |                     T > id                       |
         eoc end code end code sc E' id           |              id              |                     match id                     |
           eoc end code end code sc E'            |              sc              |                    E' > null                     |
          eoc end code end code sc null           |             null             |                    match null                    |
            eoc end code end code sc              |              sc              |                     match sc                     |
              eoc end code end code               |             end              |                   code > null                    |
              eoc end code end null               |             null             |                    match null                    |
                eoc end code end                  |             end              |                    match end                     |
                  eoc end code                    |             end              |                   code > null                    |
                  eoc end null                    |             null             |                    match null                    |
                     eoc end                      |             end              |                    match end                     |
                       eoc                        |             eoc              |                    match eoc                     |
-------------------------------------------------------------------------------------------------------------------------------------

Parsing Successfull
Valid

```