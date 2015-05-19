#!/usr/bin/env python

# Copyright (c) 2001-2014, Canal TP and/or its affiliates. All rights reserved.
#
# This file is part of Navitia,
#     the software to build cool stuff with public transport.
#
# Hope you'll enjoy and contribute to this project,
#     powered by Canal TP (www.canaltp.fr).
# Help us simplify mobility and open public transport:
#     a non ending quest to the responsive locomotion way of traveling!
#
# LICENCE: This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Stay tuned using
# twitter @navitia
# IRC #navitia on freenode
# https://groups.google.com/d/forum/navitia
# www.navitia.io

from distutils.core import setup, Command
from setuptools import find_packages
from distutils.spawn import find_executable
import glob
import os

protoc = find_executable("protoc")


class BuildPbfCommand(Command):
    description = "build protocol buffer files"
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('{protoc} -Inavitia-proto --python_out=stat_persistor navitia-proto/*.proto'.format(protoc=protoc))


setup(name='stat_persistor',
        version='0.01.0',
        description="This service persist statistics",
        author='CanalTP',
        author_email='krishna.adhikari@canaltp.fr',
        url='www.navitia.io',
        packages=find_packages(),
        scripts=['stat_persist.py'],
        data_files=[
            ('/usr/share/stat_persistor/migrations', ['migrations/alembic.ini',
                                                     'migrations/alembic/env.py',
                                                     'migrations/alembic/script.py.mako']),
            ('/usr/share/stat_persistor/migrations/versions', glob.glob('migrations/alembic/versions/*.py')),
            ('/usr/bin', ['stat_persist.py'])
        ],
        cmdclass={'build_pbf': BuildPbfCommand},
)
