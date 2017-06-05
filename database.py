# -*- coding: cp936 -*-
import mysql.connector
class Database(object):
##############################################################################################################################

        ##查找指定语言是否在表中
        ##参数：name:语言
        ##返回值：存在:True
        ##        否则：False
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
        
        ##更新languages表内容
        ##参数：name:语言
        ##      number:对应语言的项目数量
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

        ##读取languages表数据
        ##返回：表中所有数据
        def read_languages_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from languages')
                values=cursor.fetchall()                
                cursor.close()
                conn.close()
                return values

 
##############################################################################################################################

        ##查找指定年份是否在表中
        ##参数：year:年份
        ##返回值：存在:True
        ##        否则：False
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
        
        ##更新repositories表内容
        ##参数：year:年份
        ##      number:对应年份的仓库数量
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

        ##读取repositories表数据
        ##返回：表中所有数据
        def read_repositories_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from repositories')
                values=cursor.fetchall()
                cursor.close()
                conn.close()
                return values

                        
##############################################################################################################################

        ##查找指定id号是否在表中
        ##参数：myid:id号
        ##返回值：存在:True
        ##        否则：False
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
                        
        ##更新projects表内容
        ##参数：myid:id号
        ##      name:项目名称
        ##      address:项目网址
        def update_projects_data(self,myid,repo_name,repo_url,stargazers_count,user_login,user_url):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                if self.find_projects_data(myid):
                        cursor.execute('update projects set id=%s,repo_name=%s,repo_url=%s,stargazers_count=%s,user_login=%s,user_url=%s where id=%s',[myid,repo_name,repo_url,stargazers_count,user_login,user_url,myid])
                else:
                        cursor.execute('insert into projects (id,repo_name,repo_url,stargazers_count,user_login,user_url) values (%s,%s,%s,%s,%s,%s)',[myid,repo_name,repo_url,stargazers_count,user_login,user_url])
                conn.commit()
                cursor.close()
                conn.close()

        ##读取projects表数据
        ##返回：表中所有数据
        def read_projects_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from projects')
                values=cursor.fetchall()
                cursor.close()
                conn.close()
                return values
                        
##############################################################################################################################
 
        ##查找指定国家是否在表中
        ##参数：name:国家名称
        ##返回值：存在:True
        ##        否则：False
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
        
        ##更新locations表内容
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

        ##读取locations表数据
        ##返回：表中所有数据
        def read_locations_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from locations')
                values=cursor.fetchall()                    
                cursor.close()
                conn.close()
                return values
                        
##############################################################################################################################
 
        ##查找指定id号是否在表中
        ##参数：myid:id号
        ##返回值：存在:True
        ##        否则：False
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
        
        ##更新users表内容
        ##参数：myid:id号
        ##      user_name:用户名
        ##      user_url:用户github地址
        ##      follower:关注度
        ##      address:用户所在地
        ##      repo_name:该用户代表项目名
        ##      repo_url:项目地址
        def update_users_data(self,myid,user_name,user_url,follower,address,repo_name,repo_url):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                if self.find_users_data(myid):
                        cursor.execute('update users set user_name=%s,user_url=%s,follower=%s,address=%s,repo_name=%s,repo_url=%s where id=%s',[user_name,user_url,follower,address,repo_name,repo_url,myid])
                else:
                        cursor.execute('insert into users (id,user_name,user_url,follower,address,repo_name,repo_url) values (%s,%s,%s,%s,%s,%s,%s)',[myid,user_name,user_url,follower,address,repo_name,repo_url])
                conn.commit()
                cursor.close()
                conn.close()

        ##读取users表数据
        ##返回：表中所有数据
        def read_users_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from users')
                values=cursor.fetchall()
                cursor.close()
                conn.close()
                return values

##############################################################################################################################

        ##查找总数量是否在表中
        ##参数：name:total_count
        ##返回值：存在:True
        ##        否则：False
        def find_total_data(self,name):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()                    
                cursor.execute('select * from total where name= %s',(name,))
                values=cursor.fetchall()
                if len(values)>0:
                        n=True;
                else:
                        n=False;
                cursor.close()
                conn.close()
                return n
        
        ##更新total表内容
        ##参数：name:total_count
        ##      number:对应语言的项目数量
        def update_total_data(self,name,number):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                if self.find_total_data(name):
                        cursor.execute('update total set number=%s where name=%s',[number,name])
                else:
                        cursor.execute('insert into total (name,number) values (%s,%s)',[name,number])
                conn.commit()
                cursor.close()
                conn.close()

        ##读取total表数据
        ##返回：表中所有数据
        def read_total_data(self):
                conn=mysql.connector.connect(user='root',password='eavG53JrMC',database='github_database',use_unicode=True)
                cursor=conn.cursor()
                cursor.execute('select * from total')
                values=cursor.fetchall()                
                cursor.close()
                conn.close()
                return values

