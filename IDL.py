from netCDF4 import Dataset
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pylab

# import urllib.request

# координаты станций
st_lat = 52.971851
st_long = 158.247903
# st_lat = 62.38333
# st_long = -145.1333

def read():

    nc_folder = '/Users/iluhaseredkin/Documents/netcdf4-python/'  # define folder where .nc files are located
    os.chdir(nc_folder)
    full_direc = os.listdir()
    nc_files = [ii for ii in full_direc if ii.endswith('.nc')]
    print(nc_files)
    data_file = nc_files[3]  # select .nc file

    # url = 'https://satdat.ngdc.noaa.gov/sem/poes/data/processed/ngdc/uncorrected/full/2021/metop01/poes_m01_20210103_proc.nc'
    # data_file = urllib.request.urlretrieve(url)

    in_file = Dataset(data_file, 'r')
    in_file.set_auto_mask(False)
    time = in_file.variables['time'][:]
    lon = in_file.variables['lon'][:]
    lat = in_file.variables['lat'][:]
    lon = np.where(lon > 180, lon-360, lon)
    mep_e_90_flux_40kev = in_file.variables['mep_ele_tel90_flux_e1'][:]
    mep_e_0_flux_40kev = in_file.variables['mep_ele_tel0_flux_e1'][:]
    ted_e_1_20kev_120km = in_file.variables['ted_ele_eflux_atmo_hi'][:]
    ted_e_50ev_1kev_120km = in_file.variables['ted_ele_eflux_atmo_low'][:]
    ted_e_50ev_20kev_120km = in_file.variables['ted_ele_eflux_atmo_total'][:]
    ted_e_0_844ev = in_file.variables['ted_ele_tel0_flux_8'][:]
    ted_e_30_844ev = in_file.variables['ted_ele_tel30_flux_8'][:]

    data = np.column_stack((time, lon, lat, mep_e_90_flux_40kev, mep_e_0_flux_40kev, ted_e_1_20kev_120km, ted_e_50ev_1kev_120km, ted_e_50ev_20kev_120km, ted_e_0_844ev, ted_e_30_844ev))

    # print(data)
    # np.savetxt("filefromNetCDF.csv", data, delimiter=",")
    # data = loadtxt("myfile.txt")

    return data

def plots(data, ind_min):

    lon = data[:,1]
    lat = data[:,2]

    if lon[ind_min] > st_long:
        tr1 = data[ind_min + 2400:ind_min + 3600]
        tr2 = data[ind_min - 600:ind_min + 600]
        min_1 = ind_min + 3000
        min_2 = ind_min
    else:
        tr1 = data[ind_min - 600:ind_min + 600]
        tr2 = data[ind_min - 3600:ind_min - 2400]
        min_1 = ind_min
        min_2 = ind_min - 3000

    plt.figure(figsize=(10, 10))

    plt.subplot(2, 1, 1)
    plt.title("Карта")  # заголовок
    m = Basemap(projection='cyl', lon_0=0, resolution='c')
    m.drawcoastlines()
    m.fillcontinents(color='sienna', lake_color='aqua')
    m.drawmapboundary(fill_color='lightsteelblue')
    m.scatter(tr1[:, 1], tr1[:, 2], 1, marker='o', color='blue', latlon=False, zorder=10)
    m.scatter(tr2[:, 1], tr2[:, 2], 1, marker='o', color='blue', latlon=False, zorder=10)
    m.scatter(st_long, st_lat, 1, marker='o', color='white', latlon=False, zorder=100)

    plt.subplot(6, 2, 11)
    # plt.title("Орбита 1")  # заголовок
    plt.xlabel("latitude")  # ось абсцисс
    plt.ylabel("energy")  # ось ординат
    plt.plot(tr1[:,2], tr1[:,3])  # построение графика
    plt.plot(tr1[:,2], tr1[:,4])  # построение графика
    plt.subplot(6, 2, 12)
    # plt.title("Орбита 2")  # заголовок
    plt.xlabel("latitude")  # ось абсцисс
    plt.ylabel("energy")  # ось ординат
    plt.plot(tr2[:,2], tr2[:,3])  # построение графика
    plt.plot(tr2[:,2], tr2[:,4])  # построение графика

    ax = plt.subplot(6, 2, 7)
    ax.set_yscale('log')
    plt.title("Орбита 1")  # заголовок
    # plt.xlabel("latitude")  # ось абсцисс
    plt.ylabel("energy")  # ось ординат
    plt.plot(tr1[:, 2], tr1[:, 5])  # построение графика
    plt.plot(tr1[:, 2], tr1[:, 6])  # построение графика
    ax = plt.subplot(6, 2, 8)
    ax.set_yscale('log')
    plt.title("Орбита 2")  # заголовок
    # plt.xlabel("latitude")  # ось абсцисс
    plt.ylabel("energy")  # ось ординат
    plt.plot(tr2[:, 2], tr2[:, 5])  # построение графика
    plt.plot(tr2[:, 2], tr2[:, 6])  # построение графика

    ax = plt.subplot(6, 2, 9)
    ax.set_yscale('log')
    # plt.title("Орбита 1")  # заголовок
    # plt.xlabel("latitude")  # ось абсцисс
    plt.ylabel("energy")  # ось ординат
    plt.plot(tr1[:, 2], tr1[:, 7])  # построение графика
    plt.plot(tr1[:, 2], tr1[:, 8])  # построение графика
    ax = plt.subplot(6, 2, 10)
    ax.set_yscale('log')
    # plt.title("Орбита 2")  # заголовок
    # plt.xlabel("latitude")  # ось абсцисс
    plt.ylabel("energy")  # ось ординат
    plt.plot(tr2[:, 2], tr2[:, 7])  # построение графика
    plt.plot(tr2[:, 2], tr2[:, 8])  # построение графика

    plt.show()
    # pylab.show()

def find(data):

    # rad - радиус сферы (Земли)
    rad = 6372795
    lon = data[:,1]
    lat = data[:,2]

    # # координаты точек
    llat = st_lat
    llong = st_long

    # в радианах
    lat1 = np.array(lat * np.pi / 180.)
    lat2 = llat * np.pi / 180.

    long1 = np.array(lon * np.pi / 180.)
    long2 = llong * np.pi / 180.

    # вычисления мин. дистанции
    delta = long2 - long1
    y = np.sqrt(np.power(np.cos(lat2) * np.sin(delta), 2) + np.power(np.cos(lat1) * np.sin(lat2) - np.sin(lat1) * np.cos(lat2) * np.cos(delta), 2))
    x = np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(delta)
    distance = np.arctan2(y, x) * rad/1000
    min = np.min(distance)
    ind_min = np.argmin(distance)
    # np.savetxt("distance.csv", distance, delimiter=",")
    # print(min)
    # print(data[ind_min])

    return ind_min

def main():
    data = read()
    ind_min = find(data)
    plots(data, ind_min)

if __name__ == '__main__':
    main()