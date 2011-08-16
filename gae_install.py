#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import sys
import shutil
import StringIO

from os import path
from urllib import urlopen
from zipfile import ZipFile

GOOGLE_DW_URL = "http://code.google.com/intl/pt-BR/appengine/downloads.html"

def get_site_packages_path():
	from distutils.sysconfig import get_python_lib
	return get_python_lib()

def get_google_dw_page():
	handle = urlopen(GOOGLE_DW_URL)
	page_data = handle.read()
	handle.close()
	return page_data

def get_latest_gae_dw_link(dw_page):
	match = re.search("http://.+/google_appengine_1\.5\.2\.zip", dw_page)
	return match.group(0)

def get_gae_version(filename):
	return tuple(filename.split("_")[-1].split(".")[:-1])

def download_gae(url):
	handle = urlopen(url)
	data = handle.read()
	handle.close()
	return data

def unzip_stream(stream, dpath):
	if not path.exists(dpath):
		os.mkdir(dpath)

	file = StringIO.StringIO()
	file.write(stream)
	zip_file = ZipFile(file)
	zip_file.extractall(dpath)
	return path.join(dpath, "/google_appengine/")

def check_permissions():
	if not os.access("/opt/", os.W_OK):
		print "Your user must have write permissions for folder '/opt/' in order to proceed."
		print " - exit -"
		exit(0)

def install_gae_from_path(unziped_gae_path):
	pass

def main(args):
	check_permissions()
	google_dw_page = get_google_dw_page()
	gae_dw_link = get_latest_gae_dw_link(google_dw_page)
	gae_pk_filename = path.basename(gae_dw_link)
	gae_version = get_gae_version(gae_pk_filename)
	gae_package = download_gae(gae_dw_link)
	unziped_gae_path = unzip_stream(gae_package, "/opt/")
	install_gae_from_path(unziped_gae_path)
	print "(Python) Google App Engine %s installed." % '.'.join(gae_version)


if __name__ == "__main__":
	main(sys.argv[1:])
