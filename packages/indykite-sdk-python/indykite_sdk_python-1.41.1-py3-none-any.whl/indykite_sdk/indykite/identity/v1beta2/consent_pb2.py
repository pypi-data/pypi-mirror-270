# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indykite/identity/v1beta2/consent.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'indykite/identity/v1beta2/consent.proto\x12\x19indykite.identity.v1beta2\x1a\x1fgoogle/protobuf/timestamp.proto\"\xaf\x03\n\x0e\x43onsentReceipt\x12(\n\x10pii_principal_id\x18\x01 \x01(\tR\x0epiiPrincipalId\x12L\n\rpii_processor\x18\x02 \x01(\x0b\x32\'.indykite.identity.v1beta2.PiiProcessorR\x0cpiiProcessor\x12\x44\n\x05items\x18\x03 \x03(\x0b\x32..indykite.identity.v1beta2.ConsentReceipt.ItemR\x05items\x1a\xde\x01\n\x04Item\x12\x1d\n\nconsent_id\x18\x01 \x01(\tR\tconsentId\x12O\n\x0epii_controller\x18\x02 \x01(\x0b\x32(.indykite.identity.v1beta2.PiiControllerR\rpiiController\x12\x46\n\x11\x63onsented_at_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0f\x63onsentedAtTime\x12\x1e\n\nproperties\x18\x04 \x03(\tR\nproperties\"^\n\rPiiController\x12*\n\x11pii_controller_id\x18\x01 \x01(\tR\x0fpiiControllerId\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\"\x8b\x03\n\x0cPiiProcessor\x12(\n\x10pii_processor_id\x18\x01 \x01(\tR\x0epiiProcessorId\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x14\n\x05owner\x18\x04 \x01(\tR\x05owner\x12\x1d\n\npolicy_uri\x18\x05 \x01(\tR\tpolicyUri\x12/\n\x14terms_of_service_uri\x18\x06 \x01(\tR\x11termsOfServiceUri\x12\x1d\n\nclient_uri\x18\x07 \x01(\tR\tclientUri\x12\x19\n\x08logo_uri\x18\x08 \x01(\tR\x07logoUri\x12;\n\x1auser_support_email_address\x18\t \x01(\tR\x17userSupportEmailAddress\x12/\n\x13\x61\x64\x64itional_contacts\x18\n \x03(\tR\x12\x61\x64\x64itionalContactsB\xb3\x01\n\x1d\x63om.indykite.identity.v1beta2B\x0c\x43onsentProtoP\x01\xa2\x02\x03IIX\xaa\x02\x19Indykite.Identity.V1beta2\xca\x02\x19Indykite\\Identity\\V1beta2\xe2\x02%Indykite\\Identity\\V1beta2\\GPBMetadata\xea\x02\x1bIndykite::Identity::V1beta2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'indykite.identity.v1beta2.consent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.indykite.identity.v1beta2B\014ConsentProtoP\001\242\002\003IIX\252\002\031Indykite.Identity.V1beta2\312\002\031Indykite\\Identity\\V1beta2\342\002%Indykite\\Identity\\V1beta2\\GPBMetadata\352\002\033Indykite::Identity::V1beta2'
  _globals['_CONSENTRECEIPT']._serialized_start=104
  _globals['_CONSENTRECEIPT']._serialized_end=535
  _globals['_CONSENTRECEIPT_ITEM']._serialized_start=313
  _globals['_CONSENTRECEIPT_ITEM']._serialized_end=535
  _globals['_PIICONTROLLER']._serialized_start=537
  _globals['_PIICONTROLLER']._serialized_end=631
  _globals['_PIIPROCESSOR']._serialized_start=634
  _globals['_PIIPROCESSOR']._serialized_end=1029
# @@protoc_insertion_point(module_scope)
