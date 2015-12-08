#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
from gi.repository import Notify

from urllib2 import Request, urlopen

import sqlite3
import pwd
import os


class Url(object):

    conn = None

    def connect_db(self):

        user = pwd.getpwuid( os.getuid() )[0], pwd.getpwuid( os.getuid() )[5]

        dir_db = '%s/.promo' % user[1]

        if not os.path.isdir(dir_db):
            os.mkdir(dir_db)

        self.conn = sqlite3.connect('%s/.promo/sqllite.db' % user[1])

    def close_db(self):

        self.conn.close()

    def population_db(self, table):

        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS %s (
                id INTEGER PRIMARY KEY ASC,
                title VARCHAR(255),
                link VARCHAR(255)
            );
        """ % table)

        # cursor.execute("""
        #     SELECT * FROM %s ORDER BY id;
        # """ % table)
        #
        # for linha in cursor.fetchall():
        #     print linha

    def get_db_item(self, table, title):

        cursor = self.conn.cursor()

        cursor.execute("""
            SELECT * FROM %s WHERE title = ?;
        """ % table, (title, ))

        result = cursor.fetchall()

        return len(result) > 0

    def insert_db(self, table, values):

        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO %s (
                title,
                link
            )
            VALUES (?, ?);
        """ % table, values)

        self.conn.commit()

    def start(self):

        url = 'http://www.hardmob.com.br/promocoes/'

        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

        # conectou
        self.connect_db()

        # populou
        self.population_db('hardmob')

        req = Request(url, headers=hdr)

        page = urlopen(req).read()

        soup = BeautifulSoup(page, 'html.parser')
        soup.prettify()

        # initialisation de libnotify avec le nom de notre application
        Notify.init(u'Promoções Hardmob')

        for s in soup.find_all("a", class_="title"):
            # inseriu
            if not self.get_db_item('hardmob', s.string):
                self.insert_db('hardmob', (s.string, s['href']))
                notif = Notify.Notification.new(
                    '%s' % s.string,
                    '%s' % s['href'],
                    'dialog-information'
                )
                notif.show()

url = Url()
# iniciar busca
url.start()