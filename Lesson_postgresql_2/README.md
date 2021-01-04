### **Postgresql lesson**

==================

This is a brief description of the created "movies" database.

#### **Content**

The database contains several tables where four of them relate to the task. Other tables shall be disregarded.

Relevant tables:
1. films
    ```    
    id - serial
	film - varchar(100)
	director - varchar(100)
   ```
2. actors
    ```    
    id - serial
	actor - varchar(100)
	film - varchar(100)
   ```
3. directors
    ```    
    id - serial
	director - varchar(100)
   ```
4. result_table
    ```    
    id_film - varchar(100)
	id_director - varchar(100)
	id_actor - varchar(100)
   ```