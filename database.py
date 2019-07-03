#!/bin/python3
import sqlite3
from home import Home
from flask_sqlalchemy import SQLAlchemy
import math
from geopy import distance

class DataBase:
    def __init__(self):
        self.home_lst = []

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

        for row in rows:
            print(row)
            h = Home(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
            self.home_lst.append(h)

        return self.home_lst


    def filtra_valor(self, val):
        rem = []

        for i in range(len(self.home_lst) ):
            if(self.home_lst[i].valor > float(val)):
                rem.append(self.home_lst[i])

        for i in range(len(rem)):
            self.home_lst.remove(rem[i])


    def calcula_distancia(self, long_x, lat_y):
        puc = ( -22.978993, -43.232999)
        place = (lat_y, long_x)
        return float(distance.vincenty(puc, place).km)

    def calcula_distancia2(self, long_x, lat_y, x , y ):
        place = (lat_y, long_x)
        trab = (y , x )
        return float(distance.vincenty(place, trab).km)

    def filtra_distancia(self, dist):
        dist = float(dist)
        rem = []

        for i in range(len(self.home_lst)):
            distancia = self.calcula_distancia(self.home_lst[i].lng, self.home_lst[i].lat)
            if distancia > dist:
                rem.append(self.home_lst[i])

        for i in range(len(rem)):
            self.home_lst.remove(rem[i])


    def filtra_distancia_trab(self,  lat, lng ):
        rem = []

        for i in range(len(self.home_lst)):
            distancia = self.calcula_distancia2(self.home_lst[i].lng, self.home_lst[i].lat, lng, lat)
            if distancia > 15:
                rem.append(self.home_lst[i])

        for i in range(len(rem)):
            self.home_lst.remove(rem[i])

    def filtra_tipo(self, tipo):
        rem = []

        for i in range(len(tipo)):
            for j in range(len(self.home_lst)):
                if self.home_lst[j]._type[i] == tipo:
                    if self.home_lst[i]._type[i] in rem:
                        rem.remove(self.home_lst[i])
                else:
                    rem.append(self.home_lst[i])

        for i in range(len(rem)):
            if rem[i] in self.home_lst:
              self.home_lst.remove(rem[i])



    def get_filtered_home_list(self, val, dist, tipo):
        self.home_lst = self.get_homes_list()
        self.filtra_valor(val)
        self.filtra_distancia(float(dist))
        self.filtra_tipo(tipo)

        return self.home_lst

    def get_rec_homes_list(self, lat,lng, genero, din):
        self.home_lst = self.get_homes_list()
        self.filtra_valor(float(din)*0.6)
        self.filtra_distancia_trab(float(lat), float(lng))
        ##self.filtra_genero(genero)

        return self.home_lst



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
