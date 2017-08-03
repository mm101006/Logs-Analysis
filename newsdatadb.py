#!/usr/bin/python
# -*- coding: latin-1 -*-
import psycopg2

DBNAME = "news"

conn = psycopg2.connect(database=DBNAME)
cur = conn.cursor()


def Question_1():
    query = """select title, count(*) from articles
               join log on articles.slug = replace(path, '/article/', '')
               where status = '200 OK' and path != '/'
               group by title order by count desc limit 3;"""
    cur.execute(query)
    rows = cur.fetchall()
    print "What are the most popular three articles of all time?"
    for each in rows:
        print '"%s" — %s views' % (each[0], each[1])


def Question_2():
    query = """select name, count(*) from articles
               join authors on articles.author = authors.id
               join log on articles.slug = replace(path, '/article/', '')
               where status = '200 OK' and path != '/'
               group by name order by count desc;"""
    cur.execute(query)
    rows = cur.fetchall()
    print "Who are the most popular article authors of all time?"
    for each in rows:
        print '%s — %s views' % (each[0], each[1])


def Question_3():
    query = """select to_char(sum_404.date, 'Mon dd, yyyy'),
               (sum_404.NOT_FOUND / sum_status.total) * 100 as percent
               from sum_404 join sum_status
               on sum_404.date = sum_status.date;"""
    cur.execute(query)
    rows = cur.fetchall()
    print "On which days did more than 1% of requests lead to errors?"
    for each in rows:
        if each[1] > 1.0:
            print "{} — {}% errors".format(each[0], '%04.2f' % each[1])

if __name__ == "__main__":
	Question_1()
	Question_2()
	Question_3()
