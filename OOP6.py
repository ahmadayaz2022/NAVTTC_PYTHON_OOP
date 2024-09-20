class Appliance:
    pass
class kitchenAppliance(Appliance):
    pass
class cleaningAppliance(Appliance):
    pass
class microwave(kitchenAppliance):
    pass
class vacume(cleaningAppliance):
    pass


my_Appliance = Appliance()
my_kitchenAppliance = kitchenAppliance()
my_cleaningAppliance = cleaningAppliance()
my_microwave= microwave()
myvacume=vacume()

for cls1 in [Appliance, kitchenAppliance, cleaningAppliance,microwave,vacume]:
    for cls2 in [Appliance, kitchenAppliance, cleaningAppliance,microwave,vacume]:
        print(issubclass(cls1, cls2), end="\t")
    print()
