from OOP6 import my_kitchenAppliance


class Device:
    pass
class poratabledevice(Device):
    pass
class wiredclass(Device):
    pass
class smartphone(poratabledevice):
    pass
class desktopcomputer(wiredclass):
    pass

my_device=Device()
my_portabledevice=poratabledevice()
my_wiredclass=wiredclass()
my_smart=smartphone()
my_desktop=desktopcomputer()

for cls1 in [my_device,my_portabledevice,my_wiredclass,my_smart,my_desktop]:
    for cls2 in [Device,poratabledevice,wiredclass,smartphone,desktopcomputer]:
        print(isinstance(cls1,cls2),end='\t')
    print()