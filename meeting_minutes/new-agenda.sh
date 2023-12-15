cat AGENDA-TEMPLATE.md | sed "s/__DATE__/$1/g" | sed "s/__TIME__/$2/g" >| $1.md
git checkout -b $1
git add .
git commit -S -m "new agenda created for $1"
