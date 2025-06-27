
for f in /home/mediacms.io/sample/*.mp4; do
  echo -e "$f" | python cli.py upload-media
done