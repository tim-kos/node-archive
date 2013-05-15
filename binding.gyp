{
  "targets": [
    {
      "target_name": "archive",
      "include_dirs": [
        "<!@(pkg-config libarchive --cflags-only-I | sed s/-I//g)"
      ],
      "sources": [ "src/addon.cc", "src/archive_entry_wrapper.cc", "src/archive_reader.cc", "src/helpers.cc" ]
    }
  ]
}
