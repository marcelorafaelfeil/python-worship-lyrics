#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/Worship Lyrics.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/Worship Lyrics.dmg" && rm "dist/Worship Lyrics.dmg"
create-dmg \
  --volname "Worship Lyrics" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "Worship Lyrics.app" 175 120 \
  --hide-extension "Worship Lyrics.app" \
  --app-drop-link 425 120 \
  "dist/Worship Lyrics.dmg" \
  "dist/dmg/"