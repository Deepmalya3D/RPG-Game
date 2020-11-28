from random import randint
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class person:
    def __init__(self,name,hp,mp,att,defe,magic,items,coins):
        self.name=name
        self.maxhp=hp
        self.hp=hp
        self.maxmp=mp
        self.mp=mp
        self.attl=att-10
        self.atth=att+10
        self.defe=defe
        self.magic=magic
        self.choice=['attack','magic','items']
        self.items=items
        self.coins=coins
    def attack(self):
        return randint(self.attl,self.atth)
    def use_magic(self,i):
        mgl=self.magic[i]['dmg']-5
        mgh=self.magic[i]['dmg']+5
        return randint(mgl,mgh)
    def get_maxhp(self):
        return self.maxhp
    def get_hp(self):
        return self.hp
    def get_maxmp(self):
        return self.maxmp
    def get_mp(self):
        return self.mp
    def magics_list(self):
        return self.magic
    def reduce_hp(self,dmg):
        self.hp-=dmg
        if self.hp<=0:
            self.hp=0
        return self.hp
    def reduce_mp(self,i):
        self.mp-=self.magic[i]['cost']
    def show_magic(self,i):
        return self.magic[i]['name']
    def choose(self):
        for i in range(len(self.choice)):
            print( f"    {i+1}: {self.choice[i]}")
    def choose_magic(self):
        for j in range(len(self.magic)):
            print(f"{j+1}: {self.magic[j]['name']}(cost: {self.magic[j]['cost']})")
    def choose_items(self):
        for k in range(len(self.items)):
            print(f"{k+1}: {self.items[k]['item']} ( {self.items[k]['description']} (quantity: x{self.items[k]['quantity']})")