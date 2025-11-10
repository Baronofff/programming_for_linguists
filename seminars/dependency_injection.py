
class Service:
    def get_data(self):
        return "data"


# class Controller:
#     def __init__(self):
#         self.service = Service()    # здесь создается зависимость
#
#     def handle(self):
#         return self.service.get_data()

class Controller:
    def __init__(self, service):
        self.service = service

    def handle(self):
        return self.service.get_data()


if __name__ == "__main__":
    service_obj = Service()
    controller = Controller(service_obj)


