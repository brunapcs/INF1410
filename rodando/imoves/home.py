#!/bin/python3

class Home:
    def __init__(self, latitude, longitude, _type,
     vagas, description, nome_dono, cpf_dono, telefone, cep, rua, tipo, numero ,apt=0):
        self.lat = latitude
        self.lng = longitude
        self._type = _type
        self.vagas = vagas
        self.description = description
        self.nome_dono = nome_dono
        self.cpf_dono = cpf_dono
        self.telefone = telefone
        self.cep = cep
        self.apt = apt
        self.rua = rua
        self.tipo = tipo
        self.numero = numero
    

    def update_vagas(self):
        self.vagas -= 1
        return self.vagas

    def get_atts(self):
        full_description = "<b>" + self.description + "</b><p></p>" + "Tipo: " + self._type + "<p></p>" + "Vagas: " + str(self.vagas) + "<p></p>"
        lst = [self.lat, self.lng, full_description]
        return lst
