#!/bin/sh

release=$(date +%y%m%d%H%M)
git archive --format tgz --prefix=fb-faker-0.1/ HEAD > /usr/src/redhat/SOURCES/fb-faker-0.1.tar.gz
rpmbuild -bs --define="_release $release" faker.spec
rpmbuild -bb --define="_release $release" faker.spec
