# Projekt_04 Engeto Academy: Task manager

Tento projekt slouží k **procvičení manuálního testování Task manageru**, 
který jsem sama naprogramovala a otestovala, podle mnou napsaných testovacích případů

---

## Instalace ##

### 1. Klonování repozitáře
Naklonujte nebo stáhněte tento projekt do svého počítače.

### 2. Vytvoření a aktivace virtuálního prostředí v terminálu
Doporučený postup je spustit projekt v samostatném virtuálním prostředí:

| python -m venv venv      |               |
|--------------------------|---------------|
|                          |               |
| source venv/bin/activate | # Linux / Mac |
| venv\Scripts\activate    | # Windows     |


### 3. Instalace závislostí
Žádné další závislosti nejsou potřeba

### 4. Použití
**Soubor main.py spusťte v jakémkoliv editoru kódu a dle souboru testovaci_pripady.txt otestujte**


## Ukázkový výstup programu

Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu

Vyberte možnost (1-4): 1

Zadejte název úkolu: uklid

Zadejte popis úkolu: nadobi, pracka

Úkol "uklid" byl přidán.

Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu

Vyberte možnost (1-4): 2

Seznam úkolů:
1. uklid - nadobi, pracka

Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu

Vyberte možnost (1-4): 3

Seznam úkolů:
1. uklid - nadobi, pracka

Zadejte číslo úkolu, který chcete odstranit: 1

Úkol "uklid" byl odstraněn.

Správce úkolů - Hlavní menu
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu

Vyberte možnost (1-4): 4

Konec programu.


## Očekávaný výstup
Task manager po každém vykonaném požadavku znovu vypíše hlavní menu dokud není program ukončen volbou č. 4.






