from nbtlib import load
from mojang import API
import json

class UserStats:
    def __init__(self, uuid):
        player_data = f'playerdata/{uuid}.dat'
        self.file_location = player_data
        self.file = load(self.file_location)
        self.invulnerable = bool(self.file['Invulnerable'])
        self.fall_flying = bool(self.file['FallFlying'])
        self.portal_cooldown = int(self.file['PortalCooldown'])
        self.absorption = float(self.file['AbsorptionAmount'])
        self.abilities = self.Abilities(file=self.file)
        self.fall_distance = float(self.file['FallDistance'])
        if 'active_effects' in self.file:
            self.effects = self.get_effects(self.file['active_effects'])
        else:
            self.effects = "There is no active effects"
        self.death_time = int(self.file['DeathTime'])
        self.xp = self.Xp(self.file)
        self.uuid = self.get_uuid(player_data=player_data)
        self.player_game_type = int(self.file['playerGameType'])
        self.spawn_dimension = str(self.file['SpawnDimension'])
        self.seen_credits = bool(self.file['seenCredits'])
        self.motion = [float(item) for item in self.file['Motion']]
        self.spawn = self.Spawn(self.file)
        self.health = float(self.file['Health'])
        self.food = self.Food_Stats(self.file)
        self.air = int(self.file['Air'])
        self.onground = bool(self.file['OnGround'])
        self.dimension = str(self.file['Dimension'])
        self.spawn_angle = float(self.file['SpawnAngle'])
        self.rotation = list(self.file['Rotation'])
        self.warden_spawn_tracker = {'warning_level': int(self.file['warden_spawn_tracker']['warning_level']), 'ticks_since_last_warning': int(self.file['warden_spawn_tracker']['ticks_since_last_warning']), 'cooldown_ticks': int(self.file['warden_spawn_tracker']['cooldown_ticks'])}
        self.score = int(self.file['Score'])
        self.pos = [float(item) for item in self.file['Pos']]
        self.fire = int(self.file['Fire'])
        self.data_version = int(self.file['DataVersion'])
        self.hurt_time = int(self.file['HurtTime'])
        self.selected_item_slot = int(self.file['SelectedItemSlot'])
        self.inventory = self.Inventory(inventory_items=self.file['Inventory'])
        self.ender_chest = self.Inventory(inventory_items=self.file['EnderItems'])
        self.stats_file = json.load(open(f'stats/{uuid}.json'))
        self.stats = self.Stats(values=self.stats_file['stats'])
        self.name, self.profile = self.get_name(self.uuid)


    class Inventory:
        def __init__(self, inventory_items):
            self.items = []
            if len(inventory_items) > 0:
                for item in inventory_items:
                    item = self.Item(item)
                    self.items.append(item)


        class Item:
            def __init__(self, item):
                self.id = str(item['id'])
                self.slot = int(item['Slot'])
                self.count = int(item['Count'])
                if 'tag' in item:
                    if 'Damage' in item['tag']:
                        self.damage = int(item['tag']['Damage'])
                    else:
                        self.damage = 0
                    if 'RepairCost' in item['tag']:
                        self.repaircost = int(item['tag']['RepairCost'])
                    else:
                        self.repaircost = 0
                    if 'Enchantments' in item['tag']:
                        self.enchantments = {}
                        for enchant in item['tag']['Enchantments']:
                            self.enchantments[str(enchant['id'])]: {int(enchant['lvl'])} 
                    else:
                        self.enchantments = None
            def __str__(self):
                return str(self.id)
        
        def __str__(self):
            if len(self.items) > 0:
                string = "["
                for item in self.items:
                    string += str(item).split(":")[1] + ", "
                string = list(string)
                string[-1], string[-2] = "]", ""
                return "".join(string)
            else:
                return "There is no Items"


    class Food_Stats:
        def __init__(self, file):
            self.saturation_level = float(file['foodSaturationLevel'])
            self.level = int(file['foodLevel'])
            self.exhaustion_level = float(file['foodExhaustionLevel'])
            self.tick_timer = int(file['foodTickTimer'])
            
        def __str__(self):
            return "The options are 'saturation_level', 'level' 'exhaustion_level' and 'tick_timer'."
            
    
    class Spawn:
        def __init__(self, file):
            self.x = float(file['SpawnX'])
            self.y = float(file['SpawnY'])
            self.z = float(file['SpawnZ'])
            self.angle = float(file['SpawnAngle'])
        
        def __str__(self):
            return "The options are 'x', 'y', 'z', and 'angle'."
    
    @staticmethod
    def get_uuid(player_data):
        return player_data.split("/")[-1].split(".")[0]
    
    
    class Xp:
        def __init__(self, file):
            self.total = int(file['XpTotal'])
            self.seed = int(file['XpSeed'])
            self.level = int(file['XpLevel'])
            self.p = float(file['XpP'])
        
        def __str__(self):
            return "The options are 'total', 'seed', 'level' and 'p'."
    
    
    @staticmethod
    def get_effects(active_effects):
        results = {}
        for effect in active_effects:
            effect_id = str(effect['id'])
            results[effect_id] = {
            'duration': int(effect['duration']),
            'show_icon': bool(effect['show_icon']),
            'amplifier': int(effect['amplifier']),
            'ambient': bool(effect['ambient']),
            'show_particles': bool(effect['show_particles'])
            }
        return results

    class Abilities:
        def __init__(self, file):
            self.invulnerable = bool(file['abilities']['invulnerable'])
            self.mayfly = bool(file['abilities']['mayfly'])
            self.instabuild = bool(file['abilities']['instabuild'])
            self.walk_speed = bool(file['abilities']['walkSpeed'])
            self.maybuild = bool(file['abilities']['mayBuild'])
            self.flying = bool(file['abilities']['flying'])
            self.fly_speed = float(file['abilities']['flySpeed'])
        
        def __str__(self):
            return "The options are 'invulnerable', 'mayfly', 'instabuild', 'walk_speed', 'maybuild', 'flying', 'fly_speed'."

    # noinspection PyArgumentList
    class Stats:
        def __init__(self, values):
            self.mined = self.dictionary(values=values['minecraft:mined'])
            self.dropped = self.dictionary(values=values['minecraft:dropped'])
            self.used = self.dictionary(values=values['minecraft:used'])
            self.picked_up = self.dictionary(values=values['minecraft:picked_up'])
            self.custom = self.dictionary(values=values['minecraft:custom'])
            self.killed = self.dictionary(values=values['minecraft:killed'])
            self.broken = self.dictionary(values=values['minecraft:broken'])
            self.crafted = self.dictionary(values=values['minecraft:crafted'])
    
        @staticmethod
        def dictionary(values):
            dictionary = {}
            for item in values:
                dictionary[item.split(':')[-1]] = int(values[item])
            return  dictionary
        
        def __str__(self):
            return "The options are 'mined', 'dropped', 'used', 'picked_up', 'custom', 'killed', 'broken' and 'crafted'."
                
    @staticmethod
    def get_name(uuid):
        api = API()
        name = api.get_username(uuid)
        profile = api.get_profile(uuid)
        return name, profile
    

user = UserStats("5612b91c-fb7b-4f3a-a85c-61415ebf9e1e")
print(user.profile)