# 10.9
class Bear:
    def eats(self):
        return "berries"


class Rabbit:
    def eats(self):
        return "clover"


class Octothorpe:
    def eats(self):
        return "campers"


b = Bear()
r = Rabbit()
o = Octothorpe()

print(f"{b.eats()},  {r.eats()},  {o.eats()}")



