# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_synthesizer.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aresponse_synthesizer.proto\"(\n\x16getFinalAnswerResponse\x12\x0e\n\x06\x41nswer\x18\x01 \x01(\t\"\x0c\n\nFinalEmpty\"\x9b\x01\n\x0b\x46inalParams\x12\x0c\n\x04rs_k\x18\x01 \x01(\x05\x12\x10\n\x08rs_top_k\x18\x02 \x01(\x05\x12\x16\n\x0ers_temperature\x18\x03 \x01(\x02\x12\x19\n\x11rs_max_new_tokens\x18\x04 \x01(\x05\x12\x1a\n\x12rs_score_threshold\x18\x05 \x01(\x02\x12\x1d\n\x15rs_repetition_penalty\x18\x06 \x01(\x02\"\xbb\x01\n\x15getFinalAnswerRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x1c\n\x06params\x18\x02 \x01(\x0b\x32\x0c.FinalParams\x12\x34\n\x07qaPairs\x18\x03 \x03(\x0b\x32#.getFinalAnswerRequest.QaPairsEntry\x12\x0f\n\x07Sources\x18\x04 \x01(\x0c\x1a.\n\x0cQaPairsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x9b\x01\n\x13ResponseSynthesizer\x12H\n\x11summarizeResponse\x12\x16.getFinalAnswerRequest\x1a\x17.getFinalAnswerResponse\"\x00\x30\x01\x12:\n\x1bgetSynthesizerDefaultParams\x12\x0b.FinalEmpty\x1a\x0c.FinalParams\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'response_synthesizer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETFINALANSWERREQUEST_QAPAIRSENTRY']._options = None
  _globals['_GETFINALANSWERREQUEST_QAPAIRSENTRY']._serialized_options = b'8\001'
  _globals['_GETFINALANSWERRESPONSE']._serialized_start=30
  _globals['_GETFINALANSWERRESPONSE']._serialized_end=70
  _globals['_FINALEMPTY']._serialized_start=72
  _globals['_FINALEMPTY']._serialized_end=84
  _globals['_FINALPARAMS']._serialized_start=87
  _globals['_FINALPARAMS']._serialized_end=242
  _globals['_GETFINALANSWERREQUEST']._serialized_start=245
  _globals['_GETFINALANSWERREQUEST']._serialized_end=432
  _globals['_GETFINALANSWERREQUEST_QAPAIRSENTRY']._serialized_start=386
  _globals['_GETFINALANSWERREQUEST_QAPAIRSENTRY']._serialized_end=432
  _globals['_RESPONSESYNTHESIZER']._serialized_start=435
  _globals['_RESPONSESYNTHESIZER']._serialized_end=590
# @@protoc_insertion_point(module_scope)
