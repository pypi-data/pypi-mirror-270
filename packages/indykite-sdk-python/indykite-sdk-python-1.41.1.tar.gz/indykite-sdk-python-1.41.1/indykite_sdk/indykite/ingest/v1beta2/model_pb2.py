# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indykite/ingest/v1beta2/model.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from indykite_sdk.indykite.objects.v1beta1 import struct_pb2 as indykite_dot_objects_dot_v1beta1_dot_struct__pb2
from indykite_sdk.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#indykite/ingest/v1beta2/model.proto\x12\x17indykite.ingest.v1beta2\x1a%indykite/objects/v1beta1/struct.proto\x1a\x17validate/validate.proto\"\xb2\x01\n\x06Record\x12\x18\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x18\x80\x02R\x02id\x12=\n\x06upsert\x18\x02 \x01(\x0b\x32#.indykite.ingest.v1beta2.UpsertDataH\x00R\x06upsert\x12=\n\x06\x64\x65lete\x18\x03 \x01(\x0b\x32#.indykite.ingest.v1beta2.DeleteDataH\x00R\x06\x64\x65leteB\x10\n\toperation\x12\x03\xf8\x42\x01\"\x8f\x01\n\nUpsertData\x12\x33\n\x04node\x18\x01 \x01(\x0b\x32\x1d.indykite.ingest.v1beta2.NodeH\x00R\x04node\x12?\n\x08relation\x18\x02 \x01(\x0b\x32!.indykite.ingest.v1beta2.RelationH\x00R\x08relationB\x0b\n\x04\x64\x61ta\x12\x03\xf8\x42\x01\"\x8f\x05\n\nDeleteData\x12\x38\n\x04node\x18\x01 \x01(\x0b\x32\".indykite.ingest.v1beta2.NodeMatchH\x00R\x04node\x12\x44\n\x08relation\x18\x02 \x01(\x0b\x32&.indykite.ingest.v1beta2.RelationMatchH\x00R\x08relation\x12\\\n\rnode_property\x18\x03 \x01(\x0b\x32\x35.indykite.ingest.v1beta2.DeleteData.NodePropertyMatchH\x00R\x0cnodeProperty\x12h\n\x11relation_property\x18\x04 \x01(\x0b\x32\x39.indykite.ingest.v1beta2.DeleteData.RelationPropertyMatchH\x00R\x10relationProperty\x1a\x90\x01\n\x11NodePropertyMatch\x12\x42\n\x05match\x18\x01 \x01(\x0b\x32\".indykite.ingest.v1beta2.NodeMatchB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x05match\x12\x37\n\x03key\x18\x02 \x01(\tB%\xfa\x42\"r (\x80\x02\x32\x18^[a-zA-Z_][a-zA-Z0-9_]+$\xd0\x01\x01R\x03key\x1a\x98\x01\n\x15RelationPropertyMatch\x12\x46\n\x05match\x18\x01 \x01(\x0b\x32&.indykite.ingest.v1beta2.RelationMatchB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x05match\x12\x37\n\x03key\x18\x02 \x01(\tB%\xfa\x42\"r (\x80\x02\x32\x18^[a-zA-Z_][a-zA-Z0-9_]+$\xd0\x01\x01R\x03keyB\x0b\n\x04\x64\x61ta\x12\x03\xf8\x42\x01\"\xc3\x03\n\x0b\x44igitalTwin\x12+\n\x0b\x65xternal_id\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\x80\x02R\nexternalId\x12-\n\x04type\x18\x02 \x01(\tB\x19\xfa\x42\x16r\x14\x18@2\x10^([A-Z][a-z]+)+$R\x04type\x12\x36\n\x04tags\x18\x03 \x03(\tB\"\xfa\x42\x1f\x92\x01\x1c\x10 \x18\x01\"\x16r\x14\x18@2\x10^([A-Z][a-z]+)+$R\x04tags\x12\x46\n\ttenant_id\x18\x05 \x01(\tB)\x18\x01\xfa\x42$r\"\x10\x16\x18\xfe\x01\x32\x18^[A-Za-z0-9-_:]{22,254}$\xd0\x01\x01R\x08tenantId\x12\x66\n\x13identity_properties\x18\x06 \x03(\x0b\x32).indykite.ingest.v1beta2.IdentityPropertyB\n\x18\x01\xfa\x42\x05\x92\x01\x02\x10\nR\x12identityProperties\x12K\n\nproperties\x18\x07 \x03(\x0b\x32!.indykite.ingest.v1beta2.PropertyB\x08\xfa\x42\x05\x92\x01\x02\x10\nR\nproperties\x12#\n\x02id\x18\x08 \x01(\tB\x13\xfa\x42\x10r\x0e\x10\x16\x18\x80\x02:\x04gid:\xd0\x01\x01R\x02id\"\xeb\x01\n\x08Resource\x12+\n\x0b\x65xternal_id\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\x80\x02R\nexternalId\x12-\n\x04type\x18\x02 \x01(\tB\x19\xfa\x42\x16r\x14\x18@2\x10^([A-Z][a-z]+)+$R\x04type\x12\x36\n\x04tags\x18\x03 \x03(\tB\"\xfa\x42\x1f\x92\x01\x1c\x10 \x18\x01\"\x16r\x14\x18@2\x10^([A-Z][a-z]+)+$R\x04tags\x12K\n\nproperties\x18\x04 \x03(\x0b\x32!.indykite.ingest.v1beta2.PropertyB\x08\xfa\x42\x05\x92\x01\x02\x10\x32R\nproperties\"\x82\x01\n\x10IdentityProperty\x12\x37\n\x03key\x18\x01 \x01(\tB%\xfa\x42\"r (\x80\x02\x32\x18^[a-zA-Z_][a-zA-Z0-9_]+$\xd0\x01\x01R\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.indykite.objects.v1beta1.ValueR\x05value\"\x9f\x01\n\x04Node\x12I\n\x0c\x64igital_twin\x18\x01 \x01(\x0b\x32$.indykite.ingest.v1beta2.DigitalTwinH\x00R\x0b\x64igitalTwin\x12?\n\x08resource\x18\x02 \x01(\x0b\x32!.indykite.ingest.v1beta2.ResourceH\x00R\x08resourceB\x0b\n\x04type\x12\x03\xf8\x42\x01\"z\n\x08Property\x12\x37\n\x03key\x18\x01 \x01(\tB%\xfa\x42\"r (\x80\x02\x32\x18^[a-zA-Z_][a-zA-Z0-9_]+$\xd0\x01\x01R\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.indykite.objects.v1beta1.ValueR\x05value\"\x9f\x01\n\x08Relation\x12\x46\n\x05match\x18\x01 \x01(\x0b\x32&.indykite.ingest.v1beta2.RelationMatchB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x05match\x12K\n\nproperties\x18\x02 \x03(\x0b\x32!.indykite.ingest.v1beta2.PropertyB\x08\xfa\x42\x05\x92\x01\x02\x10\x32R\nproperties\"g\n\tNodeMatch\x12+\n\x0b\x65xternal_id\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x10\x01\x18\x80\x02R\nexternalId\x12-\n\x04type\x18\x02 \x01(\tB\x19\xfa\x42\x16r\x14\x18@2\x10^([A-Z][a-z]+)+$R\x04type\"\xe5\x01\n\rRelationMatch\x12O\n\x0csource_match\x18\x01 \x01(\x0b\x32\".indykite.ingest.v1beta2.NodeMatchB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x0bsourceMatch\x12O\n\x0ctarget_match\x18\x02 \x01(\x0b\x32\".indykite.ingest.v1beta2.NodeMatchB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x0btargetMatch\x12\x32\n\x04type\x18\x03 \x01(\tB\x1e\xfa\x42\x1br\x19\x18\x80\x01\x32\x14^[A-Z]+(?:_[A-Z]+)*$R\x04type\"+\n\rPropertyError\x12\x1a\n\x08messages\x18\x01 \x03(\tR\x08messages\"\xdb\x01\n\x0bRecordError\x12\x61\n\x0fproperty_errors\x18\x01 \x03(\x0b\x32\x38.indykite.ingest.v1beta2.RecordError.PropertyErrorsEntryR\x0epropertyErrors\x1ai\n\x13PropertyErrorsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.indykite.ingest.v1beta2.PropertyErrorR\x05value:\x02\x38\x01\"A\n\x04Info\x12\x39\n\x07\x63hanges\x18\x01 \x03(\x0b\x32\x1f.indykite.ingest.v1beta2.ChangeR\x07\x63hanges\"\xce\x01\n\x06\x43hange\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x45\n\tdata_type\x18\x02 \x01(\x0e\x32(.indykite.ingest.v1beta2.Change.DataTypeR\x08\x64\x61taType\"m\n\x08\x44\x61taType\x12\x15\n\x11\x44\x41TA_TYPE_INVALID\x10\x00\x12\x1a\n\x16\x44\x41TA_TYPE_DIGITAL_TWIN\x10\x01\x12\x16\n\x12\x44\x41TA_TYPE_RESOURCE\x10\x02\x12\x16\n\x12\x44\x41TA_TYPE_RELATION\x10\x03\x42\xa7\x01\n\x1b\x63om.indykite.ingest.v1beta2B\nModelProtoP\x01\xa2\x02\x03IIX\xaa\x02\x17Indykite.Ingest.V1beta2\xca\x02\x17Indykite\\Ingest\\V1beta2\xe2\x02#Indykite\\Ingest\\V1beta2\\GPBMetadata\xea\x02\x19Indykite::Ingest::V1beta2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'indykite.ingest.v1beta2.model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.indykite.ingest.v1beta2B\nModelProtoP\001\242\002\003IIX\252\002\027Indykite.Ingest.V1beta2\312\002\027Indykite\\Ingest\\V1beta2\342\002#Indykite\\Ingest\\V1beta2\\GPBMetadata\352\002\031Indykite::Ingest::V1beta2'
  _globals['_RECORD'].oneofs_by_name['operation']._loaded_options = None
  _globals['_RECORD'].oneofs_by_name['operation']._serialized_options = b'\370B\001'
  _globals['_RECORD'].fields_by_name['id']._loaded_options = None
  _globals['_RECORD'].fields_by_name['id']._serialized_options = b'\372B\005r\003\030\200\002'
  _globals['_UPSERTDATA'].oneofs_by_name['data']._loaded_options = None
  _globals['_UPSERTDATA'].oneofs_by_name['data']._serialized_options = b'\370B\001'
  _globals['_DELETEDATA_NODEPROPERTYMATCH'].fields_by_name['match']._loaded_options = None
  _globals['_DELETEDATA_NODEPROPERTYMATCH'].fields_by_name['match']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_DELETEDATA_NODEPROPERTYMATCH'].fields_by_name['key']._loaded_options = None
  _globals['_DELETEDATA_NODEPROPERTYMATCH'].fields_by_name['key']._serialized_options = b'\372B\"r (\200\0022\030^[a-zA-Z_][a-zA-Z0-9_]+$\320\001\001'
  _globals['_DELETEDATA_RELATIONPROPERTYMATCH'].fields_by_name['match']._loaded_options = None
  _globals['_DELETEDATA_RELATIONPROPERTYMATCH'].fields_by_name['match']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_DELETEDATA_RELATIONPROPERTYMATCH'].fields_by_name['key']._loaded_options = None
  _globals['_DELETEDATA_RELATIONPROPERTYMATCH'].fields_by_name['key']._serialized_options = b'\372B\"r (\200\0022\030^[a-zA-Z_][a-zA-Z0-9_]+$\320\001\001'
  _globals['_DELETEDATA'].oneofs_by_name['data']._loaded_options = None
  _globals['_DELETEDATA'].oneofs_by_name['data']._serialized_options = b'\370B\001'
  _globals['_DIGITALTWIN'].fields_by_name['external_id']._loaded_options = None
  _globals['_DIGITALTWIN'].fields_by_name['external_id']._serialized_options = b'\372B\007r\005\020\001\030\200\002'
  _globals['_DIGITALTWIN'].fields_by_name['type']._loaded_options = None
  _globals['_DIGITALTWIN'].fields_by_name['type']._serialized_options = b'\372B\026r\024\030@2\020^([A-Z][a-z]+)+$'
  _globals['_DIGITALTWIN'].fields_by_name['tags']._loaded_options = None
  _globals['_DIGITALTWIN'].fields_by_name['tags']._serialized_options = b'\372B\037\222\001\034\020 \030\001\"\026r\024\030@2\020^([A-Z][a-z]+)+$'
  _globals['_DIGITALTWIN'].fields_by_name['tenant_id']._loaded_options = None
  _globals['_DIGITALTWIN'].fields_by_name['tenant_id']._serialized_options = b'\030\001\372B$r\"\020\026\030\376\0012\030^[A-Za-z0-9-_:]{22,254}$\320\001\001'
  _globals['_DIGITALTWIN'].fields_by_name['identity_properties']._loaded_options = None
  _globals['_DIGITALTWIN'].fields_by_name['identity_properties']._serialized_options = b'\030\001\372B\005\222\001\002\020\n'
  _globals['_DIGITALTWIN'].fields_by_name['properties']._loaded_options = None
  _globals['_DIGITALTWIN'].fields_by_name['properties']._serialized_options = b'\372B\005\222\001\002\020\n'
  _globals['_DIGITALTWIN'].fields_by_name['id']._loaded_options = None
  _globals['_DIGITALTWIN'].fields_by_name['id']._serialized_options = b'\372B\020r\016\020\026\030\200\002:\004gid:\320\001\001'
  _globals['_RESOURCE'].fields_by_name['external_id']._loaded_options = None
  _globals['_RESOURCE'].fields_by_name['external_id']._serialized_options = b'\372B\007r\005\020\001\030\200\002'
  _globals['_RESOURCE'].fields_by_name['type']._loaded_options = None
  _globals['_RESOURCE'].fields_by_name['type']._serialized_options = b'\372B\026r\024\030@2\020^([A-Z][a-z]+)+$'
  _globals['_RESOURCE'].fields_by_name['tags']._loaded_options = None
  _globals['_RESOURCE'].fields_by_name['tags']._serialized_options = b'\372B\037\222\001\034\020 \030\001\"\026r\024\030@2\020^([A-Z][a-z]+)+$'
  _globals['_RESOURCE'].fields_by_name['properties']._loaded_options = None
  _globals['_RESOURCE'].fields_by_name['properties']._serialized_options = b'\372B\005\222\001\002\0202'
  _globals['_IDENTITYPROPERTY'].fields_by_name['key']._loaded_options = None
  _globals['_IDENTITYPROPERTY'].fields_by_name['key']._serialized_options = b'\372B\"r (\200\0022\030^[a-zA-Z_][a-zA-Z0-9_]+$\320\001\001'
  _globals['_NODE'].oneofs_by_name['type']._loaded_options = None
  _globals['_NODE'].oneofs_by_name['type']._serialized_options = b'\370B\001'
  _globals['_PROPERTY'].fields_by_name['key']._loaded_options = None
  _globals['_PROPERTY'].fields_by_name['key']._serialized_options = b'\372B\"r (\200\0022\030^[a-zA-Z_][a-zA-Z0-9_]+$\320\001\001'
  _globals['_RELATION'].fields_by_name['match']._loaded_options = None
  _globals['_RELATION'].fields_by_name['match']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_RELATION'].fields_by_name['properties']._loaded_options = None
  _globals['_RELATION'].fields_by_name['properties']._serialized_options = b'\372B\005\222\001\002\0202'
  _globals['_NODEMATCH'].fields_by_name['external_id']._loaded_options = None
  _globals['_NODEMATCH'].fields_by_name['external_id']._serialized_options = b'\372B\007r\005\020\001\030\200\002'
  _globals['_NODEMATCH'].fields_by_name['type']._loaded_options = None
  _globals['_NODEMATCH'].fields_by_name['type']._serialized_options = b'\372B\026r\024\030@2\020^([A-Z][a-z]+)+$'
  _globals['_RELATIONMATCH'].fields_by_name['source_match']._loaded_options = None
  _globals['_RELATIONMATCH'].fields_by_name['source_match']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_RELATIONMATCH'].fields_by_name['target_match']._loaded_options = None
  _globals['_RELATIONMATCH'].fields_by_name['target_match']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_RELATIONMATCH'].fields_by_name['type']._loaded_options = None
  _globals['_RELATIONMATCH'].fields_by_name['type']._serialized_options = b'\372B\033r\031\030\200\0012\024^[A-Z]+(?:_[A-Z]+)*$'
  _globals['_RECORDERROR_PROPERTYERRORSENTRY']._loaded_options = None
  _globals['_RECORDERROR_PROPERTYERRORSENTRY']._serialized_options = b'8\001'
  _globals['_RECORD']._serialized_start=129
  _globals['_RECORD']._serialized_end=307
  _globals['_UPSERTDATA']._serialized_start=310
  _globals['_UPSERTDATA']._serialized_end=453
  _globals['_DELETEDATA']._serialized_start=456
  _globals['_DELETEDATA']._serialized_end=1111
  _globals['_DELETEDATA_NODEPROPERTYMATCH']._serialized_start=799
  _globals['_DELETEDATA_NODEPROPERTYMATCH']._serialized_end=943
  _globals['_DELETEDATA_RELATIONPROPERTYMATCH']._serialized_start=946
  _globals['_DELETEDATA_RELATIONPROPERTYMATCH']._serialized_end=1098
  _globals['_DIGITALTWIN']._serialized_start=1114
  _globals['_DIGITALTWIN']._serialized_end=1565
  _globals['_RESOURCE']._serialized_start=1568
  _globals['_RESOURCE']._serialized_end=1803
  _globals['_IDENTITYPROPERTY']._serialized_start=1806
  _globals['_IDENTITYPROPERTY']._serialized_end=1936
  _globals['_NODE']._serialized_start=1939
  _globals['_NODE']._serialized_end=2098
  _globals['_PROPERTY']._serialized_start=2100
  _globals['_PROPERTY']._serialized_end=2222
  _globals['_RELATION']._serialized_start=2225
  _globals['_RELATION']._serialized_end=2384
  _globals['_NODEMATCH']._serialized_start=2386
  _globals['_NODEMATCH']._serialized_end=2489
  _globals['_RELATIONMATCH']._serialized_start=2492
  _globals['_RELATIONMATCH']._serialized_end=2721
  _globals['_PROPERTYERROR']._serialized_start=2723
  _globals['_PROPERTYERROR']._serialized_end=2766
  _globals['_RECORDERROR']._serialized_start=2769
  _globals['_RECORDERROR']._serialized_end=2988
  _globals['_RECORDERROR_PROPERTYERRORSENTRY']._serialized_start=2883
  _globals['_RECORDERROR_PROPERTYERRORSENTRY']._serialized_end=2988
  _globals['_INFO']._serialized_start=2990
  _globals['_INFO']._serialized_end=3055
  _globals['_CHANGE']._serialized_start=3058
  _globals['_CHANGE']._serialized_end=3264
  _globals['_CHANGE_DATATYPE']._serialized_start=3155
  _globals['_CHANGE_DATATYPE']._serialized_end=3264
# @@protoc_insertion_point(module_scope)
