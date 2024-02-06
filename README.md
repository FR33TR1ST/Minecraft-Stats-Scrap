# Minecraft User Stats Scrap

### Dependecies
- Mojang
- Nbtlib

#### Concepts
The UUID argument is the Universally Unique IDentifier of a minecraft user.
The User attributes as Inventory and Enchantments is found in stats folder on the world minecraft folder

### Quick Start
``` python
from functions import UserStats
# Here you introduce your uuid
user = UserStats('uuid')
print(user.name)
```

### Values
- file_location: Where is the Attributes File
- file: Loaded File
- invulnerable: Player Invulneravility => Boolean
- fall_flying: If the Player is falling => Boolean
- portal_cooldown: Player Cooldown to Portal Travelling => Integer
- absorption: Absorption Quantity => Float
- abilities: [Abilities Class](#abilities)
- fall_distance: Distance to the ground => Float
- effects: Active Effects => Dictionary or None
- death_time: => Integer
- xp: [XP Class](#xp)
- uuid: Player UUID => String
- player_game_type: Player Game Mode => Integer
- spawn_dimension: Spawn Dimension => String
- seen_credits: If Credits were seen => Boolean
- spawn: [Spawn Class](#spawn)
- motion:  => List
- health: Player Health => Float
- food: [Food Class](#food)
- air:  => Integer
- onground: If Player is OnGround => Boolean
- dimension: Player Dimension => String
- spawn_angle: Spawn Angle => Float
- rotation:  => List
- warden_spawn_tracker: Warden Near Stats => Dictionary
- score: Player Score => Integer
- pos:  => Floats List
- fire:  => Integer
- data_version: Data Version => Integer
- hurt_time:  => Integer
- selected_item_slot: Selected Item Slot => Integer
- inventory: [Inventory Class](#inventory) => List or Text
- ender_chest: [Inventory Class](#inventory) => List or Text
- stats_file: File Opened => Json State
- stats: [Stats Class](#stats) => String if its called
- name: Player Name => String
- profile: [Player Profile](#profile)

##### Abilities
- abilities.invulnerable: Player Invulneravility => Boolean
- abilities.mayfly: May the Player Fly => Boolean
- abilities.instabuild: Can the Player Instabuild => Boolean
- abilities.walk_speed: If the Player is Walking => Boolean
- abilities.maybuild: May the Player Build => Boolean
- abilities.flying: If the Player is Flying => Boolean
- abilities.fly_speed: Fly Speed => Float

##### XP
- xp.total: Total XP => Integer
- xp.seed: Xp Seed => Integer
- xp.level: Xp Level => Integer
- xp.p: => Float

##### Spawn
- spawn.x: X Spawn Position => Float
- spawn.y: Y Spawn Position => Float
- spawn.z: Z Spawn Position => Float
- spawn.angle: Spawn Angle => Float

##### Food
- food.saturation_level: Food Saturation => Float
- food.level:  => Integer
- food.exhaustion: Exaustion Level => Float
- food.tick_timer:  => Integer

##### Inventory
- inventory.items: [Item Class](#item) List

##### Item
- inventory.item[n]: Item Name => String
- inventory.item[n].id: Item Name => String
- inventory.item[n].slot: Slot Item => Integer
- inventory.item[n].count: Item Quantity => Integer
- inventory.item[n].damage: Item Damage => Integer
- inventory.item[n].rapaircost: Repair Cost => Integer
- inventory.item[n].enchantments: Enchantments => Dictionary or None

##### Stats
- stats.mined: Mined Blocks => Dictionary
- stats.dropped: Blocks Dropped => Dictionary
- stats.used: Used Blocks => Dictionary
- stats.picked_up: Blocks Picked Up => Dictionary
- stats.custom:  => Dictionary
- stats.killed: Killed Mobs => Dictionary
- stats.broken: Broken Blocks => Dictionary
- stats.crafted: Crafted Items => Dictionary

##### Profile
+ id: str #
+ timestamp: int #
+ name: str #
+ is_legacy_profile: bool #
+ skin_variant: str #
+ cape_url: Optional[str] = None #
+ skin_url: Optional[str] = None #
