# -*- coding: cp936 -*-
import mysql.connector
class Database(object):
##############################################################################################################################

        ##����ָ�������Ƿ��ڱ���
        ##������name:����
        ##����ֵ������:True
        ##        ����False
        def find_languages_data(self,name):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()                    
                cursor.execute('select * from languages where name= %s',(name,))
                values=cursor.fetchall()
                if len(values)>0:
                        n=True;
                else:
                        n=False;
                cursor.close()
                conn.close()
                return n
        
        ##����languages������
        ##������name:����
        ##      number:��Ӧ���Ե���Ŀ����
        def update_languages_data(self,name,number):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                if self.find_languages_data(name):
                        cursor.execute('update languages set number=%s where name=%s',[number,name])
                else:
                        cursor.execute('insert into languages (name,number) values (%s,%s)',[name,number])
                conn.commit()
                cursor.close()
                conn.close()

        ##��ȡlanguages������
        ##���أ�������������
        def read_languages_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from languages')
                values=cursor.fetchall()                
                cursor.close()
                conn.close()
                return values

 
##############################################################################################################################

        ##����ָ������Ƿ��ڱ���
        ##������year:���
        ##����ֵ������:True
        ##        ����False
        def find_repositories_data(self,year):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()                        
                cursor.execute('select * from repositories where year= %s',(year,))
                values=cursor.fetchall()
                if len(values)>0:
                        n=True;
                else:
                        n=False;
                cursor.close()
                conn.close()
                return n
        
        ##����repositories������
        ##������year:���
        ##      number:��Ӧ��ݵĲֿ�����
        def update_repositories_data(self,year,number):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                if self.find_repositories_data(year):
                        cursor.execute('update repositories set number=%s where year=%s',[number,year])
                else:
                        cursor.execute('insert into repositories (year,number) values (%s,%s)',[year,number])
                conn.commit()
                cursor.close()
                conn.close()

        ##��ȡrepositories������
        ##���أ�������������
        def read_repositories_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from repositories')
                values=cursor.fetchall()
                cursor.close()
                conn.close()
                return values

                        
##############################################################################################################################

        ##����ָ��id���Ƿ��ڱ���
        ##������myid:id��
        ##����ֵ������:True
        ##        ����False
        def find_projects_data(self,myid):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()                        
                cursor.execute('select * from projects where id= %s',(myid,))
                values=cursor.fetchall()
                if len(values)>0:
                        n=True;
                else:
                        n=False;
                cursor.close()
                conn.close()
                return n
                        
        ##����projects������
        ##������myid:id��
        ##      name:��Ŀ����
        ##      address:��Ŀ��ַ
        def update_projects_data(self,myid,name,address):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                if self.find_projects_data(myid):
                        cursor.execute('update projects set name=%s,address=%s where id=%s',[name,address,myid])
                else:
                        cursor.execute('insert into projects (id,name,address) values (%s,%s,%s)',[myid,name,address])
                conn.commit()
                cursor.close()
                conn.close()

        ##��ȡprojects������
        ##���أ�������������
        def read_projects_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from projects')
                values=cursor.fetchall()
                cursor.close()
                conn.close()
                return values
                        
##############################################################################################################################
 
        ##����ָ�������Ƿ��ڱ���
        ##������name:��������
        ##����ֵ������:True
        ##        ����False
        def find_locations_data(self,name):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()                        
                cursor.execute('select * from locations where name= %s',(name,))
                values=cursor.fetchall()
                if len(values)>0:
                        n=True;
                else:
                        n=False;
                cursor.close()
                conn.close()
                return n
        
        ##����locations������
        def update_locations_data(self,name,number):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                if self.find_locations_data(name):
                        cursor.execute('update locations set number=%s where name=%s',[number,name])
                else:
                        cursor.execute('insert into locations (name,number) values (%s,%s)',[name,number])
                conn.commit()
                cursor.close()
                conn.close()

        ##��ȡlocations������
        ##���أ�������������
        def read_locations_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from locations')
                values=cursor.fetchall()                    
                cursor.close()
                conn.close()
                return values
                        
##############################################################################################################################
 
        ##����ָ��id���Ƿ��ڱ���
        ##������myid:id��
        ##����ֵ������:True
        ##        ����False
        def find_users_data(self,myid):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()                        
                cursor.execute('select * from users where id= %s',(myid,))
                values=cursor.fetchall()
                if len(values)>0:
                        n=True;
                else:
                        n=False;
                cursor.close()
                conn.close()
                return n
        
        ##����users������
        def update_users_data(self,myid,name,address):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                if self.find_users_data(myid):
                        cursor.execute('update users set name=%s,address=%s where id=%s',[name,address,myid])
                else:
                        cursor.execute('insert into users (id,name,address) values (%s,%s,%s)',[myid,name,address])
                conn.commit()
                cursor.close()
                conn.close()

        ##��ȡusers������
        ##���أ�������������
        def read_users_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from users')
                values=cursor.fetchall()
                cursor.close()
                conn.close()
                return values
