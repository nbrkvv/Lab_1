import json 

filenamejson = "data.json"

#-----------------------------------------------

class JsonHandler:

    def save_to_json(data) -> None:
        with open(filenamejson, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            print("Данные успешно сохранены")
        pass

    def load_from_json() -> dict:
        try:
            with open(filenamejson, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"movies": [], "tvseries": []}

    def print_data(data):
        print("\nДанные из JSON:")
    
        print("\nФильмы:")
        for movie in data['movies']:
            print(f"Название: {movie['title']}, Длительность: {movie['duration']} мин, Рейтинг: {movie['rating']}")

        print("\nСериалы:")
        for series in data['serials']:
            print(f"Название: {series['title']}, Эпизодов: {series['num_of_ep']}, Рейтинг: {series['rating']}")

    def data_to_dict(data) -> dict:

        while True:
            choice = int(input("Что записать в массив?\n1-Фильмы\n2-Сериалы\n"))
            if choice == 1:
                res = []
                for movie in data['movies']:
                    res.append(movie)
                print("Данные успешно сохранены в массив \n")
                return res
            elif choice == 2:
                res = []
                for movie in data['serials']:
                    res.append(movie)
                print("Данные успешно сохранены в массив \n")
                return res
            else:
                print("Неверный выбор")


#-----------------------------------------------

class Serial:
    title = ""
    num_of_ep = 0
    rating = 0

    def __init__(self, inp_title = "", inp_num_of_ep = 0, inp_rating = 0) -> None:
        self.title = inp_title
        self.num_of_ep = inp_num_of_ep
        self.rating = inp_rating
        pass

    def set_title(self) -> None:
        self.title = input("Введите название сериала: ")
        pass
  
    def set_rating(self) -> None:
        while True:
            try:
                rating = float(input("Введите рейтинг фильма: "))
                if rating < 0 or rating > 5:
                    print("Рейтинг фильма может быть только от 0 до 5")
                else:
                    self.rating = rating
                    break
            except ValueError:
                print("Рейтинг фильма может быть только вещественным числом")
        pass

    def set_num_of_ep(self) -> None:
        while True:
            try:
                eps = int(input("Введите количество серий в сериале: "))
                if eps <= 0:
                    print("Количество серий должно быть положительным")
                else:
                    self.num_of_ep = eps
                    break
            except ValueError:
                print("Количество серий может быть только целым числом")
        pass

    def get_title(self) -> str:
        return self.title

    def get_num_of_ep(self) -> int:
        return self.num_of_ep
    
    def get_rating(self) -> float:
        return self.rating

    def to_dict(self) -> dict:
            return {
            "title": self.title,
            "num_of_ep": self.num_of_ep,
            "rating": self.rating
        }

    def __str__(self) -> str:
        return f"Сериал: {self.title}, количество эпизодов: {self.num_of_ep}, рейтинг: {self.rating}"

#-----------------------------------------------

class Film:
    title = ""
    duration = 0
    rating = 0

    def __init__(self, inp_title = "", inp_duratoin = 0, inp_rating = 0) -> None:
        self.title = inp_title
        self.duration = inp_duratoin
        self.rating = inp_rating
        pass

    def set_title(self) -> None:
        self.title = input("Введите название фильма: ")
        pass

    def set_duration(self) -> None:
        while True:
            try:
                duration = int(input("Введите хронометраж фильма в минутах: "))
                if duration <= 0:
                    print("Хронометраж должно быть быть положительным")
                else:
                    self.duration = duration
                    break
            except ValueError:
                print("Хронометраж фильма может быть только целым числом")
        pass

    def set_rating(self) -> None:

        while True:
            try:
                rating = float(input("Введите рейтинг фильма: "))
                if rating < 0 or rating > 5:
                    print("Рейтинг фильма может быть только от 0 до 5")
                else:
                    self.rating = rating
                    break
            except ValueError:
                print("Рейтинг фильма может быть только вещественным числом")
        pass

    def get_title(self) -> str:
        return self.title

    def get_duration(self) -> int:
        return self.duration
    
    def get_rating(self) -> float:
        return self.rating
    
    def to_dict(self) -> dict:
            return {
            "title": self.title,
            "duration": self.duration,
            "rating": self.rating
        }

    def __str__(self) -> str:
        return f"Фильм: {self.title}, хронометраж: {self.duration}, рейтинг: {self.rating}"

