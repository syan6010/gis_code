require 'csv'

write_parameters = { write_headers: true, headers: ["點名", "N (m)", "E (m)", "h (m) 橢球高", "經度", "緯度", "h (m) 橢球高", "計算後N", "計算後E", "是否有誤"] }


def dms2rad dms
    degrees = dms[0]
    minutes = dms[1]
    seconds = dms[2]
    dd = Float(degrees) + Float(minutes)/60 + Float(seconds)/(60*60);
    rad = dd * Math::PI / 180 
end

class Geo_coord
    attr_reader :e_97, :n_97

    def initialize lon, lat
        @lon = dms2rad(lon)
        @lat = dms2rad(lat)
        @e_97, @n_97 = to_tm2_97
    end

    def to_tm2_97
        a = 6378137.0
        b = 6356752.314245
        long0 = dms2rad([121, 0, 0])
        k0 = 0.9999
        dx = 250000
    
        e = (1-b**2/a**2)**0.5
        e2 = e**2/(1-e**2)
        n = (a-b)/(a+b)
        nu = a/(1-(e**2)*(Math.sin(@lat)**2))**0.5
        p = @lon-long0
    
        a_n = a*(1 - n + (5/4.0)*(n**2 - n**3) + (81/64.0)*(n**4  - n**5))
        b_n = (3*a*n/2.0)*(1 - n + (7/8.0)*(n**2 - n**3) + (55/64.0)*(n**4 - n**5))
        c_n = (15*a*(n**2)/16.0)*(1 - n + (3/4.0)*(n**2 - n**3))
        d_n = (35*a*(n**3)/48.0)*(1 - n + (11/16.0)*(n**2 - n**3))
        e_n = (315*a*(n**4)/51.0)*(1 - n)
    
        s = a_n*@lat - b_n*Math.sin(2*@lat) + c_n*Math.sin(4*@lat) - d_n*Math.sin(6*@lat) + e_n*Math.sin(8*@lat)
    
        k1 = s*k0
        k2 = k0*nu*Math.sin(2*@lat)/4.0
        k3 = (k0*nu*Math.sin(@lat)*(Math.cos(@lat)**3)/24.0) * (5 - Math.tan(@lat)**2 + 9*e2*(Math.cos(@lat)**2) + 4*(e2**2)*(Math.cos(@lat)**4))
    
        y_97 = k1 + k2*(p**2) + k3*(p**4)
    
        k4 = k0*nu*Math.cos(@lat)
        k5 = (k0*nu*(Math.cos(@lat)**3)/6.0) * (1 - Math.tan(@lat)**2 + e2*(Math.cos(@lat)**2))
    
        x_97 = k4*p + k5*(p**3) + dx
        return x_97.round(3), y_97.round(3)
    end
end



CSV.open("new_geo2tm2.csv", 'w+', write_parameters) do |new_csv|
    CSV.foreach('geo2tm2.csv', "r:UTF-8", headers: true) do |row|
        lon_d, lon_m, lon_s = row[4].split('-')
        lat_d, lat_m, lat_s = row[5].split('-')
        lon = [lon_d, lon_m, lon_s]
        lat = [lat_d, lat_m, lat_s]
        point = Geo_coord.new(lon, lat)

        wrong = (point.n_97.to_f == row[1].to_f and point.e_97.to_f == row[2].to_f) ? false : true
        
        new_row = row << ["計算後N", point.n_97] << ["計算後E", point.e_97] << ["是否有誤", wrong] 
        
        new_csv << new_row 
    end
end


