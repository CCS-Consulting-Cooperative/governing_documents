set -euo pipefail

help () {
    echo 'Usage: ./new-agenda.sh <date> <time>'
    echo 'Example: ./new-agenda.sh "2024-01-23" "14:00"'
}
# Check args
if [ "$#" -ne 2 ]; then
   echo "Usage: $0 <YYYY-MM-DD> <HH:MM>" >&2
   help
   exit 1
fi

# Validate date format
if ! [[ $1 =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
   echo "Error: Date must be YYYY-MM-DD format" >&2
   help
   exit 1
fi

# Validate time format
if ! [[ $2 =~ ^[0-9]{2}:[0-9]{2}$ ]]; then
   echo "Error: Time must be HH:MM format" >&2
   help
   exit 1
fi

YEAR=${1:0:4}
DIR="$YEAR/"
mkdir -p $DIR

# Check directory exists
if [ ! -d "$DIR" ]; then
   echo "Error: Directory $DIR not found" >&2
   exit 1
fi
pushd $DIR
cat ../AGENDA-TEMPLATE.md | sed "s/__DATE__/$1/g" | sed "s/__TIME__/$2/g" >| $1.md
popd
git checkout -b $1
git add .
git commit -S -m "new agenda created for $1"

