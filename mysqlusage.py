# -*- coding: cp936 -*-
#django mysql ����

from rest_server import Student
from rest_server import Teacher
#��Զ���������teacher����
a=Student.objects.get(name='mike')
#'get' get object 
b=Teacher.objects.get(name='lishiye')
a.myteacher.all()
b.student.all()

Student.objects.create(name='liyuanye',sex='male')
a.myteacher.add(b)
b.student.add(a)

#���²���
#'filter' get queryset
Student.objects.filter(name='mike').update(name='lee')

#ɾ������
Student.objects.filter(name='lee').delete()










#mysql���ݿ����

#login: mysql -uroot -p
create table if not exists tablename(1:2,3:4);
drop table tablename;
show columns from tablename;
#�޸�����������
alter table tablename drop/add columnname;
alter table tablename modify coluname int;
alter table tablename change coluname newcolumname;
#�޸ı���
alter table tablename rename to newtablename;


#��
insert into tablename values (1,'mike');
#ɾ
delete from tablename where name='mike' and id=1;
#��
update tablename set name='lee',sex='female' where id=1;
#��
select from tablename where name='mike' order by id desc;
select from tablename where name like '%m%';
select from tablename where name REGEXP '^$'
select name,count(*) from tablename group by name;
select a.name,b.schoole from t1 a inner/left/right join t2 b on a.name=b.name;
select * from t1 where count is null/not null;
