#!/bin/python3
import sqlite3
from home import Home
from flask_sqlalchemy import SQLAlchemy
import math

class DataBase:

    def connect_database(self):
        try:
            self.conn = sqlite3.connect("data.db")
        except:
            print("Exception hit")

        self.cursor = self.conn.cursor()

    def get_homes_list(self):
        self.connect_database()
        self.cursor.execute(
            """
            SELECT lat, long, tipo, vagas, descricao, nome_dono, cpf_dono, telefone_dono, cep, rua, tipo, numero, apt, valor       
            from Home
            """
        )
        rows = self.cursor.fetchall()

        self.home_lst = []
        for row in rows:
            print(row)
            h = Home(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
            self.home_lst.append(h)

        return self.home_lst


    def filtra_valor(self, val):
        val = str(val)
        rem = []

        for i in range(len(self.home_lst) ):
            if(self.home_lst[i].valor > float(val)):
                rem.append(self.home_lst[i])

        for i in range(len(rem)):
            self.home_lst.remove(rem[i])

        return self.home_lst


    def calcula_distancia(self, long_x, lat_y):
        puc_x = -22.978993
        puc_y = -43.232999

        return math.sqrt(math.pow((long_x - puc_x), 2) + math.pow((lat_y - puc_y), 2) )

    def filtra_distancia(self, dist):
        dist = float(dist)
        rem = []

        for i in range(len(self.home_lst)-1):
            if self.calcula_distancia(self.home_lst[i].lng, self.home_lst[i].lat) > dist:
                rem.append(self.home_lst[i])

        for i in range(len(rem)):
            self.home_lst.remove(rem[i])

        return self.home_lst


    def get_filtered_home_list(self, val, dist):
        self.connect_database()
        home_lst = self.get_homes_list()

        if( float(val) > 0.0 ):
            self.home_lst = self.filtra_valor(val)

        if(float(dist) > 0):
            self.filtra_distancia(dist)

        return home_lst



    def insert_data(self, home):
        self.connect_database()
        self.cursor.execute(
                """
                INSERT INTO Home (vagas, telefone_dono, cpf_dono, nome_dono, 
                cep, numero, apt, rua, lat, long, tipo, descricao, valor)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """, (home.vagas, home.telefone, home.cpf_dono, home.nome_dono,
                 home.cep, home.numero, home.apt, home.rua, home.lat, home.lng,
                 home.tipo, home.description, home.valor)
                 )
        self.conn.commit()
