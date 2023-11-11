data_dict = {"Gender": None,
             "Class": None,
             "PhoneNumber": None,
             "FavoriteSubjects": [],
             "Rests": [],
             "Sections": [],
             "City": None}

subjects_7 = {
    "Алгебра/геометрия": ["Алгоритмика"],
    "Иностранный язык": ["Lexika", "Софтиум", "Классика", "smart", "Юник club",
                         "Academy School", "Полиглот", "Grinwich"],

    "Информатика": ["Софтиум", "Наследники ползунова", "Алгоритмика",
                    "Кодология", "Курсы в политехе"],
    "Физика": ["Наследники ползунова"],

    "Физ-ра": ["Спарта", "Cпортивная/художественная гимнастика в заре", "Плавание в заре", "Бригантина (бокс)",
               "Грани (скалолазание)", "Atmosfera (фитнес студия)", "Барс(водное поло)", "Гренада (кикбоксинг)",
               "Баба йога (хатха-йога)", "Эфа(бой)", "Чемпион (бокс)", "Индиго (танцы)", "Шаг вперед (танцы)",
               "Овация (танцы)"],
    "История": [],
    "Литература": [],
    "Обществознание": [],
    "Русский язык": [],
    "Биология": [],
    "География": []
}

rest = ["Спорт (активный отдых)",
        "Чтение книг (комиксов)",
        "Творчество (лепка, \nрисование, бисер и т.д.)",
        "Компьютерные игры",
        "Просмотр чего-либо (YouTube, \nфильмы, мультфильмы и т.д.)",
        "Лежание на диване"]

classes = {1: None,
           2: None,
           3: None,
           4: None,
           5: None,
           6: None,
           7: subjects_7,
           8: None,
           9: None,
           10: None,
           11: None}

city_dict = {"Бийск": classes}