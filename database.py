#!/bin/python3
import sqlite3
from home import Home


def get_homes_list():
    try:
        conn = sqlite3.connect("data.db")
    except:
        print("Exception hit")
    
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT lat, long, tipo, vagas, descricao, nome_dono, cpf_dono, telefone_dono, cep, rua, tipo, numero, apt        
        from Home
        """
    )

    rows = cursor.fetchall()

    home_lst = []
    for row in rows:
        print(row)
        h = Home(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        home_lst.append(h)
    
    return home_lst


def insert_data(home):
    try:
            conn = sqlite3.connect("data.db")
    except:
        print("Exception hit")
        
    cursor = conn.cursor()
    cursor.execute(
            """
            INSERT INTO Home (vagas, telefone_dono, cpf_dono, nome_dono, 
            cep, numero, apt, rua, lat, long, tipo, descricao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (home.vagas, home.telefone, home.cpf_dono, home.nome_dono,
             home.cep, home.numero, home.apt, home.rua, home.lat, home.lng,
             home.tipo, home.description)
             )

    conn.commit()
