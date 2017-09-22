set -x
curl -XPOST -H 'Accept:application/yml' http://0.0.0.0:5000
echo ''

curl -XPOST -H 'Accept:application/json' http://0.0.0.0:5000
echo ''

curl -XPOST  http://0.0.0.0:5000
