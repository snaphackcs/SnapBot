
# Initialization

use 

```shell
sqlite3 userdata.db
```
to create the database

# The structure of the database


![db struct](./img/db_struct.svg)
（注：这张图只是个大概）
## notes:
- `sign.compulitity`: the currency inside the wechat bot
- `class_register.grade_class`: this should be a integer of four digit, the first two digits specifies the grade, the second two digit specifies the class. example: 1010 means grade 10 class 10
- `class_register.registered_lesson`: a json string