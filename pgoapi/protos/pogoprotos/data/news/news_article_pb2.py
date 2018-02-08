# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/news/news_article.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/news/news_article.proto',
  package='pogoprotos.data.news',
  syntax='proto3',
  serialized_pb=_b('\n\'pogoprotos/data/news/news_article.proto\x12\x14pogoprotos.data.news\"\x9b\x02\n\x0bNewsArticle\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\timage_url\x18\x02 \x03(\t\x12\x12\n\nheader_key\x18\x03 \x01(\t\x12\x15\n\rsubheader_key\x18\x04 \x01(\t\x12\x15\n\rmain_text_key\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x12@\n\x08template\x18\x07 \x01(\x0e\x32..pogoprotos.data.news.NewsArticle.NewsTemplate\x12\x0f\n\x07\x65nabled\x18\x08 \x01(\x08\x12\x14\n\x0c\x61rticle_read\x18\t \x01(\x08\"/\n\x0cNewsTemplate\x12\t\n\x05UNSET\x10\x00\x12\x14\n\x10\x44\x45\x46\x41ULT_TEMPLATE\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_NEWSARTICLE_NEWSTEMPLATE = _descriptor.EnumDescriptor(
  name='NewsTemplate',
  full_name='pogoprotos.data.news.NewsArticle.NewsTemplate',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_TEMPLATE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=302,
  serialized_end=349,
)
_sym_db.RegisterEnumDescriptor(_NEWSARTICLE_NEWSTEMPLATE)


_NEWSARTICLE = _descriptor.Descriptor(
  name='NewsArticle',
  full_name='pogoprotos.data.news.NewsArticle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.data.news.NewsArticle.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='pogoprotos.data.news.NewsArticle.image_url', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='header_key', full_name='pogoprotos.data.news.NewsArticle.header_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subheader_key', full_name='pogoprotos.data.news.NewsArticle.subheader_key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='main_text_key', full_name='pogoprotos.data.news.NewsArticle.main_text_key', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='pogoprotos.data.news.NewsArticle.timestamp', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='template', full_name='pogoprotos.data.news.NewsArticle.template', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='pogoprotos.data.news.NewsArticle.enabled', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='article_read', full_name='pogoprotos.data.news.NewsArticle.article_read', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NEWSARTICLE_NEWSTEMPLATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=349,
)

_NEWSARTICLE.fields_by_name['template'].enum_type = _NEWSARTICLE_NEWSTEMPLATE
_NEWSARTICLE_NEWSTEMPLATE.containing_type = _NEWSARTICLE
DESCRIPTOR.message_types_by_name['NewsArticle'] = _NEWSARTICLE

NewsArticle = _reflection.GeneratedProtocolMessageType('NewsArticle', (_message.Message,), dict(
  DESCRIPTOR = _NEWSARTICLE,
  __module__ = 'pogoprotos.data.news.news_article_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.news.NewsArticle)
  ))
_sym_db.RegisterMessage(NewsArticle)


# @@protoc_insertion_point(module_scope)
