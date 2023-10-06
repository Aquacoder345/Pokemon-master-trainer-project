class Pokemon:
  def __init__(self, name, level, current_health, max_health, pokemon_type, is_knocked_out=False, speed=0, attack=0, defence=0, experience = 0, evolution_level = None):
    self.name = name
    self.level = level
    self.current_health = current_health
    self.max_health = max_health
    self.pokemon_type = pokemon_type
    self.is_knocked_out = is_knocked_out
    self.experience = experience
    self.evolution_level = evolution_level
    self.speed = speed
    self.attack = attack
    self.defence = defence

  def __repr__(self):
    return 'This level {level} {name} has {health} HP remaining. They are a {type} type pokemon'.format(level = self.level, name = self.name, health = self.current_health, type = self.pokemon_type)

  def lose_health(self, decrease):
    hp_lost = min(decrease, self.current_health)
    self.current_health -= hp_lost
    print("{} lost {} health.".format(self.name, hp_lost))
    if self.current_health <= 0:
      self.is_knocked_out = True
      print("{} is knocked out.".format(self.name))
    return hp_lost

  def gain_health(self, increase):
    hp = self.current_health
    self.current_health = min(self.current_health + increase, self.max_health)
    new_hp = self.current_health - hp
    if self.current_health > self.max_health:
      self.current_health = self.max_health
    new_hp = self.current_health - hp
    print('{} health was restored'.format(new_hp))
    return self.current_health

  def knocked_out(self):
    if self.is_knocked_out < 0 and self.is_knocked_out == False:
      self.is_knocked_out = True
    return self.is_knocked_out

  def total_health(self):
    return '{name}now has {current}/{max} health'.format(name = self.name, current = self.current_health, max = self.max_health)
      
  def perform_attack(self, target):
    hp = 0
    if self.is_knocked_out:
      print("{name} can't attack because it is knocked out!".format(name=self.name))
      return 0
    elif (self.pokemon_type == 'Fire' and target.pokemon_type == 'Water') or \
     (self.pokemon_type == 'Water' and target.pokemon_type == "Electric"):
      print("Half-Damage dealt.\n{attacker} {victim} for {damage}".format(attacker=self.name, victim=target.name, damage=round(self.level * 0.5)))
      damage_done = self.level * 0.5
    elif (self.pokemon_type == "Fire" and target.pokemon_type == "Ice") or \
    (self.pokemon_type == "Electric" and target.pokemon_type == "Water"):
      print("Double-Damage dealt.\n{attacker} attacked {victim} for {damage} damage".format(attacker=self.name, victim=target.name, damage=self.level * 2))
      damage_done = self.level * 2.0
    else:
      print("{attacker} attacked {victim} for {damage} damage".format(attacker=self.name, victim=target.name, damage=self.level))
      damage_done = self.level
    experience_gained = int(damage_done / 2)
    self.experience += experience_gained
    print("{} gained {} experience".format(self.name, experience_gained))
    if self.evolution_level and self.level >= self.evolution_level:
      print("{} is Evolving!".format(self.name))
    return target.lose_health(damage_done)
   
class Trainer:
  def __init__(self, pokemons, potions, name, current_pokemon):
    self.pokemons = pokemons
    self.potions = potions
    self.name = name
    self.current_pokemon = current_pokemon

  def use_potion(self):
    print ("{trainer} uses potion on {target}".format(trainer = self.name, target = self.current_pokemon.name))
    return self.current_pokemon.gain_health(10)
  
  def attack(self, target):
    print('{attacker} attacks {target}'.format(attacker = self.current_pokemon.name, target = target.current_pokemon.name))
    return target.current_pokemon.lose_health(10)
  
  def is_active(self):
    if self.current_pokemon.is_knocked_out:
      print("Can't switch to a knocked out Pokemon.")
      return False
    print('{} is the active Pokemon.'.format(self.current_pokemon.name))
    return True


class Charmander(Pokemon):
  def __init__(self, name, level, current_health, max_health, is_knocked_out=False, experience = 0, evolution_level=None, special_attack_name = 'Ember', speed=0, attack=0, defence=0):
    super().__init__(name, level, current_health, max_health, 'fire', is_knocked_out, experience, evolution_level)
    self.special_attack_name = special_attack_name
  def special_attack(self, target):
    print("{} uses {} on {}!".format(self.name, self.special_attack_name, target.name))

venesaur = Pokemon('Venesaur', 1, 100, 100, 'grass', False, speed=5, attack=10, defence=15)
charmander = Charmander('Charmander', 5, 100, 100, False, evolution_level=16, special_attack_name='Ember', speed=15, attack=20, defence=15)
charizard = Pokemon('Charizard', 1, 100, 100, 'fire', False, speed=15, attack=20, defence=20)
slowbro = Pokemon('Slowbro', 1, 0, 100, 'water', True, speed=2, attack=8, defence=20)
squirtle = Pokemon("Squritle", 5, 100, 100, 'water', False, evolution_level=10, speed=9, attack=14, defence=18)
pikachu = Pokemon('Pikachu', 5, 100, 100, 'electric', False, speed=25, attack=30, defence=25)
ash = Trainer([pikachu, charizard], 5, 'Ash', charmander)
lisa = Trainer([venesaur, slowbro], 3, 'Lisa', venesaur)


#squirtle.perform_attack(charmander)
#charmander.special_attack(squirtle)
#ash.use_potion()
lisa.attack(ash)
ash.use_potion()
ash.attack(lisa)
