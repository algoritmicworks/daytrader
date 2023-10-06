tar -cvzf daytrader.tar.gz ./*
python3 setup.py sdist
twine upload dist/*
rm daytrader.tar.gz