from CitySections import Barnaul, Biysk, Rubzovsk, Zarinsk, \
    Novoaltaysk, Aleysk, Kamen_na_Oby, Slavgorod, Zmeinogorsk, \
    Belokuriha, Gornyak, Yarovoe


data_dict = {"Gender": None,
             "Class": None,
             "PhoneNumber": None,
             "FavoriteSubjects": [],
             "Rests": [],
             "Sections": [],
             "City": None}


rest = ["Спорт (активный отдых)",
        "Чтение книг (комиксов)",
        "Творчество (лепка, \nрисование, бисер и т.д.)",
        "Компьютерные игры",
        "Просмотр чего-либо (YouTube, \nфильмы, мультфильмы и т.д.)",
        "Лежание на диване"]


city_dict = {"Алейск": Aleysk.classes,
            "Барнаул": Barnaul.classes,
             "Белокуриха": Belokuriha.classes,
             "Бийск": Biysk.classes,
             "Горняк": Gornyak.classes,
             "Камень-на-оби": Kamen_na_Oby.classes,
             "Новоалтайск": Novoaltaysk.classes,
             "Рубцовск": Rubzovsk.classes,
             "Славгород": Slavgorod.classes,
             "Яровое": Yarovoe.classes,
             "Заринск": Zarinsk.classes,
             "Змейногорск": Zmeinogorsk.classes}