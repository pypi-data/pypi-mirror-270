import os
import pkg_resources

def get_data_folder():
    return pkg_resources.resource_filename(__name__, '../data')

def get_pngs_folder():
    return pkg_resources.resource_filename(__name__, '../pngs')
