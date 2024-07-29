##### Simbología:
- xx = 0.2
- x = 0.1
- y = 0.05
- clase agrega un 0.05 al stat principal si se usa en la fórmula
  - por ej. AGI es el principal de THIEF por lo tanto cada stat que usa agi se le suma 0.05

| STAT | INFLUYE                   |
| ---- | ------------------------- |
| STR  | HP(xx), HIT(y), DMG (x)   |
| AGI  | EVA(x), DMG(y), HIT(x)    |
| INT  | MGDMG(xx), HIT(y), EVA(y) |


## Formulas:

##### BASES:
```
HP      = base + [(STR * xx)]
DMG     = base + [(STR * x) + (AGI * y)]
HIT     = base + [(STR * y) + (AGI * x) + (INT * y)]
EVA     = base + [(AGI * x) + (INT * y)]
MGDMG   = base + [(INT * xx)]
```

##### WARRIOR
```
HP      = base + (STR * 0.25)
DMG     = base + (STR * 0.15)
HIT     = base + (STR * 0.1 + AGI * 0.05 + INT * 0.05)
EVA     = base + (AGI * 0.1 + INT * 0.05)
MGDMG   = base + (INT * 0.2)
```

##### THIEF
```
HP      = base + [(STR * 0.2)]
DMG     = base + [(STR * 0.1) + (AGI * 0.1)]
HIT     = base + [(STR * 0.05) + (AGI * 0.15) + (INT * 0.05)]
EVA     = base + [(AGI * 0.15) + (INT * 0.05)]
MGDMG   = base + [(INT * 0.2)]
```
##### MAGE

```
HP      = base + [(STR * 0.2)]
DMG     = base + [(STR * 0.1) + (AGI * 0.05)]
HIT     = base + [(STR * 0.05) + (AGI * 0.1) + (INT * 0.1)]
EVA     = base + [(AGI * 0.05) + (INT * 0.1)]
MGDMG   = base + [(INT * 0.25)]
```