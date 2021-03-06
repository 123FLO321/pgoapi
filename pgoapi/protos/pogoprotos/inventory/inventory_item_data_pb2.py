# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/inventory_item_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_data_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__data__pb2
from pogoprotos.inventory import applied_items_pb2 as pogoprotos_dot_inventory_dot_applied__items__pb2
from pogoprotos.inventory import egg_incubators_pb2 as pogoprotos_dot_inventory_dot_egg__incubators__pb2
from pogoprotos.inventory import candy_pb2 as pogoprotos_dot_inventory_dot_candy__pb2
from pogoprotos.inventory import inventory_upgrades_pb2 as pogoprotos_dot_inventory_dot_inventory__upgrades__pb2
from pogoprotos.inventory import raid_tickets_pb2 as pogoprotos_dot_inventory_dot_raid__tickets__pb2
from pogoprotos.data.avatar import avatar_item_pb2 as pogoprotos_dot_data_dot_avatar_dot_avatar__item__pb2
from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.data import pokedex_entry_pb2 as pogoprotos_dot_data_dot_pokedex__entry__pb2
from pogoprotos.data.player import player_stats_pb2 as pogoprotos_dot_data_dot_player_dot_player__stats__pb2
from pogoprotos.data.player import player_currency_pb2 as pogoprotos_dot_data_dot_player_dot_player__currency__pb2
from pogoprotos.data.player import player_camera_pb2 as pogoprotos_dot_data_dot_player_dot_player__camera__pb2
from pogoprotos.data.quests import quest_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/inventory_item_data.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_pb=_b('\n.pogoprotos/inventory/inventory_item_data.proto\x12\x14pogoprotos.inventory\x1a)pogoprotos/inventory/item/item_data.proto\x1a(pogoprotos/inventory/applied_items.proto\x1a)pogoprotos/inventory/egg_incubators.proto\x1a pogoprotos/inventory/candy.proto\x1a-pogoprotos/inventory/inventory_upgrades.proto\x1a\'pogoprotos/inventory/raid_tickets.proto\x1a(pogoprotos/data/avatar/avatar_item.proto\x1a\"pogoprotos/data/pokemon_data.proto\x1a#pogoprotos/data/pokedex_entry.proto\x1a)pogoprotos/data/player/player_stats.proto\x1a,pogoprotos/data/player/player_currency.proto\x1a*pogoprotos/data/player/player_camera.proto\x1a\"pogoprotos/data/quests/quest.proto\"\xf2\x05\n\x11InventoryItemData\x12\x32\n\x0cpokemon_data\x18\x01 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12\x31\n\x04item\x18\x02 \x01(\x0b\x32#.pogoprotos.inventory.item.ItemData\x12\x34\n\rpokedex_entry\x18\x03 \x01(\x0b\x32\x1d.pogoprotos.data.PokedexEntry\x12\x39\n\x0cplayer_stats\x18\x04 \x01(\x0b\x32#.pogoprotos.data.player.PlayerStats\x12?\n\x0fplayer_currency\x18\x05 \x01(\x0b\x32&.pogoprotos.data.player.PlayerCurrency\x12;\n\rplayer_camera\x18\x06 \x01(\x0b\x32$.pogoprotos.data.player.PlayerCamera\x12\x43\n\x12inventory_upgrades\x18\x07 \x01(\x0b\x32\'.pogoprotos.inventory.InventoryUpgrades\x12\x39\n\rapplied_items\x18\x08 \x01(\x0b\x32\".pogoprotos.inventory.AppliedItems\x12;\n\x0e\x65gg_incubators\x18\t \x01(\x0b\x32#.pogoprotos.inventory.EggIncubators\x12*\n\x05\x63\x61ndy\x18\n \x01(\x0b\x32\x1b.pogoprotos.inventory.Candy\x12,\n\x05quest\x18\x0b \x01(\x0b\x32\x1d.pogoprotos.data.quests.Quest\x12\x37\n\x0b\x61vatar_item\x18\x0c \x01(\x0b\x32\".pogoprotos.data.avatar.AvatarItem\x12\x37\n\x0craid_tickets\x18\r \x01(\x0b\x32!.pogoprotos.inventory.RaidTicketsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__data__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_applied__items__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_egg__incubators__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_candy__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_inventory__upgrades__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_raid__tickets__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_avatar_dot_avatar__item__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokedex__entry__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__stats__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__currency__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_player_dot_player__camera__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_quests_dot_quest__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INVENTORYITEMDATA = _descriptor.Descriptor(
  name='InventoryItemData',
  full_name='pogoprotos.inventory.InventoryItemData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_data', full_name='pogoprotos.inventory.InventoryItemData.pokemon_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.inventory.InventoryItemData.item', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_entry', full_name='pogoprotos.inventory.InventoryItemData.pokedex_entry', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_stats', full_name='pogoprotos.inventory.InventoryItemData.player_stats', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_currency', full_name='pogoprotos.inventory.InventoryItemData.player_currency', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_camera', full_name='pogoprotos.inventory.InventoryItemData.player_camera', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_upgrades', full_name='pogoprotos.inventory.InventoryItemData.inventory_upgrades', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_items', full_name='pogoprotos.inventory.InventoryItemData.applied_items', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_incubators', full_name='pogoprotos.inventory.InventoryItemData.egg_incubators', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy', full_name='pogoprotos.inventory.InventoryItemData.candy', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest', full_name='pogoprotos.inventory.InventoryItemData.quest', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_item', full_name='pogoprotos.inventory.InventoryItemData.avatar_item', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raid_tickets', full_name='pogoprotos.inventory.InventoryItemData.raid_tickets', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=607,
  serialized_end=1361,
)

_INVENTORYITEMDATA.fields_by_name['pokemon_data'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_INVENTORYITEMDATA.fields_by_name['item'].message_type = pogoprotos_dot_inventory_dot_item_dot_item__data__pb2._ITEMDATA
_INVENTORYITEMDATA.fields_by_name['pokedex_entry'].message_type = pogoprotos_dot_data_dot_pokedex__entry__pb2._POKEDEXENTRY
_INVENTORYITEMDATA.fields_by_name['player_stats'].message_type = pogoprotos_dot_data_dot_player_dot_player__stats__pb2._PLAYERSTATS
_INVENTORYITEMDATA.fields_by_name['player_currency'].message_type = pogoprotos_dot_data_dot_player_dot_player__currency__pb2._PLAYERCURRENCY
_INVENTORYITEMDATA.fields_by_name['player_camera'].message_type = pogoprotos_dot_data_dot_player_dot_player__camera__pb2._PLAYERCAMERA
_INVENTORYITEMDATA.fields_by_name['inventory_upgrades'].message_type = pogoprotos_dot_inventory_dot_inventory__upgrades__pb2._INVENTORYUPGRADES
_INVENTORYITEMDATA.fields_by_name['applied_items'].message_type = pogoprotos_dot_inventory_dot_applied__items__pb2._APPLIEDITEMS
_INVENTORYITEMDATA.fields_by_name['egg_incubators'].message_type = pogoprotos_dot_inventory_dot_egg__incubators__pb2._EGGINCUBATORS
_INVENTORYITEMDATA.fields_by_name['candy'].message_type = pogoprotos_dot_inventory_dot_candy__pb2._CANDY
_INVENTORYITEMDATA.fields_by_name['quest'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__pb2._QUEST
_INVENTORYITEMDATA.fields_by_name['avatar_item'].message_type = pogoprotos_dot_data_dot_avatar_dot_avatar__item__pb2._AVATARITEM
_INVENTORYITEMDATA.fields_by_name['raid_tickets'].message_type = pogoprotos_dot_inventory_dot_raid__tickets__pb2._RAIDTICKETS
DESCRIPTOR.message_types_by_name['InventoryItemData'] = _INVENTORYITEMDATA

InventoryItemData = _reflection.GeneratedProtocolMessageType('InventoryItemData', (_message.Message,), dict(
  DESCRIPTOR = _INVENTORYITEMDATA,
  __module__ = 'pogoprotos.inventory.inventory_item_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.InventoryItemData)
  ))
_sym_db.RegisterMessage(InventoryItemData)


# @@protoc_insertion_point(module_scope)
