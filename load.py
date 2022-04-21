;Coordinates
vID=ncdf_varid(fID,'alt') & ncdf_varget,fID,vID,salt
vID=ncdf_varid(fID,'lat') & ncdf_varget,fID,vID,slat
vID=ncdf_varid(fID,'lon') & ncdf_varget,fID,vID,slon
sg=fltarr(narr,5)
sg[*,0]=slat[*] & sg[*,1]=slon[*] & sg[*,2]=salt[*]

;Fluxes
vID=ncdf_varid(fID,'mep_pro_tel0_flux_p1') & ncdf_varget,fID,vID,p0p1 ;p 39 keV [#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel0_flux_p2') & ncdf_varget,fID,vID,p0p2 ;p 115 keV[#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel0_flux_p3') & ncdf_varget,fID,vID,p0p3 ;p 332 keV[#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel0_flux_p4') & ncdf_varget,fID,vID,p0p4 ;p 1105 keV[#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel0_flux_p5') & ncdf_varget,fID,vID,p0p5 ;p 2723 keV[#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel0_flux_p6') & ncdf_varget,fID,vID,p0p6 ;p 6174 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_pro_tel90_flux_p1') & ncdf_varget,fID,vID,p9p1 ;p 39 keV [#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel90_flux_p2') & ncdf_varget,fID,vID,p9p2 ;p 115 keV[#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel90_flux_p3') & ncdf_varget,fID,vID,p9p3 ;p 332 keV[#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel90_flux_p4') & ncdf_varget,fID,vID,p9p4 ;p 1105 keV[#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel90_flux_p5') & ncdf_varget,fID,vID,p9p5 ;p 2723 keV[#/cm2-s-str-keV]
vID=ncdf_varid(fID,'mep_pro_tel90_flux_p6') & ncdf_varget,fID,vID,p9p6 ;p 6174 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_ele_tel0_flux_e1') & ncdf_varget,fID,vID,p0e1 ;e>40 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_ele_tel0_flux_e2') & ncdf_varget,fID,vID,p0e2 ;e>130 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_ele_tel0_flux_e3') & ncdf_varget,fID,vID,p0e3 ;e>287 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_ele_tel0_flux_e4') & ncdf_varget,fID,vID,p0e4 ;e>612 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_ele_tel90_flux_e1') & ncdf_varget,fID,vID,p9e1 ;e>40 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_ele_tel90_flux_e2') & ncdf_varget,fID,vID,p9e2 ;e>130 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_ele_tel90_flux_e3') & ncdf_varget,fID,vID,p9e3 ;e>287 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_ele_tel90_flux_e4') & ncdf_varget,fID,vID,p9e4 ;e>612 keV[#/cm2-s-str]
vID=ncdf_varid(fID,'mep_omni_flux_p1') & ncdf_varget,fID,vID,p25 ;25 MeV[#/cm2-s-str-MeV]
vID=ncdf_varid(fID,'mep_omni_flux_p2') & ncdf_varget,fID,vID,p50 ;50 MeV[#/cm2-s-str-MeV]
vID=ncdf_varid(fID,'mep_omni_flux_p3') & ncdf_varget,fID,vID,p100;100 MeV[#/cm2-s-str-MeV]
e0=fltarr(narr,4) & e9=e0
p0=fltarr(narr,6) & p9=p0
ph=fltarr(narr,3)
  e0[*,0]=p0e1 & e0[*,1]=p0e2 & e0[*,2]=p0e3 & e0[*,3]=p0e4 ; e at PA=0
  e9[*,0]=p9e1 & e9[*,1]=p9e2 & e9[*,2]=p9e3 & e9[*,3]=p9e4 ; e at PA=0
  p0[*,0]=p0p1 & p0[*,1]=p0p2 & p0[*,2]=p0p3 & p0[*,3]=p0p4 & p0[*,4]=p0p5 & p0[*,5]=p0p6 ;p PA=0
  p9[*,0]=p9p1 & p9[*,1]=p9p2 & p9[*,2]=p9p3 & p9[*,3]=p9p4 & p9[*,4]=p9p5 & p9[*,5]=p9p6 ;p PA=90
  ph[*,0]=p25  & ph[*,1]=p50  & ph[*,2]=p100 ; HEP

;Plasma
vID=ncdf_varid(fID,'ted_ele_tel0_flux_4') & ncdf_varget,fID,vID,p0el4 ;e 189 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_ele_tel0_flux_8') & ncdf_varget,fID,vID,p0el8 ;e 844 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_ele_tel0_flux_11') & ncdf_varget,fID,vID,p0el11 ;e 2595 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_ele_tel0_flux_14') & ncdf_varget,fID,vID,p0el14 ;e 7980 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_ele_tel30_flux_4') & ncdf_varget,fID,vID,p3el4 ;e 189 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_ele_tel30_flux_8') & ncdf_varget,fID,vID,p3el8 ;e 844 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_ele_tel30_flux_11') & ncdf_varget,fID,vID,p3el11 ;e 2595 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_ele_tel30_flux_14') & ncdf_varget,fID,vID,p3el14 ;e 7980 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_pro_tel0_flux_4') & ncdf_varget,fID,vID,p0pl4 ;p 189 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_pro_tel0_flux_8') & ncdf_varget,fID,vID,p0pl8 ;p 844 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_pro_tel0_flux_11') & ncdf_varget,fID,vID,p0pl11 ;p 2595 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_pro_tel0_flux_14') & ncdf_varget,fID,vID,p0pl14 ;p 7980 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_pro_tel30_flux_4') & ncdf_varget,fID,vID,p3pl4 ;p 189 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_pro_tel30_flux_8') & ncdf_varget,fID,vID,p3pl8 ;p 844 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_pro_tel30_flux_11') & ncdf_varget,fID,vID,p3pl11 ;p 2595 eV[#/cm2-s-str-eV]
vID=ncdf_varid(fID,'ted_pro_tel30_flux_14') & ncdf_varget,fID,vID,p3pl14 ;p 7980 eV[#/cm2-s-str-eV]
pe0=fltarr(narr,4) & pe3=pe0 & pp0=pe0 & pp3=pe0
pe0[*,0]=p0el4 & pe0[*,1]=p0el8 & pe0[*,2]=p0el11 & pe0[*,3]=p0el14 ; e plasma at PA=0
pe3[*,0]=p3el4 & pe3[*,1]=p3el8 & pe3[*,2]=p3el11 & pe3[*,3]=p3el14 ; e plasma at PA=30
pp0[*,0]=p0pl4 & pp0[*,1]=p0pl8 & pp0[*,2]=p0pl11 & pp0[*,3]=p0pl14 ; p plasma at PA=0
pp3[*,0]=p3pl4 & pp3[*,1]=p3pl8 & pp3[*,2]=p3pl11 & pp3[*,3]=p3pl14 ; p plasma at PA=30

;Energy fluxes
vID=ncdf_varid(fID,'ted_ele_tel0_low_eflux') & ncdf_varget,fID,vID,p0elef ;e 50eV-1keV 0deg energy flux mW/m2-str
vID=ncdf_varid(fID,'ted_ele_tel30_low_eflux') & ncdf_varget,fID,vID,p3elef ;e 50eV-1keV 30deg energy flux mW/m2-str
vID=ncdf_varid(fID,'ted_ele_tel0_hi_eflux') & ncdf_varget,fID,vID,p0ehef ;e 1-20keV 0deg energy flux mW/m2-str
vID=ncdf_varid(fID,'ted_ele_tel30_hi_eflux') & ncdf_varget,fID,vID,p3ehef ;e 1-20keV 30deg energy flux mW/m2-str
vID=ncdf_varid(fID,'ted_pro_tel0_low_eflux') & ncdf_varget,fID,vID,p0plef ;p 50eV-1keV 0deg energy flux mW/m2-str
vID=ncdf_varid(fID,'ted_pro_tel30_low_eflux') & ncdf_varget,fID,vID,p3plef ;p 50eV-1keV 30deg energy flux mW/m2-str
vID=ncdf_varid(fID,'ted_pro_tel0_hi_eflux') & ncdf_varget,fID,vID,p0phef ;p 1-20keV 0deg energy flux mW/m2-str
vID=ncdf_varid(fID,'ted_pro_tel30_hi_eflux') & ncdf_varget,fID,vID,p3phef ;p 1-20keV 30deg energy flux mW/m2-str
efe=fltarr(narr,4) & efp=efe
efe[*,0]=p0elef & efe[*,1]=p3elef & efe[*,2]=p0ehef & efe[*,3]=p3ehef
efp[*,0]=p0plef & efp[*,1]=p3plef & efp[*,2]=p0phef & efp[*,3]=p3phef

;Magnetic field IGRF
vID=ncdf_varid(fID,'Br_sat') & ncdf_varget,fID,vID,Br ;Bradial IGRF, nT
vID=ncdf_varid(fID,'Bt_sat') & ncdf_varget,fID,vID,Bt ;Btheta IGRF, nT
vID=ncdf_varid(fID,'Bp_sat') & ncdf_varget,fID,vID,Bp ;Bphi IGRF, nT
vID=ncdf_varid(fID,'Btot_sat') & ncdf_varget,fID,vID,Btot ;Btotal IGRF, nT
magF=fltarr(narr,4)
magF[*,0]=Btot & magF[*,1]=Br & magF[*,2]=Bt & magF[*,3]=Bp

;Coordinates others
vID=ncdf_varid(fID,'geod_lat_foot') & ncdf_varget,fID,vID,glatf ;Geodetic lat (foot of field line), deg
vID=ncdf_varid(fID,'geod_lon_foot') & ncdf_varget,fID,vID,glonf ;Geodetic lon (foot of field line), deg
vID=ncdf_varid(fID,'aacgm_lat_foot') & ncdf_varget,fID,vID,alatf ;AACGM lat (foot of field line), deg
vID=ncdf_varid(fID,'aacgm_lon_foot') & ncdf_varget,fID,vID,alonf ;AACGM lon (foot of field line), deg
vID=ncdf_varid(fID,'mag_lat_foot') & ncdf_varget,fID,vID,mlatf ;Magnetic lat (foot of field line), deg
vID=ncdf_varid(fID,'mag_lon_foot') & ncdf_varget,fID,vID,mlonf ;Magnetic lon (foot of field line), deg
vID=ncdf_varid(fID,'mag_lat_sat') & ncdf_varget,fID,vID,mlat ;Magnetic lat (satellite), deg
vID=ncdf_varid(fID,'mag_lon_sat') & ncdf_varget,fID,vID,mlon ;Magnetic lon (satellite), deg
vID=ncdf_varid(fID,'L_IGRF') & ncdf_varget,fID,vID,vl ;L-value IGRF
vID=ncdf_varid(fID,'MLT') & ncdf_varget,fID,vID,vmlt ;MLT, hours
sg[*,3]=mlat & sg[*,4]=mlon
sgm=fltarr(narr,2)
sgm[*,0]=vl & sgm[*,1]=vmlt
fg=fltarr(narr,6)
fg[*,0]=glatf & fg[*,1]=glonf & fg[*,2]=alatf & fg[*,3]=alonf & fg[*,4]=mlatf & fg[*,5]=mlonf

;Orientation
vID=ncdf_varid(fID,'ted_alpha_0_sat') & ncdf_varget,fID,vID,pa0ted ;TED 0 deg telescope pitch angle, deg
vID=ncdf_varid(fID,'ted_alpha_30_sat') & ncdf_varget,fID,vID,pa3ted ;TED 30 deg telescope pitch angle, deg
vID=ncdf_varid(fID,'meped_alpha_0_sat') & ncdf_varget,fID,vID,pa0mep ;MEPED 0 deg telescope pitch angle, deg
vID=ncdf_varid(fID,'meped_alpha_90_sat') & ncdf_varget,fID,vID,pa9mep ;MEPED 90 deg telescope pitch angle, deg
pa=fltarr(narr,4)
pa[*,0]=pa0mep & pa[*,1]=pa9mep & pa[*,2]=pa0ted & pa[*,3]=pa3ted