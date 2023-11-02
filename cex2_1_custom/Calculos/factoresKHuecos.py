# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Calculos\factoresKHuecos.pyc
# Compiled at: 2015-05-29 10:02:49
diccionarioValorMedioCalefaccion = {}
diccionarioValorMedioCalefaccion['Techo'] = 0.9845
diccionarioValorMedioCalefaccion['Sur'] = 1.0
diccionarioValorMedioCalefaccion['SO'] = 0.8828
diccionarioValorMedioCalefaccion['Oeste'] = 0.6052
diccionarioValorMedioCalefaccion['NO'] = 0.3801
diccionarioValorMedioCalefaccion['Norte'] = 0.3355
diccionarioValorMedioCalefaccion['NE'] = 0.3925
diccionarioValorMedioCalefaccion['Este'] = 0.6612
diccionarioValorMedioCalefaccion['SE'] = 0.9469
diccionarioValorMedioRefrigeracion = {}
diccionarioValorMedioRefrigeracion['Techo'] = 2.0824
diccionarioValorMedioRefrigeracion['Sur'] = 1.0
diccionarioValorMedioRefrigeracion['SO'] = 1.1047
diccionarioValorMedioRefrigeracion['Oeste'] = 1.1069
diccionarioValorMedioRefrigeracion['NO'] = 0.7782
diccionarioValorMedioRefrigeracion['Norte'] = 0.4811
diccionarioValorMedioRefrigeracion['NE'] = 0.7763
diccionarioValorMedioRefrigeracion['Este'] = 1.1346
diccionarioValorMedioRefrigeracion['SE'] = 1.0661
diccionarioValorMedioCalefaccionTerciario = {}
diccionarioValorMedioRefrigeracionTerciario = {}
diccionarioValorMedioCalefaccionIntensidadBaja_8h = {}
diccionarioValorMedioCalefaccionIntensidadBaja_8h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadBaja_8h['NO'] = 0.3878
diccionarioValorMedioCalefaccionIntensidadBaja_8h['NE'] = 0.3888
diccionarioValorMedioCalefaccionIntensidadBaja_8h['SO'] = 0.8979
diccionarioValorMedioCalefaccionIntensidadBaja_8h['Este'] = 0.6299
diccionarioValorMedioCalefaccionIntensidadBaja_8h['Norte'] = 0.331
diccionarioValorMedioCalefaccionIntensidadBaja_8h['Oeste'] = 0.6093
diccionarioValorMedioCalefaccionIntensidadBaja_8h['SE'] = 0.9232
diccionarioValorMedioCalefaccionIntensidadBaja_8h['Techo'] = 0.9021
diccionarioValorMedioCalefaccionTerciario['Intensidad Baja - 8h'] = diccionarioValorMedioCalefaccionIntensidadBaja_8h
diccionarioValorMedioRefrigeracionIntensidadBaja_8h = {}
diccionarioValorMedioRefrigeracionIntensidadBaja_8h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadBaja_8h['NO'] = 0.6181
diccionarioValorMedioRefrigeracionIntensidadBaja_8h['NE'] = 0.6748
diccionarioValorMedioRefrigeracionIntensidadBaja_8h['SO'] = 0.9718
diccionarioValorMedioRefrigeracionIntensidadBaja_8h['Este'] = 1.0695
diccionarioValorMedioRefrigeracionIntensidadBaja_8h['Norte'] = 0.3804
diccionarioValorMedioRefrigeracionIntensidadBaja_8h['Oeste'] = 0.9756
diccionarioValorMedioRefrigeracionIntensidadBaja_8h['SE'] = 1.0682
diccionarioValorMedioRefrigeracionIntensidadBaja_8h['Techo'] = 1.6727
diccionarioValorMedioRefrigeracionTerciario['Intensidad Baja - 8h'] = diccionarioValorMedioRefrigeracionIntensidadBaja_8h
diccionarioValorMedioCalefaccionIntensidadMedia_8h = {}
diccionarioValorMedioCalefaccionIntensidadMedia_8h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadMedia_8h['NO'] = 0.3536
diccionarioValorMedioCalefaccionIntensidadMedia_8h['NE'] = 0.3554
diccionarioValorMedioCalefaccionIntensidadMedia_8h['SO'] = 0.9169
diccionarioValorMedioCalefaccionIntensidadMedia_8h['Este'] = 0.6048
diccionarioValorMedioCalefaccionIntensidadMedia_8h['Norte'] = 0.3063
diccionarioValorMedioCalefaccionIntensidadMedia_8h['Oeste'] = 0.5818
diccionarioValorMedioCalefaccionIntensidadMedia_8h['SE'] = 0.9383
diccionarioValorMedioCalefaccionIntensidadMedia_8h['Techo'] = 0.8504
diccionarioValorMedioCalefaccionTerciario['Intensidad Media - 8h'] = diccionarioValorMedioCalefaccionIntensidadMedia_8h
diccionarioValorMedioRefrigeracionIntensidadMedia_8h = {}
diccionarioValorMedioRefrigeracionIntensidadMedia_8h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadMedia_8h['NO'] = 0.6651
diccionarioValorMedioRefrigeracionIntensidadMedia_8h['NE'] = 0.6983
diccionarioValorMedioRefrigeracionIntensidadMedia_8h['SO'] = 0.9696
diccionarioValorMedioRefrigeracionIntensidadMedia_8h['Este'] = 1.0247
diccionarioValorMedioRefrigeracionIntensidadMedia_8h['Norte'] = 0.4433
diccionarioValorMedioRefrigeracionIntensidadMedia_8h['Oeste'] = 0.9435
diccionarioValorMedioRefrigeracionIntensidadMedia_8h['SE'] = 1.0551
diccionarioValorMedioRefrigeracionIntensidadMedia_8h['Techo'] = 1.6299
diccionarioValorMedioRefrigeracionTerciario['Intensidad Media - 8h'] = diccionarioValorMedioRefrigeracionIntensidadMedia_8h
diccionarioValorMedioCalefaccionIntensidadAlta_8h = {}
diccionarioValorMedioCalefaccionIntensidadAlta_8h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadAlta_8h['NO'] = 0.3743
diccionarioValorMedioCalefaccionIntensidadAlta_8h['NE'] = 0.3787
diccionarioValorMedioCalefaccionIntensidadAlta_8h['SO'] = 1.1916
diccionarioValorMedioCalefaccionIntensidadAlta_8h['Este'] = 0.6258
diccionarioValorMedioCalefaccionIntensidadAlta_8h['Norte'] = 0.349
diccionarioValorMedioCalefaccionIntensidadAlta_8h['Oeste'] = 0.6055
diccionarioValorMedioCalefaccionIntensidadAlta_8h['SE'] = 1.228
diccionarioValorMedioCalefaccionIntensidadAlta_8h['Techo'] = 1.0093
diccionarioValorMedioCalefaccionTerciario['Intensidad Alta - 8h'] = diccionarioValorMedioCalefaccionIntensidadAlta_8h
diccionarioValorMedioRefrigeracionIntensidadAlta_8h = {}
diccionarioValorMedioRefrigeracionIntensidadAlta_8h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadAlta_8h['NO'] = 0.6354
diccionarioValorMedioRefrigeracionIntensidadAlta_8h['NE'] = 0.6706
diccionarioValorMedioRefrigeracionIntensidadAlta_8h['SO'] = 0.9666
diccionarioValorMedioRefrigeracionIntensidadAlta_8h['Este'] = 0.9895
diccionarioValorMedioRefrigeracionIntensidadAlta_8h['Norte'] = 0.4448
diccionarioValorMedioRefrigeracionIntensidadAlta_8h['Oeste'] = 0.9114
diccionarioValorMedioRefrigeracionIntensidadAlta_8h['SE'] = 1.0472
diccionarioValorMedioRefrigeracionIntensidadAlta_8h['Techo'] = 1.5728
diccionarioValorMedioRefrigeracionTerciario['Intensidad Alta - 8h'] = diccionarioValorMedioRefrigeracionIntensidadAlta_8h
diccionarioValorMedioCalefaccionIntensidadBaja_12h = {}
diccionarioValorMedioCalefaccionIntensidadBaja_12h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadBaja_12h['NO'] = 0.4011
diccionarioValorMedioCalefaccionIntensidadBaja_12h['NE'] = 0.4006
diccionarioValorMedioCalefaccionIntensidadBaja_12h['SO'] = 0.8998
diccionarioValorMedioCalefaccionIntensidadBaja_12h['Este'] = 0.6448
diccionarioValorMedioCalefaccionIntensidadBaja_12h['Norte'] = 0.3461
diccionarioValorMedioCalefaccionIntensidadBaja_12h['Oeste'] = 0.6188
diccionarioValorMedioCalefaccionIntensidadBaja_12h['SE'] = 0.9345
diccionarioValorMedioCalefaccionIntensidadBaja_12h['Techo'] = 0.9161
diccionarioValorMedioCalefaccionTerciario['Intensidad Baja - 12h'] = diccionarioValorMedioCalefaccionIntensidadBaja_12h
diccionarioValorMedioRefrigeracionIntensidadBaja_12h = {}
diccionarioValorMedioRefrigeracionIntensidadBaja_12h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadBaja_12h['NO'] = 0.694
diccionarioValorMedioRefrigeracionIntensidadBaja_12h['NE'] = 0.7118
diccionarioValorMedioRefrigeracionIntensidadBaja_12h['SO'] = 1.0254
diccionarioValorMedioRefrigeracionIntensidadBaja_12h['Este'] = 1.0242
diccionarioValorMedioRefrigeracionIntensidadBaja_12h['Norte'] = 0.4763
diccionarioValorMedioRefrigeracionIntensidadBaja_12h['Oeste'] = 1.0004
diccionarioValorMedioRefrigeracionIntensidadBaja_12h['SE'] = 1.0442
diccionarioValorMedioRefrigeracionIntensidadBaja_12h['Techo'] = 1.6882
diccionarioValorMedioRefrigeracionTerciario['Intensidad Baja - 12h'] = diccionarioValorMedioRefrigeracionIntensidadBaja_12h
diccionarioValorMedioCalefaccionIntensidadMedia_12h = {}
diccionarioValorMedioCalefaccionIntensidadMedia_12h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadMedia_12h['NO'] = 0.3707
diccionarioValorMedioCalefaccionIntensidadMedia_12h['NE'] = 0.3736
diccionarioValorMedioCalefaccionIntensidadMedia_12h['SO'] = 0.9115
diccionarioValorMedioCalefaccionIntensidadMedia_12h['Este'] = 0.6186
diccionarioValorMedioCalefaccionIntensidadMedia_12h['Norte'] = 0.3266
diccionarioValorMedioCalefaccionIntensidadMedia_12h['Oeste'] = 0.5949
diccionarioValorMedioCalefaccionIntensidadMedia_12h['SE'] = 0.9521
diccionarioValorMedioCalefaccionIntensidadMedia_12h['Techo'] = 0.8721
diccionarioValorMedioCalefaccionTerciario['Intensidad Media - 12h'] = diccionarioValorMedioCalefaccionIntensidadMedia_12h
diccionarioValorMedioRefrigeracionIntensidadMedia_12h = {}
diccionarioValorMedioRefrigeracionIntensidadMedia_12h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadMedia_12h['NO'] = 0.6579
diccionarioValorMedioRefrigeracionIntensidadMedia_12h['NE'] = 0.6759
diccionarioValorMedioRefrigeracionIntensidadMedia_12h['SO'] = 1.0105
diccionarioValorMedioRefrigeracionIntensidadMedia_12h['Este'] = 0.9917
diccionarioValorMedioRefrigeracionIntensidadMedia_12h['Norte'] = 0.4508
diccionarioValorMedioRefrigeracionIntensidadMedia_12h['Oeste'] = 0.9614
diccionarioValorMedioRefrigeracionIntensidadMedia_12h['SE'] = 1.039
diccionarioValorMedioRefrigeracionIntensidadMedia_12h['Techo'] = 1.6251
diccionarioValorMedioRefrigeracionTerciario['Intensidad Media - 12h'] = diccionarioValorMedioRefrigeracionIntensidadMedia_12h
diccionarioValorMedioCalefaccionIntensidadAlta_12h = {}
diccionarioValorMedioCalefaccionIntensidadAlta_12h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadAlta_12h['NO'] = 0.397
diccionarioValorMedioCalefaccionIntensidadAlta_12h['NE'] = 0.4007
diccionarioValorMedioCalefaccionIntensidadAlta_12h['SO'] = 1.2848
diccionarioValorMedioCalefaccionIntensidadAlta_12h['Este'] = 0.6448
diccionarioValorMedioCalefaccionIntensidadAlta_12h['Norte'] = 0.3684
diccionarioValorMedioCalefaccionIntensidadAlta_12h['Oeste'] = 0.6167
diccionarioValorMedioCalefaccionIntensidadAlta_12h['SE'] = 1.4666
diccionarioValorMedioCalefaccionIntensidadAlta_12h['Techo'] = 1.0917
diccionarioValorMedioCalefaccionTerciario['Intensidad Alta - 12h'] = diccionarioValorMedioCalefaccionIntensidadAlta_12h
diccionarioValorMedioRefrigeracionIntensidadAlta_12h = {}
diccionarioValorMedioRefrigeracionIntensidadAlta_12h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadAlta_12h['NO'] = 0.6281
diccionarioValorMedioRefrigeracionIntensidadAlta_12h['NE'] = 0.6392
diccionarioValorMedioRefrigeracionIntensidadAlta_12h['SO'] = 1.0067
diccionarioValorMedioRefrigeracionIntensidadAlta_12h['Este'] = 0.9431
diccionarioValorMedioRefrigeracionIntensidadAlta_12h['Norte'] = 0.4468
diccionarioValorMedioRefrigeracionIntensidadAlta_12h['Oeste'] = 0.9173
diccionarioValorMedioRefrigeracionIntensidadAlta_12h['SE'] = 1.0248
diccionarioValorMedioRefrigeracionIntensidadAlta_12h['Techo'] = 1.569
diccionarioValorMedioRefrigeracionTerciario['Intensidad Alta - 12h'] = diccionarioValorMedioRefrigeracionIntensidadAlta_12h
diccionarioValorMedioCalefaccionIntensidadBaja_16h = {}
diccionarioValorMedioCalefaccionIntensidadBaja_16h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadBaja_16h['NO'] = 0.419
diccionarioValorMedioCalefaccionIntensidadBaja_16h['NE'] = 0.4182
diccionarioValorMedioCalefaccionIntensidadBaja_16h['SO'] = 0.915
diccionarioValorMedioCalefaccionIntensidadBaja_16h['Este'] = 0.6602
diccionarioValorMedioCalefaccionIntensidadBaja_16h['Norte'] = 0.3662
diccionarioValorMedioCalefaccionIntensidadBaja_16h['Oeste'] = 0.6465
diccionarioValorMedioCalefaccionIntensidadBaja_16h['SE'] = 0.9436
diccionarioValorMedioCalefaccionIntensidadBaja_16h['Techo'] = 0.9434
diccionarioValorMedioCalefaccionTerciario['Intensidad Baja - 16h'] = diccionarioValorMedioCalefaccionIntensidadBaja_16h
diccionarioValorMedioRefrigeracionIntensidadBaja_16h = {}
diccionarioValorMedioRefrigeracionIntensidadBaja_16h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadBaja_16h['NO'] = 0.7062
diccionarioValorMedioRefrigeracionIntensidadBaja_16h['NE'] = 0.7116
diccionarioValorMedioRefrigeracionIntensidadBaja_16h['SO'] = 1.058
diccionarioValorMedioRefrigeracionIntensidadBaja_16h['Este'] = 1.0298
diccionarioValorMedioRefrigeracionIntensidadBaja_16h['Norte'] = 0.4791
diccionarioValorMedioRefrigeracionIntensidadBaja_16h['Oeste'] = 1.0158
diccionarioValorMedioRefrigeracionIntensidadBaja_16h['SE'] = 1.0638
diccionarioValorMedioRefrigeracionIntensidadBaja_16h['Techo'] = 1.709
diccionarioValorMedioRefrigeracionTerciario['Intensidad Baja - 16h'] = diccionarioValorMedioRefrigeracionIntensidadBaja_16h
diccionarioValorMedioCalefaccionIntensidadMedia_16h = {}
diccionarioValorMedioCalefaccionIntensidadMedia_16h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadMedia_16h['NO'] = 0.392
diccionarioValorMedioCalefaccionIntensidadMedia_16h['NE'] = 0.3969
diccionarioValorMedioCalefaccionIntensidadMedia_16h['SO'] = 0.9346
diccionarioValorMedioCalefaccionIntensidadMedia_16h['Este'] = 0.6408
diccionarioValorMedioCalefaccionIntensidadMedia_16h['Norte'] = 0.3605
diccionarioValorMedioCalefaccionIntensidadMedia_16h['Oeste'] = 0.6174
diccionarioValorMedioCalefaccionIntensidadMedia_16h['SE'] = 0.9695
diccionarioValorMedioCalefaccionIntensidadMedia_16h['Techo'] = 0.898
diccionarioValorMedioCalefaccionTerciario['Intensidad Media - 16h'] = diccionarioValorMedioCalefaccionIntensidadMedia_16h
diccionarioValorMedioRefrigeracionIntensidadMedia_16h = {}
diccionarioValorMedioRefrigeracionIntensidadMedia_16h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadMedia_16h['NO'] = 0.6706
diccionarioValorMedioRefrigeracionIntensidadMedia_16h['NE'] = 0.6828
diccionarioValorMedioRefrigeracionIntensidadMedia_16h['SO'] = 1.031
diccionarioValorMedioRefrigeracionIntensidadMedia_16h['Este'] = 0.9947
diccionarioValorMedioRefrigeracionIntensidadMedia_16h['Norte'] = 0.4731
diccionarioValorMedioRefrigeracionIntensidadMedia_16h['Oeste'] = 0.9746
diccionarioValorMedioRefrigeracionIntensidadMedia_16h['SE'] = 1.0493
diccionarioValorMedioRefrigeracionIntensidadMedia_16h['Techo'] = 1.6395
diccionarioValorMedioRefrigeracionTerciario['Intensidad Media - 16h'] = diccionarioValorMedioRefrigeracionIntensidadMedia_16h
diccionarioValorMedioCalefaccionIntensidadAlta_16h = {}
diccionarioValorMedioCalefaccionIntensidadAlta_16h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadAlta_16h['NO'] = 0.3996
diccionarioValorMedioCalefaccionIntensidadAlta_16h['NE'] = 0.4011
diccionarioValorMedioCalefaccionIntensidadAlta_16h['SO'] = 1.433
diccionarioValorMedioCalefaccionIntensidadAlta_16h['Este'] = 0.6762
diccionarioValorMedioCalefaccionIntensidadAlta_16h['Norte'] = 0.3863
diccionarioValorMedioCalefaccionIntensidadAlta_16h['Oeste'] = 0.6427
diccionarioValorMedioCalefaccionIntensidadAlta_16h['SE'] = 1.6243
diccionarioValorMedioCalefaccionIntensidadAlta_16h['Techo'] = 1.209
diccionarioValorMedioCalefaccionTerciario['Intensidad Alta - 16h'] = diccionarioValorMedioCalefaccionIntensidadAlta_16h
diccionarioValorMedioRefrigeracionIntensidadAlta_16h = {}
diccionarioValorMedioRefrigeracionIntensidadAlta_16h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadAlta_16h['NO'] = 0.6336
diccionarioValorMedioRefrigeracionIntensidadAlta_16h['NE'] = 0.6416
diccionarioValorMedioRefrigeracionIntensidadAlta_16h['SO'] = 1.0229
diccionarioValorMedioRefrigeracionIntensidadAlta_16h['Este'] = 0.9457
diccionarioValorMedioRefrigeracionIntensidadAlta_16h['Norte'] = 0.4524
diccionarioValorMedioRefrigeracionIntensidadAlta_16h['Oeste'] = 0.9279
diccionarioValorMedioRefrigeracionIntensidadAlta_16h['SE'] = 1.0389
diccionarioValorMedioRefrigeracionIntensidadAlta_16h['Techo'] = 1.5835
diccionarioValorMedioRefrigeracionTerciario['Intensidad Alta - 16h'] = diccionarioValorMedioRefrigeracionIntensidadAlta_16h
diccionarioValorMedioCalefaccionIntensidadBaja_24h = {}
diccionarioValorMedioCalefaccionIntensidadBaja_24h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadBaja_24h['NO'] = 0.4658
diccionarioValorMedioCalefaccionIntensidadBaja_24h['NE'] = 0.4651
diccionarioValorMedioCalefaccionIntensidadBaja_24h['SO'] = 0.9724
diccionarioValorMedioCalefaccionIntensidadBaja_24h['Este'] = 0.7114
diccionarioValorMedioCalefaccionIntensidadBaja_24h['Norte'] = 0.4094
diccionarioValorMedioCalefaccionIntensidadBaja_24h['Oeste'] = 0.7071
diccionarioValorMedioCalefaccionIntensidadBaja_24h['SE'] = 0.9854
diccionarioValorMedioCalefaccionIntensidadBaja_24h['Techo'] = 1.043
diccionarioValorMedioCalefaccionTerciario['Intensidad Baja - 24h'] = diccionarioValorMedioCalefaccionIntensidadBaja_24h
diccionarioValorMedioRefrigeracionIntensidadBaja_24h = {}
diccionarioValorMedioRefrigeracionIntensidadBaja_24h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadBaja_24h['NO'] = 0.7279
diccionarioValorMedioRefrigeracionIntensidadBaja_24h['NE'] = 0.7292
diccionarioValorMedioRefrigeracionIntensidadBaja_24h['SO'] = 1.0853
diccionarioValorMedioRefrigeracionIntensidadBaja_24h['Este'] = 1.0582
diccionarioValorMedioRefrigeracionIntensidadBaja_24h['Norte'] = 0.4937
diccionarioValorMedioRefrigeracionIntensidadBaja_24h['Oeste'] = 1.0583
diccionarioValorMedioRefrigeracionIntensidadBaja_24h['SE'] = 1.0858
diccionarioValorMedioRefrigeracionIntensidadBaja_24h['Techo'] = 1.751
diccionarioValorMedioRefrigeracionTerciario['Intensidad Baja - 24h'] = diccionarioValorMedioRefrigeracionIntensidadBaja_24h
diccionarioValorMedioCalefaccionIntensidadMedia_24h = {}
diccionarioValorMedioCalefaccionIntensidadMedia_24h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadMedia_24h['NO'] = 0.4083
diccionarioValorMedioCalefaccionIntensidadMedia_24h['NE'] = 0.4198
diccionarioValorMedioCalefaccionIntensidadMedia_24h['SO'] = 0.9224
diccionarioValorMedioCalefaccionIntensidadMedia_24h['Este'] = 0.664
diccionarioValorMedioCalefaccionIntensidadMedia_24h['Norte'] = 0.3706
diccionarioValorMedioCalefaccionIntensidadMedia_24h['Oeste'] = 0.628
diccionarioValorMedioCalefaccionIntensidadMedia_24h['SE'] = 0.9681
diccionarioValorMedioCalefaccionIntensidadMedia_24h['Techo'] = 0.9297
diccionarioValorMedioCalefaccionTerciario['Intensidad Media - 24h'] = diccionarioValorMedioCalefaccionIntensidadMedia_24h
diccionarioValorMedioRefrigeracionIntensidadMedia_24h = {}
diccionarioValorMedioRefrigeracionIntensidadMedia_24h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadMedia_24h['NO'] = 0.7697
diccionarioValorMedioRefrigeracionIntensidadMedia_24h['NE'] = 0.7472
diccionarioValorMedioRefrigeracionIntensidadMedia_24h['SO'] = 1.1777
diccionarioValorMedioRefrigeracionIntensidadMedia_24h['Este'] = 1.0497
diccionarioValorMedioRefrigeracionIntensidadMedia_24h['Norte'] = 0.5508
diccionarioValorMedioRefrigeracionIntensidadMedia_24h['Oeste'] = 1.1145
diccionarioValorMedioRefrigeracionIntensidadMedia_24h['SE'] = 1.1129
diccionarioValorMedioRefrigeracionIntensidadMedia_24h['Techo'] = 1.803
diccionarioValorMedioRefrigeracionTerciario['Intensidad Media - 24h'] = diccionarioValorMedioRefrigeracionIntensidadMedia_24h
diccionarioValorMedioCalefaccionIntensidadAlta_24h = {}
diccionarioValorMedioCalefaccionIntensidadAlta_24h['Sur'] = 1.0
diccionarioValorMedioCalefaccionIntensidadAlta_24h['NO'] = 0.4585
diccionarioValorMedioCalefaccionIntensidadAlta_24h['NE'] = 0.4611
diccionarioValorMedioCalefaccionIntensidadAlta_24h['SO'] = 1.0583
diccionarioValorMedioCalefaccionIntensidadAlta_24h['Este'] = 0.7198
diccionarioValorMedioCalefaccionIntensidadAlta_24h['Norte'] = 0.4338
diccionarioValorMedioCalefaccionIntensidadAlta_24h['Oeste'] = 0.7043
diccionarioValorMedioCalefaccionIntensidadAlta_24h['SE'] = 1.2658
diccionarioValorMedioCalefaccionIntensidadAlta_24h['Techo'] = 0.9916
diccionarioValorMedioCalefaccionTerciario['Intensidad Alta - 24h'] = diccionarioValorMedioCalefaccionIntensidadAlta_24h
diccionarioValorMedioRefrigeracionIntensidadAlta_24h = {}
diccionarioValorMedioRefrigeracionIntensidadAlta_24h['Sur'] = 1.0
diccionarioValorMedioRefrigeracionIntensidadAlta_24h['NO'] = 0.6874
diccionarioValorMedioRefrigeracionIntensidadAlta_24h['NE'] = 0.6924
diccionarioValorMedioRefrigeracionIntensidadAlta_24h['SO'] = 1.0753
diccionarioValorMedioRefrigeracionIntensidadAlta_24h['Este'] = 0.9964
diccionarioValorMedioRefrigeracionIntensidadAlta_24h['Norte'] = 0.5097
diccionarioValorMedioRefrigeracionIntensidadAlta_24h['Oeste'] = 0.9827
diccionarioValorMedioRefrigeracionIntensidadAlta_24h['SE'] = 1.0901
diccionarioValorMedioRefrigeracionIntensidadAlta_24h['Techo'] = 1.6356
diccionarioValorMedioRefrigeracionTerciario['Intensidad Alta - 24h'] = diccionarioValorMedioRefrigeracionIntensidadAlta_24h

def factorKHuecosResidencial(orientacion=None):
    """
    Justificacion valores:
    D:\x08aseDeDatosCexYBateriasComprobacion\\BD_2014
uevaBD\\simulacionesHU\\gHuecosPorOrientacion

    Valores Orientacion:
          - Sur: (acimuth  HU: 0)
          - SO: (acimuth HU: 45)
          - Oeste: (acimuth HU: 90)
          - NO: (acimuth HU: 138.75)
          - Norte: (acimuth HU: 180)
          - NE: (acimuth HU: 221.25)
          - Este: (acimtuh HU: 270.)
          - SE: (acimuth HU: 315.)
          - Techo
    """
    try:
        return (
         diccionarioValorMedioCalefaccion[orientacion], diccionarioValorMedioRefrigeracion[orientacion])
    except KeyError:
        return 'Orientacion no reconocida'


def factorKHuecosTerciario(orientacion=None, intensidadUso=None, zonaClimatica=None):
    """
    Justificacion valores:
    D:\x08aseDeDatosCexYBateriasComprobacion\\BD_2014
uevaBD\\simulacionesHU\\gHuecosPorOrientacion

    Valores Orientacion:
          - Sur: (acimuth  HU: 0)
          - SO: (acimuth HU: 45)
          - Oeste: (acimuth HU: 90)
          - NO: (acimuth HU: 138.75)
          - Norte: (acimuth HU: 180)
          - NE: (acimuth HU: 221.25)
          - Este: (acimtuh HU: 270.)
          - SE: (acimuth HU: 315.)
          - Techo
    """
    factorCorrectoVeranoPorZonaClimatica = 1.0
    try:
        return (
         diccionarioValorMedioCalefaccionTerciario[intensidadUso][orientacion] * 1.0,
         diccionarioValorMedioRefrigeracionTerciario[intensidadUso][orientacion] * factorCorrectoVeranoPorZonaClimatica)
    except KeyError:
        return 'Orientacion no reconocida'