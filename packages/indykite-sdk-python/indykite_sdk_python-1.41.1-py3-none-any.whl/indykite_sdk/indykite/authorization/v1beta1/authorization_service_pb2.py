# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indykite/authorization/v1beta1/authorization_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from indykite_sdk.validate import validate_pb2 as validate_dot_validate__pb2
from indykite_sdk.indykite.authorization.v1beta1 import model_pb2 as indykite_dot_authorization_dot_v1beta1_dot_model__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:indykite/authorization/v1beta1/authorization_service.proto\x12\x1eindykite.authorization.v1beta1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17validate/validate.proto\x1a*indykite/authorization/v1beta1/model.proto\"\xca\x05\n\x13IsAuthorizedRequest\x12K\n\x07subject\x18\x01 \x01(\x0b\x32\'.indykite.authorization.v1beta1.SubjectB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\x12\x66\n\tresources\x18\x02 \x03(\x0b\x32<.indykite.authorization.v1beta1.IsAuthorizedRequest.ResourceB\n\xfa\x42\x07\x92\x01\x04\x08\x01\x10 R\tresources\x12\x98\x01\n\x0cinput_params\x18\x03 \x03(\x0b\x32\x44.indykite.authorization.v1beta1.IsAuthorizedRequest.InputParamsEntryB/\xfa\x42,\x9a\x01)\x08\x00\x10\x14\"#r!\x10\x01\x18\x14\x32\x1b^(?:[a-zA-Z][a-zA-Z0-9]+)+$R\x0binputParams\x12\x43\n\x0bpolicy_tags\x18\x04 \x03(\tB\"\xfa\x42\x1f\x92\x01\x1c\x18\x01\"\x16r\x14\x10\x01\x18\x14\x32\x0e^[a-zA-Z0-9]+$(\x01R\npolicyTags\x1a\xb1\x01\n\x08Resource\x12*\n\x0b\x65xternal_id\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x02\x18\x32R\nexternalId\x12\x31\n\x04type\x18\x02 \x01(\tB\x1d\xfa\x42\x1ar\x18\x10\x02\x18\x32\x32\x12^(?:[A-Z][a-z]+)+$R\x04type\x12\x46\n\x07\x61\x63tions\x18\x03 \x03(\tB,\xfa\x42)\x92\x01&\x08\x01\x10\x05\" r\x1e\x10\x02\x18\x32\x32\x18^[a-zA-Z0-9.:_\\-\\/]{2,}$R\x07\x61\x63tions\x1aj\n\x10InputParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12@\n\x05value\x18\x02 \x01(\x0b\x32*.indykite.authorization.v1beta1.InputParamR\x05value:\x02\x38\x01\"\xc5\x06\n\x14IsAuthorizedResponse\x12?\n\rdecision_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x64\x65\x63isionTime\x12\x61\n\tdecisions\x18\x02 \x03(\x0b\x32\x43.indykite.authorization.v1beta1.IsAuthorizedResponse.DecisionsEntryR\tdecisions\x1a\x1e\n\x06\x41\x63tion\x12\x14\n\x05\x61llow\x18\x01 \x01(\x08R\x05\x61llow\x1a\xe9\x01\n\x08Resource\x12\x64\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32J.indykite.authorization.v1beta1.IsAuthorizedResponse.Resource.ActionsEntryR\x07\x61\x63tions\x1aw\n\x0c\x41\x63tionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12Q\n\x05value\x18\x02 \x01(\x0b\x32;.indykite.authorization.v1beta1.IsAuthorizedResponse.ActionR\x05value:\x02\x38\x01\x1a\xfb\x01\n\x0cResourceType\x12n\n\tresources\x18\x01 \x03(\x0b\x32P.indykite.authorization.v1beta1.IsAuthorizedResponse.ResourceType.ResourcesEntryR\tresources\x1a{\n\x0eResourcesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12S\n\x05value\x18\x02 \x01(\x0b\x32=.indykite.authorization.v1beta1.IsAuthorizedResponse.ResourceR\x05value:\x02\x38\x01\x1a\x7f\n\x0e\x44\x65\x63isionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12W\n\x05value\x18\x02 \x01(\x0b\x32\x41.indykite.authorization.v1beta1.IsAuthorizedResponse.ResourceTypeR\x05value:\x02\x38\x01\"\xb7\x05\n\x15WhatAuthorizedRequest\x12K\n\x07subject\x18\x01 \x01(\x0b\x32\'.indykite.authorization.v1beta1.SubjectB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07subject\x12u\n\x0eresource_types\x18\x02 \x03(\x0b\x32\x42.indykite.authorization.v1beta1.WhatAuthorizedRequest.ResourceTypeB\n\xfa\x42\x07\x92\x01\x04\x08\x01\x10\nR\rresourceTypes\x12\x9a\x01\n\x0cinput_params\x18\x03 \x03(\x0b\x32\x46.indykite.authorization.v1beta1.WhatAuthorizedRequest.InputParamsEntryB/\xfa\x42,\x9a\x01)\x08\x00\x10\x14\"#r!\x10\x01\x18\x14\x32\x1b^(?:[a-zA-Z][a-zA-Z0-9]+)+$R\x0binputParams\x12\x43\n\x0bpolicy_tags\x18\x04 \x03(\tB\"\xfa\x42\x1f\x92\x01\x1c\x18\x01\"\x16r\x14\x10\x01\x18\x14\x32\x0e^[a-zA-Z0-9]+$(\x01R\npolicyTags\x1a\x8b\x01\n\x0cResourceType\x12\x31\n\x04type\x18\x01 \x01(\tB\x1d\xfa\x42\x1ar\x18\x10\x02\x18\x32\x32\x12^(?:[A-Z][a-z]+)+$R\x04type\x12H\n\x07\x61\x63tions\x18\x03 \x03(\tB.\xfa\x42+\x92\x01(\x08\x01\x10\x05\" r\x1e\x10\x02\x18\x32\x32\x18^[a-zA-Z0-9.:_\\-\\/]{2,}$(\x01R\x07\x61\x63tions\x1aj\n\x10InputParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12@\n\x05value\x18\x02 \x01(\x0b\x32*.indykite.authorization.v1beta1.InputParamR\x05value:\x02\x38\x01\"\xd0\x05\n\x16WhatAuthorizedResponse\x12?\n\rdecision_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x64\x65\x63isionTime\x12\x63\n\tdecisions\x18\x02 \x03(\x0b\x32\x45.indykite.authorization.v1beta1.WhatAuthorizedResponse.DecisionsEntryR\tdecisions\x1a+\n\x08Resource\x12\x1f\n\x0b\x65xternal_id\x18\x01 \x01(\tR\nexternalId\x1ag\n\x06\x41\x63tion\x12]\n\tresources\x18\x01 \x03(\x0b\x32?.indykite.authorization.v1beta1.WhatAuthorizedResponse.ResourceR\tresources\x1a\xf5\x01\n\x0cResourceType\x12j\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32P.indykite.authorization.v1beta1.WhatAuthorizedResponse.ResourceType.ActionsEntryR\x07\x61\x63tions\x1ay\n\x0c\x41\x63tionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12S\n\x05value\x18\x02 \x01(\x0b\x32=.indykite.authorization.v1beta1.WhatAuthorizedResponse.ActionR\x05value:\x02\x38\x01\x1a\x81\x01\n\x0e\x44\x65\x63isionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12Y\n\x05value\x18\x02 \x01(\x0b\x32\x43.indykite.authorization.v1beta1.WhatAuthorizedResponse.ResourceTypeR\x05value:\x02\x38\x01\"\x82\x05\n\x14WhoAuthorizedRequest\x12g\n\tresources\x18\x01 \x03(\x0b\x32=.indykite.authorization.v1beta1.WhoAuthorizedRequest.ResourceB\n\xfa\x42\x07\x92\x01\x04\x08\x01\x10 R\tresources\x12\x99\x01\n\x0cinput_params\x18\x02 \x03(\x0b\x32\x45.indykite.authorization.v1beta1.WhoAuthorizedRequest.InputParamsEntryB/\xfa\x42,\x9a\x01)\x08\x00\x10\x14\"#r!\x10\x01\x18\x14\x32\x1b^(?:[a-zA-Z][a-zA-Z0-9]+)+$R\x0binputParams\x12\x43\n\x0bpolicy_tags\x18\x03 \x03(\tB\"\xfa\x42\x1f\x92\x01\x1c\x18\x01\"\x16r\x14\x10\x01\x18\x14\x32\x0e^[a-zA-Z0-9]+$(\x01R\npolicyTags\x1a\xb3\x01\n\x08Resource\x12*\n\x0b\x65xternal_id\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x02\x18\x32R\nexternalId\x12\x31\n\x04type\x18\x02 \x01(\tB\x1d\xfa\x42\x1ar\x18\x10\x02\x18\x32\x32\x12^(?:[A-Z][a-z]+)+$R\x04type\x12H\n\x07\x61\x63tions\x18\x03 \x03(\tB.\xfa\x42+\x92\x01(\x08\x01\x10\x05\" r\x1e\x10\x02\x18\x32\x32\x18^[a-zA-Z0-9.:_\\-\\/]{2,}$(\x01R\x07\x61\x63tions\x1aj\n\x10InputParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12@\n\x05value\x18\x02 \x01(\x0b\x32*.indykite.authorization.v1beta1.InputParamR\x05value:\x02\x38\x01\"\xbe\x07\n\x15WhoAuthorizedResponse\x12?\n\rdecision_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x64\x65\x63isionTime\x12\x62\n\tdecisions\x18\x02 \x03(\x0b\x32\x44.indykite.authorization.v1beta1.WhoAuthorizedResponse.DecisionsEntryR\tdecisions\x1a*\n\x07Subject\x12\x1f\n\x0b\x65xternal_id\x18\x01 \x01(\tR\nexternalId\x1a\x63\n\x06\x41\x63tion\x12Y\n\x08subjects\x18\x01 \x03(\x0b\x32=.indykite.authorization.v1beta1.WhoAuthorizedResponse.SubjectR\x08subjects\x1a\xeb\x01\n\x08Resource\x12\x65\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32K.indykite.authorization.v1beta1.WhoAuthorizedResponse.Resource.ActionsEntryR\x07\x61\x63tions\x1ax\n\x0c\x41\x63tionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12R\n\x05value\x18\x02 \x01(\x0b\x32<.indykite.authorization.v1beta1.WhoAuthorizedResponse.ActionR\x05value:\x02\x38\x01\x1a\xfd\x01\n\x0cResourceType\x12o\n\tresources\x18\x01 \x03(\x0b\x32Q.indykite.authorization.v1beta1.WhoAuthorizedResponse.ResourceType.ResourcesEntryR\tresources\x1a|\n\x0eResourcesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12T\n\x05value\x18\x02 \x01(\x0b\x32>.indykite.authorization.v1beta1.WhoAuthorizedResponse.ResourceR\x05value:\x02\x38\x01\x1a\x80\x01\n\x0e\x44\x65\x63isionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12X\n\x05value\x18\x02 \x01(\x0b\x32\x42.indykite.authorization.v1beta1.WhoAuthorizedResponse.ResourceTypeR\x05value:\x02\x38\x01\x32\x8c\x03\n\x10\x41uthorizationAPI\x12y\n\x0cIsAuthorized\x12\x33.indykite.authorization.v1beta1.IsAuthorizedRequest\x1a\x34.indykite.authorization.v1beta1.IsAuthorizedResponse\x12\x7f\n\x0eWhatAuthorized\x12\x35.indykite.authorization.v1beta1.WhatAuthorizedRequest\x1a\x36.indykite.authorization.v1beta1.WhatAuthorizedResponse\x12|\n\rWhoAuthorized\x12\x34.indykite.authorization.v1beta1.WhoAuthorizedRequest\x1a\x35.indykite.authorization.v1beta1.WhoAuthorizedResponseB\xd9\x01\n\"com.indykite.authorization.v1beta1B\x19\x41uthorizationServiceProtoP\x01\xa2\x02\x03IAX\xaa\x02\x1eIndykite.Authorization.V1beta1\xca\x02\x1eIndykite\\Authorization\\V1beta1\xe2\x02*Indykite\\Authorization\\V1beta1\\GPBMetadata\xea\x02 Indykite::Authorization::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'indykite.authorization.v1beta1.authorization_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.indykite.authorization.v1beta1B\031AuthorizationServiceProtoP\001\242\002\003IAX\252\002\036Indykite.Authorization.V1beta1\312\002\036Indykite\\Authorization\\V1beta1\342\002*Indykite\\Authorization\\V1beta1\\GPBMetadata\352\002 Indykite::Authorization::V1beta1'
  _globals['_ISAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['external_id']._loaded_options = None
  _globals['_ISAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['external_id']._serialized_options = b'\372B\006r\004\020\002\0302'
  _globals['_ISAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['type']._loaded_options = None
  _globals['_ISAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['type']._serialized_options = b'\372B\032r\030\020\002\03022\022^(?:[A-Z][a-z]+)+$'
  _globals['_ISAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['actions']._loaded_options = None
  _globals['_ISAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['actions']._serialized_options = b'\372B)\222\001&\010\001\020\005\" r\036\020\002\03022\030^[a-zA-Z0-9.:_\\-\\/]{2,}$'
  _globals['_ISAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._loaded_options = None
  _globals['_ISAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._serialized_options = b'8\001'
  _globals['_ISAUTHORIZEDREQUEST'].fields_by_name['subject']._loaded_options = None
  _globals['_ISAUTHORIZEDREQUEST'].fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_ISAUTHORIZEDREQUEST'].fields_by_name['resources']._loaded_options = None
  _globals['_ISAUTHORIZEDREQUEST'].fields_by_name['resources']._serialized_options = b'\372B\007\222\001\004\010\001\020 '
  _globals['_ISAUTHORIZEDREQUEST'].fields_by_name['input_params']._loaded_options = None
  _globals['_ISAUTHORIZEDREQUEST'].fields_by_name['input_params']._serialized_options = b'\372B,\232\001)\010\000\020\024\"#r!\020\001\030\0242\033^(?:[a-zA-Z][a-zA-Z0-9]+)+$'
  _globals['_ISAUTHORIZEDREQUEST'].fields_by_name['policy_tags']._loaded_options = None
  _globals['_ISAUTHORIZEDREQUEST'].fields_by_name['policy_tags']._serialized_options = b'\372B\037\222\001\034\030\001\"\026r\024\020\001\030\0242\016^[a-zA-Z0-9]+$(\001'
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCE_ACTIONSENTRY']._loaded_options = None
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCE_ACTIONSENTRY']._serialized_options = b'8\001'
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCETYPE_RESOURCESENTRY']._loaded_options = None
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCETYPE_RESOURCESENTRY']._serialized_options = b'8\001'
  _globals['_ISAUTHORIZEDRESPONSE_DECISIONSENTRY']._loaded_options = None
  _globals['_ISAUTHORIZEDRESPONSE_DECISIONSENTRY']._serialized_options = b'8\001'
  _globals['_WHATAUTHORIZEDREQUEST_RESOURCETYPE'].fields_by_name['type']._loaded_options = None
  _globals['_WHATAUTHORIZEDREQUEST_RESOURCETYPE'].fields_by_name['type']._serialized_options = b'\372B\032r\030\020\002\03022\022^(?:[A-Z][a-z]+)+$'
  _globals['_WHATAUTHORIZEDREQUEST_RESOURCETYPE'].fields_by_name['actions']._loaded_options = None
  _globals['_WHATAUTHORIZEDREQUEST_RESOURCETYPE'].fields_by_name['actions']._serialized_options = b'\372B+\222\001(\010\001\020\005\" r\036\020\002\03022\030^[a-zA-Z0-9.:_\\-\\/]{2,}$(\001'
  _globals['_WHATAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._loaded_options = None
  _globals['_WHATAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._serialized_options = b'8\001'
  _globals['_WHATAUTHORIZEDREQUEST'].fields_by_name['subject']._loaded_options = None
  _globals['_WHATAUTHORIZEDREQUEST'].fields_by_name['subject']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_WHATAUTHORIZEDREQUEST'].fields_by_name['resource_types']._loaded_options = None
  _globals['_WHATAUTHORIZEDREQUEST'].fields_by_name['resource_types']._serialized_options = b'\372B\007\222\001\004\010\001\020\n'
  _globals['_WHATAUTHORIZEDREQUEST'].fields_by_name['input_params']._loaded_options = None
  _globals['_WHATAUTHORIZEDREQUEST'].fields_by_name['input_params']._serialized_options = b'\372B,\232\001)\010\000\020\024\"#r!\020\001\030\0242\033^(?:[a-zA-Z][a-zA-Z0-9]+)+$'
  _globals['_WHATAUTHORIZEDREQUEST'].fields_by_name['policy_tags']._loaded_options = None
  _globals['_WHATAUTHORIZEDREQUEST'].fields_by_name['policy_tags']._serialized_options = b'\372B\037\222\001\034\030\001\"\026r\024\020\001\030\0242\016^[a-zA-Z0-9]+$(\001'
  _globals['_WHATAUTHORIZEDRESPONSE_RESOURCETYPE_ACTIONSENTRY']._loaded_options = None
  _globals['_WHATAUTHORIZEDRESPONSE_RESOURCETYPE_ACTIONSENTRY']._serialized_options = b'8\001'
  _globals['_WHATAUTHORIZEDRESPONSE_DECISIONSENTRY']._loaded_options = None
  _globals['_WHATAUTHORIZEDRESPONSE_DECISIONSENTRY']._serialized_options = b'8\001'
  _globals['_WHOAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['external_id']._loaded_options = None
  _globals['_WHOAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['external_id']._serialized_options = b'\372B\006r\004\020\002\0302'
  _globals['_WHOAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['type']._loaded_options = None
  _globals['_WHOAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['type']._serialized_options = b'\372B\032r\030\020\002\03022\022^(?:[A-Z][a-z]+)+$'
  _globals['_WHOAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['actions']._loaded_options = None
  _globals['_WHOAUTHORIZEDREQUEST_RESOURCE'].fields_by_name['actions']._serialized_options = b'\372B+\222\001(\010\001\020\005\" r\036\020\002\03022\030^[a-zA-Z0-9.:_\\-\\/]{2,}$(\001'
  _globals['_WHOAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._loaded_options = None
  _globals['_WHOAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._serialized_options = b'8\001'
  _globals['_WHOAUTHORIZEDREQUEST'].fields_by_name['resources']._loaded_options = None
  _globals['_WHOAUTHORIZEDREQUEST'].fields_by_name['resources']._serialized_options = b'\372B\007\222\001\004\010\001\020 '
  _globals['_WHOAUTHORIZEDREQUEST'].fields_by_name['input_params']._loaded_options = None
  _globals['_WHOAUTHORIZEDREQUEST'].fields_by_name['input_params']._serialized_options = b'\372B,\232\001)\010\000\020\024\"#r!\020\001\030\0242\033^(?:[a-zA-Z][a-zA-Z0-9]+)+$'
  _globals['_WHOAUTHORIZEDREQUEST'].fields_by_name['policy_tags']._loaded_options = None
  _globals['_WHOAUTHORIZEDREQUEST'].fields_by_name['policy_tags']._serialized_options = b'\372B\037\222\001\034\030\001\"\026r\024\020\001\030\0242\016^[a-zA-Z0-9]+$(\001'
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCE_ACTIONSENTRY']._loaded_options = None
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCE_ACTIONSENTRY']._serialized_options = b'8\001'
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCETYPE_RESOURCESENTRY']._loaded_options = None
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCETYPE_RESOURCESENTRY']._serialized_options = b'8\001'
  _globals['_WHOAUTHORIZEDRESPONSE_DECISIONSENTRY']._loaded_options = None
  _globals['_WHOAUTHORIZEDRESPONSE_DECISIONSENTRY']._serialized_options = b'8\001'
  _globals['_ISAUTHORIZEDREQUEST']._serialized_start=197
  _globals['_ISAUTHORIZEDREQUEST']._serialized_end=911
  _globals['_ISAUTHORIZEDREQUEST_RESOURCE']._serialized_start=626
  _globals['_ISAUTHORIZEDREQUEST_RESOURCE']._serialized_end=803
  _globals['_ISAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._serialized_start=805
  _globals['_ISAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._serialized_end=911
  _globals['_ISAUTHORIZEDRESPONSE']._serialized_start=914
  _globals['_ISAUTHORIZEDRESPONSE']._serialized_end=1751
  _globals['_ISAUTHORIZEDRESPONSE_ACTION']._serialized_start=1102
  _globals['_ISAUTHORIZEDRESPONSE_ACTION']._serialized_end=1132
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCE']._serialized_start=1135
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCE']._serialized_end=1368
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCE_ACTIONSENTRY']._serialized_start=1249
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCE_ACTIONSENTRY']._serialized_end=1368
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCETYPE']._serialized_start=1371
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCETYPE']._serialized_end=1622
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCETYPE_RESOURCESENTRY']._serialized_start=1499
  _globals['_ISAUTHORIZEDRESPONSE_RESOURCETYPE_RESOURCESENTRY']._serialized_end=1622
  _globals['_ISAUTHORIZEDRESPONSE_DECISIONSENTRY']._serialized_start=1624
  _globals['_ISAUTHORIZEDRESPONSE_DECISIONSENTRY']._serialized_end=1751
  _globals['_WHATAUTHORIZEDREQUEST']._serialized_start=1754
  _globals['_WHATAUTHORIZEDREQUEST']._serialized_end=2449
  _globals['_WHATAUTHORIZEDREQUEST_RESOURCETYPE']._serialized_start=2202
  _globals['_WHATAUTHORIZEDREQUEST_RESOURCETYPE']._serialized_end=2341
  _globals['_WHATAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._serialized_start=805
  _globals['_WHATAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._serialized_end=911
  _globals['_WHATAUTHORIZEDRESPONSE']._serialized_start=2452
  _globals['_WHATAUTHORIZEDRESPONSE']._serialized_end=3172
  _globals['_WHATAUTHORIZEDRESPONSE_RESOURCE']._serialized_start=2644
  _globals['_WHATAUTHORIZEDRESPONSE_RESOURCE']._serialized_end=2687
  _globals['_WHATAUTHORIZEDRESPONSE_ACTION']._serialized_start=2689
  _globals['_WHATAUTHORIZEDRESPONSE_ACTION']._serialized_end=2792
  _globals['_WHATAUTHORIZEDRESPONSE_RESOURCETYPE']._serialized_start=2795
  _globals['_WHATAUTHORIZEDRESPONSE_RESOURCETYPE']._serialized_end=3040
  _globals['_WHATAUTHORIZEDRESPONSE_RESOURCETYPE_ACTIONSENTRY']._serialized_start=2919
  _globals['_WHATAUTHORIZEDRESPONSE_RESOURCETYPE_ACTIONSENTRY']._serialized_end=3040
  _globals['_WHATAUTHORIZEDRESPONSE_DECISIONSENTRY']._serialized_start=3043
  _globals['_WHATAUTHORIZEDRESPONSE_DECISIONSENTRY']._serialized_end=3172
  _globals['_WHOAUTHORIZEDREQUEST']._serialized_start=3175
  _globals['_WHOAUTHORIZEDREQUEST']._serialized_end=3817
  _globals['_WHOAUTHORIZEDREQUEST_RESOURCE']._serialized_start=3530
  _globals['_WHOAUTHORIZEDREQUEST_RESOURCE']._serialized_end=3709
  _globals['_WHOAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._serialized_start=805
  _globals['_WHOAUTHORIZEDREQUEST_INPUTPARAMSENTRY']._serialized_end=911
  _globals['_WHOAUTHORIZEDRESPONSE']._serialized_start=3820
  _globals['_WHOAUTHORIZEDRESPONSE']._serialized_end=4778
  _globals['_WHOAUTHORIZEDRESPONSE_SUBJECT']._serialized_start=4010
  _globals['_WHOAUTHORIZEDRESPONSE_SUBJECT']._serialized_end=4052
  _globals['_WHOAUTHORIZEDRESPONSE_ACTION']._serialized_start=4054
  _globals['_WHOAUTHORIZEDRESPONSE_ACTION']._serialized_end=4153
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCE']._serialized_start=4156
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCE']._serialized_end=4391
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCE_ACTIONSENTRY']._serialized_start=4271
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCE_ACTIONSENTRY']._serialized_end=4391
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCETYPE']._serialized_start=4394
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCETYPE']._serialized_end=4647
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCETYPE_RESOURCESENTRY']._serialized_start=4523
  _globals['_WHOAUTHORIZEDRESPONSE_RESOURCETYPE_RESOURCESENTRY']._serialized_end=4647
  _globals['_WHOAUTHORIZEDRESPONSE_DECISIONSENTRY']._serialized_start=4650
  _globals['_WHOAUTHORIZEDRESPONSE_DECISIONSENTRY']._serialized_end=4778
  _globals['_AUTHORIZATIONAPI']._serialized_start=4781
  _globals['_AUTHORIZATIONAPI']._serialized_end=5177
# @@protoc_insertion_point(module_scope)
