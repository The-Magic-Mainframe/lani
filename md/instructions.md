# instructions.md

## Assembly
See [Assembler instruction statements - IBM Documentation](https://www.ibm.com/docs/en/zos/2.1.0?topic=reference-assembler-instruction-statements).

### Program Control
* `AINSERT`
* `CNOP` - Maybe
* `COPY` - Maybe
* `END` - MVP
* `EXITCTL`
* `ICTL`
* `ISEQ`
* `LTORG` - MVP
* `ORG` - MVP
* `POP` - MVP (partial)
* `PUNCH`
* `PUSH` - MVP (partial)
* `REPRO` - Maybe

### Listing Control
* `CEJECT` - MVP
* `EJECT` - MVP
* `PRINT` - MVP (partial)
* `SPACE` - MVP
* `TITLE` - MVP

### Operation Code Definition
* `OPSYN`

### Program Section and Linking
* `ALIAS`
* `AMODE` - MVP
* `CATTR`
* `COM`
* `CSECT` - MVP
* `CXD`
* `DSECT` - MVP
* `DXD`
* `ENTRY` - MVP
* `EXTRN`
* `LOCTR` - MVP
* `RMODE` - MVP
* `RSECT`
* `START`
* `WXTRN`
* `XATTR`

### Base Register
* `DROP` - MVP
* `USING` - MVP

### Data Definition
* `CCW` - Maybe
* `CCW0` - Maybe
* `CCW1` - Maybe
* `DC` - MVP
* `DS` - MVP

### Symbol Definition
* `EQU` - MVP

### Associated Data
* `ADATA`

### Assembler Options
* `*PROCESS` - MVP (partial)
* `ACONTROL` - MVP (partial)

## Macro
Some subset of these at python "compile time"
Some subset of these via C preprocessor?

### Prototype Statement
* `MACRO`
* `GBLA`
* `GBLB`
* `GBLC`
* `LCLA`

### Model Statement
* `SETA`
* `SETAF`
* `SETB`
* `SETC`
* `SETCF`
* `MNOTE`

## Machine
All documented z/Architecture machine instructions. Support z16
and eventually support compatibility modes (ESA/390, ESA/370, 
S/370, and S/360)

### General

### Decimal

### Floating-Point

### Control

### I/O

### Hex-Floating-Point

### Binary-Floating-Point

### Decimal-Floating-Point

### Vector Integer

### Vector String

### Special
