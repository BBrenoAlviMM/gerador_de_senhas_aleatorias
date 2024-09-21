import PySimpleGUI as sg
from random import choice

with open("nothing_here.txt", "a+") as arquivo:
    arquivo.read()

password = ''
generate_layout = [
    [sg.Push(), sg.Text("Gerador de senhas Fortes!"), sg.Push()],
    [sg.Text("Aonde a senha será usada?"), sg.In(key="local")],
    [sg.Push(), sg.Btn("Gerar"), sg.Combo(["8", "10", "12", "14", "16", "18",
     "20", "30", "40", "50"], key="passLenght"), sg.In("", key="passPlace")],
    [sg.Push(), sg.Text("", key="caution"), sg.Push()],
    [sg.Btn("Salvar"), sg.Push(), sg.Btn("Senhas Salvas"), sg.Push(),
     sg.Btn("Sair")]
]

local = ''
password = ''
password_content = ''
wind2 = False
generator_window = sg.Window("Gerador de senhas", layout=generate_layout)

while True:
    ev, vls = generator_window.read()
    if ev == "Sair" or ev == sg.WIN_CLOSED:
        generator_window.close()
        break
    if ev == "Gerar":
        lenght = vls['passLenght']
        if lenght == "" or lenght == "0":
            generator_window['caution'].update("A quantidade de caracteres"
                                              " não pode ser vazía ou 0!")
        elif int(lenght) > 200:
            generator_window['caution'].update("O limite de caracteres"
                                              " é de 200!")
        else:
            generator_window['caution'].update('')
            for x in range(int(lenght)):
                char = choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
                               'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                               't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@',
                               '#', '$', '%', '&', '-', '1', '2', '3', '4',
                               '5', '6', '7', '8', '9', '0'])
                password += char
            generator_window['passPlace'].Update(password)
            password = ''
    if ev == "Salvar":
        local = vls['local']
        password_content = vls['passPlace']
        if local != '' and password_content != '':
            with open("nothing_here.txt", "a") as arquivo:
                arquivo.write(f"\n{local}|{password_content}|")
            generator_window['caution'].update("Senha Salva Com Sucesso")
            password_content = ''
        else:
            generator_window['caution'].update("Local onde será usado ou senha "
                                              "em branco!")
    if ev == "Senhas Salvas" and not wind2:
        generator_window.hide()
        wind2 = True
        layoutPerfis = [
            [sg.Push(), sg.Text("Perfis"), sg.Push()]
        ]
        listPass = []
        nmbr = 0
        win2 = False
        with open("nothing_here.txt", "r") as arquivo:
            for content in arquivo:
                ps = content.split("|")
                if len(ps) > 1:
                    nmbr += 1
                    layoutPerfis += [[sg.Push(), sg.Btn(ps[0], key=nmbr), sg.Push()]]
                    listPass += [ps[1]]
                else:
                    continue
            layoutPerfis += [
                [sg.Push(),sg.Txt(60*"-"), sg.Push()],
                [sg.Push(), sg.Btn("Voltar")]]
        windowPerfis = sg.Window("Perfis e Senhas", layout=layoutPerfis)
        while True:
            ev1, vls1 = windowPerfis.read()
            if ev1 == sg.WIN_CLOSED or ev1 == "Voltar":
                generator_window.UnHide()
                windowPerfis.close()
                wind2 = False
                break
            if ev1 != sg.WIN_CLOSED or ev1 != "Voltar" and win2 is False:
                win2 = True
                layoutSenhas = [[sg.Push(), sg.In(listPass[int(ev1) - 1]),
                                 sg.Push()],
                                [sg.Push(), sg.Btn("Voltar"), sg.Push()]]
                windowSenhas = sg.Window("Senha", layout=layoutSenhas)
                while True:
                    ev2, vls2 = windowSenhas.read()
                    if ev2 == sg.WIN_CLOSED or ev2 == "Voltar":
                        windowSenhas.close()
                        win2 = False
                        break
