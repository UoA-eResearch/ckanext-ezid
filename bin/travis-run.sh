#!/bin/sh -e

echo "NO_START=0\nJETTY_HOST=127.0.0.1\nJETTY_PORT=8983\nJAVA_HOME=$JAVA_HOME" | sudo tee /etc/default/jetty
sudo cp ckan/ckan/config/solr/schema.xml /etc/solr/conf/schema.xml
sudo service jetty restart
sed -i "s/USERNAME/$USERNAME/g" subdir/test.ini
sed -i "s/PASSWORD/$PASSWORD/g" subdir/test.ini
sed -i "s/NAMESPACE/$NAMESPACE/g" subdir/test.ini
nosetests --nologcapture --with-pylons=subdir/test.ini --with-coverage --cover-package=ckanext.ezid --cover-inclusive --cover-erase --cover-tests