from netCDF4 import Dataset
import matplotlib as mpl

mpl.use('TkAgg')
import matplotlib.pyplot as plt
import os
from mpl_toolkits.basemap import Basemap, cm
import numpy as np


def lat_lon_reproj(nc_folder):
    os.chdir(nc_folder)
    full_direc = os.listdir()
    nc_files = [ii for ii in full_direc if ii.endswith('.nc')]
    data_file = nc_files[0]  # select .nc file
    print(nc_files[0]) # print file name

    # designate dataset
    in_file = Dataset(data_file, 'r')
    # print(in_file.variables.keys())
    var_names = [ii for ii in in_file.variables]
    var_name = var_names[0]

    lon = in_file.variables['lon'][:]
    lat = in_file.variables['lat'][:]

    # close file when finished
    in_file.close()
    in_file = None

    # create meshgrid filled with radian angles


    # latitude and longitude projection for plotting data on traditional lat/lon maps


    return lon, lat


def data_grab(nc_folder, nc_indx):
    os.chdir(nc_folder)
    full_direc = os.listdir()
    nc_files = [ii for ii in full_direc if ii.endswith('.nc')]
    data_file = nc_files[0]  # select .nc file

    # designate dataset
    in_file = Dataset(data_file, 'r')
    # print(in_file.variables.keys())
    var_names = [ii for ii in in_file.variables]

    # data info
    data = in_file.variables['ted_ele_eflux_atmo_hi'][:]
    data_units = in_file.variables['ted_ele_eflux_atmo_hi'].units
    # data_time_grab = in_file.variables['time']
    data_long_name = in_file.variables['ted_ele_eflux_atmo_hi'].long_name

    # close file when finished
    in_file.close()
    in_file = None

    os.chdir('../')
    # print test coordinates
    # print('{} N, {} W'.format(lat[318, 1849], abs(lon[318, 1849])))
    print(data, data_units, data_long_name)
    return data, data_units, data_long_name



nc_folder = '/Users/iluhaseredkin/Documents/netcdf4-python/'  # define folder where .nc files are located
lon, lat = lat_lon_reproj(nc_folder)

file_indx = 1  # be sure to pick the correct file. Make sure the file is not too big either,
# some of the bands create large files (stick to band 7-16)

data, data_units, data_long_name = data_grab(nc_folder, file_indx)
# main data grab from function above

data_bounds = np.where(data.data != 65535)
bbox = [np.min(lon[data_bounds]),
        np.min(lat[data_bounds]),
        np.max(lon[data_bounds]),
        np.max(lat[data_bounds])]  # set bounds for plotting

# figure routine for visualization
fig = plt.figure(figsize=(9, 4), dpi=200)

n_add = 0  # for zooming in and out
m = Basemap(llcrnrlon=bbox[0] - n_add, llcrnrlat=bbox[1] - n_add, urcrnrlon=bbox[2] + n_add, urcrnrlat=bbox[3] + n_add,
            resolution='i', projection='cyl')
m.fillcontinents(color='#d9b38c', lake_color='#bdd5d5', zorder=1)  # continent colors
m.drawmapboundary(fill_color='#bdd5d5', zorder=0)  # ocean color
m.drawcoastlines(linewidth=0.5)
m.drawcountries(linewidth=0.25)
m.drawstates(zorder=2)



map.hexbin(array(x), array(y), gridsize=20, mincnt=1, cmap='summer', norm=colors.LogNorm())

cb = map.colorbar(location='bottom', format='%d', label='# lightnings')

# m.pcolormesh(lon.data, lat.data, data, latlon=True, zorder=999)  # plotting actual LST data
parallels = np.linspace(bbox[1], bbox[3], 5.)
m.drawparallels(parallels, labels=[True, False, False, False], zorder=2, fontsize=8)
meridians = np.linspace(bbox[0], bbox[2], 5.)
m.drawmeridians(meridians, labels=[False, False, False, True], zorder=1, fontsize=8)
cb = m.colorbar()

data_units = ((data_units.replace('-', '^{-')).replace('1', '1}')).replace('2', '2}')
plt.rc('text', usetex=True)
cb.set_label(r'%s $ \left[ \nprm \right] $' % (var_name, data_units))
plt.title(' on '.format(data_long_name, data_time_grab))
plt.tight_layout()

plt.savefig('goes_16_data_demo.png', dpi=200, facecolor=[252 / 255, 252 / 255, 252 / 255])  # uncomment to save figure
plt.show()