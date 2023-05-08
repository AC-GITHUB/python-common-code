# -*- coding: <utf-8> -*-
import osgeo.ogr as ogr
import osgeo.gdal as gdal
import os


class GeoUtils(object):

    def __init__(self):
        super()

    def read_shp(self, file):
        'open'
        ds = ogr.Open(file, False)
        layer = ds.GetLayer(0)

        lydefn = layer.GetLayerDefn()
        spatialref = layer.GetSpatialRef()

        geomtype = lydefn.GetGeomType()
        fieldlist = []
        for i in range(lydefn.GetFieldCount()):
            fddefn = lydefn.GetFieldDefn(i)
            fieldlist.append(fddefn.GetName())
            '''
            fddict = {
                'name': fddefn.GetName(),
                'type': fddefn.GetType(),
                'width': fddefn.GetWidth(),
                'decimal': fddefn.GetPrecision()
            }
            fieldlist += [fddict]
            '''

        geomlist = []
        reclist = []

        feature = layer.GetNextFeature()
        while feature is not None:
            geom = feature.GetGeometryRef()
            geomlist += [geom.ExportToJson()]
            '''
            rec = {}
            for fd in fieldlist:
                rec[fd['name']] = feature.GetField(fd['name'])
            reclist += [rec]
            '''
            feature = layer.GetNextFeature()

        ds.Destroy()
        return (spatialref, geomtype, geomlist, fieldlist, reclist)

    def write_shp(self, file, data):
        gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "YES")
        gdal.SetConfigOption("SHAPE_ENCODING", "UTF-8")
        spatialref, geomtype, geomlist, fieldlist, reclist = data

        driver = ogr.GetDriverByName("ESRI Shapefile")
        if os.access(file, os.F_OK):
            driver.DeleteDataSource(file)
        ds = driver.CreateDataSource(file)

        layer = ds.CreateLayer(file[:-4], srs=spatialref, geom_type=geomtype)

        for fd in fieldlist:
            field = ogr.FieldDefn(fd['name'], fd['type'])
            if fd.has_key('width'):
                field.SetWidth(fd['width'])
            if fd.has_key('decimal'):
                field.SetPrecision(fd['decimal'])
            layer.CreateField(field)

        for i in range(len(reclist)):
            geom = ogr.CreateGeometryFromWkt(geomlist[i])
            feat = ogr.Feature(layer.GetLayerDefn())
            feat.SetGeometry(geom)
            for fd in fieldlist:

                feat.SetField(fd['name'], reclist[i][fd['name']])
            layer.CreateFeature(feat)

        ds.Destroy()


if __name__ == "__main__":
    shp = GeoUtils()
    data = shp.read_shp(
        r'/Users/acc/开发学习资料/雷电/台州暴雨/linhai/桃渚变/桃渚变_dxf_Polyline.shp')
    print(data)
