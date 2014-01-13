{
  "targets": [
    {
      "target_name": "archive",
      "libraries": ["<!@(pkg-config libarchive --libs)"],
      "include_dirs": [
        "<!@(pkg-config libarchive --cflags-only-I | sed s/-I//g)",
        "<!(node -e \"require('nan')\")"
      ],
      "sources": [ "src/addon.cc", "src/archive_entry_wrapper.cc", "src/archive_reader.cc", "src/helpers.cc" ]
    }
  ]
}
