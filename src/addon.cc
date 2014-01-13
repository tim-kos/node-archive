// Copyright 2012 Karl Skomski MIT

#include "archive_reader.h"
#include "nan.h"

using namespace v8;

void InitAll(Handle<Object> exports) {
  nodearchive::ArchiveReader::Init(target);
  nodearchive::ArchiveEntryWrapper::Init(target);
}

NODE_MODULE(addon, InitAll)
