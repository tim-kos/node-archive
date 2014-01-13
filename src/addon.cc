// Copyright 2012 Karl Skomski MIT

#include "archive_reader.h"
#include "nan.h"

using namespace v8;

void InitAll(Handle<Object> exports) {
  nodearchive::ArchiveReader::Init(exports);
  nodearchive::ArchiveEntryWrapper::Init(exports);
}

NODE_MODULE(addon, InitAll)
