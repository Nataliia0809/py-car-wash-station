class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        if 1 <= comfort_class <= 7:
            self.comfort_class = comfort_class
        else:
            raise ValueError("Error. comfort_class must be between 1 and 7.")

        if 1 <= clean_mark <= 10:
            self.clean_mark = clean_mark
        else:
            raise ValueError("Error. clean_mark must be between 1 and 10.")

        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_pover, average_rating, count_of_ratings):
        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        else:
            raise ValueError("Error. distance_from_city_center must be between 1.0 and 10.0.")

        if 1 <= clean_pover <= 10:
            self.clean_pover = clean_pover
        else:
            raise ValueError("Error. clean_pover must be between 1 and 10.")

        if 1.0 <= average_rating <= 5.0:
            self.average_rating = round(average_rating, 1)
        else:
            raise ValueError("Error. average_rating must be between 1.0 and 5.0.")

        if isinstance(count_of_ratings, int) and count_of_ratings >= 0:
            self.count_of_ratings = count_of_ratings
        else:
            raise ValueError("Error. count_of_ratings must be a non-negative integer.")

    def serve_car(self, cars):
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_pover:  # Якщо машина потребує миття
                wash_cost = self.calculate_washing_price(car)  # Обчислити вартість миття
                income += wash_cost  # Додати вартість до доходу
                self.wash_single_car(car)  # Оновити clean_mark машини
        return round(income, 1)  # Повернення доходу
    def calculate_washing_price(self, car):
        return (car.comfort_class * (self.clean_pover - car.clean_mark) *
                self.average_rating / self.distance_from_city_center)

    def wash_single_car(self, car):
        if self.clean_pover > car.clean_mark:
            car.clean_mark = self.clean_pover

    def rate_service(self, new_rating):
        if 1.0 <= new_rating <= 5.0:
            total_rating = self.average_rating * self.count_of_ratings
            total_rating += new_rating
            self.count_of_ratings += 1
            self.average_rating = round(total_rating / self.count_of_ratings, 1)
        else:
            raise ValueError("Error. Rating must be between 1.0 and 5.0.")







