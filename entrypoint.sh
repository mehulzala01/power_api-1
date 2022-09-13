mkdir ./logs
touch ./logs/gunicorn.log
touch ./logs/gunicorn-access.log
tail -n 0 -f ./logs/gunicorn*.log &

exec gunicorn power_api.wsgi:application \
    --name power_api \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --log-level=info \
    --limit-request-line 0 \
    --log-file=./logs/gunicorn.log \
    --access-logfile=./logs/gunicorn-access.log \
"$@"