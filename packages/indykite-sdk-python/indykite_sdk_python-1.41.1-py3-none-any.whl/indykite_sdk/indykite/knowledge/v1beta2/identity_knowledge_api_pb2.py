# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indykite/knowledge/v1beta2/identity_knowledge_api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from indykite_sdk.indykite.knowledge.v1beta2 import model_pb2 as indykite_dot_knowledge_dot_v1beta2_dot_model__pb2
from indykite_sdk.indykite.knowledge.objects.v1beta1 import ikg_pb2 as indykite_dot_knowledge_dot_objects_dot_v1beta1_dot_ikg__pb2
from indykite_sdk.indykite.objects.v1beta2 import value_pb2 as indykite_dot_objects_dot_v1beta2_dot_value__pb2
from indykite_sdk.validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7indykite/knowledge/v1beta2/identity_knowledge_api.proto\x12\x1aindykite.knowledge.v1beta2\x1a&indykite/knowledge/v1beta2/model.proto\x1a,indykite/knowledge/objects/v1beta1/ikg.proto\x1a$indykite/objects/v1beta2/value.proto\x1a\x17validate/validate.proto\"\xd8\x02\n\x1cIdentityKnowledgeReadRequest\x12\x1f\n\x05query\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04(\x80\xa0\x1fR\x05query\x12l\n\x0cinput_params\x18\x02 \x03(\x0b\x32I.indykite.knowledge.v1beta2.IdentityKnowledgeReadRequest.InputParamsEntryR\x0binputParams\x12H\n\x07returns\x18\x03 \x03(\x0b\x32\".indykite.knowledge.v1beta2.ReturnB\n\xfa\x42\x07\x92\x01\x04\x08\x01\x10\x14R\x07returns\x1a_\n\x10InputParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32\x1f.indykite.objects.v1beta2.ValueR\x05value:\x02\x38\x01\"\xb7\x01\n\x1dIdentityKnowledgeReadResponse\x12>\n\x05nodes\x18\x01 \x03(\x0b\x32(.indykite.knowledge.objects.v1beta1.NodeR\x05nodes\x12V\n\rrelationships\x18\x02 \x03(\x0b\x32\x30.indykite.knowledge.objects.v1beta1.RelationshipR\rrelationships2\xa5\x01\n\x14IdentityKnowledgeAPI\x12\x8c\x01\n\x15IdentityKnowledgeRead\x12\x38.indykite.knowledge.v1beta2.IdentityKnowledgeReadRequest\x1a\x39.indykite.knowledge.v1beta2.IdentityKnowledgeReadResponseB\xc5\x01\n\x1e\x63om.indykite.knowledge.v1beta2B\x19IdentityKnowledgeApiProtoP\x01\xa2\x02\x03IKX\xaa\x02\x1aIndykite.Knowledge.V1beta2\xca\x02\x1aIndykite\\Knowledge\\V1beta2\xe2\x02&Indykite\\Knowledge\\V1beta2\\GPBMetadata\xea\x02\x1cIndykite::Knowledge::V1beta2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'indykite.knowledge.v1beta2.identity_knowledge_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.indykite.knowledge.v1beta2B\031IdentityKnowledgeApiProtoP\001\242\002\003IKX\252\002\032Indykite.Knowledge.V1beta2\312\002\032Indykite\\Knowledge\\V1beta2\342\002&Indykite\\Knowledge\\V1beta2\\GPBMetadata\352\002\034Indykite::Knowledge::V1beta2'
  _globals['_IDENTITYKNOWLEDGEREADREQUEST_INPUTPARAMSENTRY']._loaded_options = None
  _globals['_IDENTITYKNOWLEDGEREADREQUEST_INPUTPARAMSENTRY']._serialized_options = b'8\001'
  _globals['_IDENTITYKNOWLEDGEREADREQUEST'].fields_by_name['query']._loaded_options = None
  _globals['_IDENTITYKNOWLEDGEREADREQUEST'].fields_by_name['query']._serialized_options = b'\372B\006r\004(\200\240\037'
  _globals['_IDENTITYKNOWLEDGEREADREQUEST'].fields_by_name['returns']._loaded_options = None
  _globals['_IDENTITYKNOWLEDGEREADREQUEST'].fields_by_name['returns']._serialized_options = b'\372B\007\222\001\004\010\001\020\024'
  _globals['_IDENTITYKNOWLEDGEREADREQUEST']._serialized_start=237
  _globals['_IDENTITYKNOWLEDGEREADREQUEST']._serialized_end=581
  _globals['_IDENTITYKNOWLEDGEREADREQUEST_INPUTPARAMSENTRY']._serialized_start=486
  _globals['_IDENTITYKNOWLEDGEREADREQUEST_INPUTPARAMSENTRY']._serialized_end=581
  _globals['_IDENTITYKNOWLEDGEREADRESPONSE']._serialized_start=584
  _globals['_IDENTITYKNOWLEDGEREADRESPONSE']._serialized_end=767
  _globals['_IDENTITYKNOWLEDGEAPI']._serialized_start=770
  _globals['_IDENTITYKNOWLEDGEAPI']._serialized_end=935
# @@protoc_insertion_point(module_scope)
