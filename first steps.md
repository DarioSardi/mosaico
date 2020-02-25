
# creating db in ms azure.
creating tables from the online console (Editor di query)

```sql
CREATE TABLE STUDENTI (
    NOME varchar(255),
    COGNOME varchar(255),
    CF varchar(255),
	IBAN varchar(255)
); 

CREATE TABLE PROFESSORI (
    NOME varchar(255),
    COGNOME varchar(255)
); 
```

# sqlcmd
connessione tramite sqlcmd e elenco delle tabelle nel db Test tramite comando 

```sql
SELECT TABLE_NAME FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE="BASE TABLE"
GO
```
# setup spark
dopo l'installazione no func sql.
aggiunte linee a .zshrc.
avvio pyspark!
