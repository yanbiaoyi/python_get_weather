#coding:utf-8
import pymysql

def insertTable(datas):
	
	#创建数据库连接
	connection = pymysql.connect("localhost", "root", "rootroot", "test")

	#创建 cursor游标
	cursor = connection.cursor()

	#建设sql语句
	sql="insert into  weather(w_id, w_date, w_detail, w_temperature_low, w_temperature_high) value(null, %s,%s,%s,%s)"
	cursor.executemany(sql,datas)
	connection.commit()
	print('sql was insert success')	

	"""
	except Exception as e:
		print('insert error')
		connection.rollback()
	"""
	cursor.close()
	connection.close()
"""
if __name__=='__main__':
	#data=[2,2,2,2]
	insertTable()	
"""
