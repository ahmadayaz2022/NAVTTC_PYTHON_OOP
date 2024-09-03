class vehicle:
    def __init__(self):
        self.size=55
        self.color='red'
        self.tyre=4
    # size=33
    # color='red'
    # tyre=33

    def Buying_selling(self):
        print("we have available a CAR having size:  ",self.size)
        print("we have available a CAR having color:  ", self.color)
        print("we have available a CAR having tyre:  ", self.tyre)

object_vehicle=vehicle()

object_vehicle.Buying_selling()