from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QTableView, QPushButton, QLineEdit, QListWidget, QTableWidget, QListWidgetItem, QTableWidgetItem, QLabel, QSpinBox, QAbstractItemView
from PySide2.QtCore import QFile, QSize, QAbstractListModel, QAbstractItemModel, QModelIndex
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtGui import QWindow
from PySide2 import QtWidgets
from PySide2.QtGui import *
#print(PySide2)
import os
import time
from datetime import  datetime
import datetime
import sys
import MySQLdb
global codprod1
global nombprod1
global precio1
global cantvprod1
global stockdis1
global userlog1
global passw1
global compus1
global compco1
global loginwindow
global codnum1
global codadd2
global prodnom1
global Busqlis1
global cantidadp2
global exCli1
global extot1
global Userlog1
global exefect1
global exdebi1
global excredi1
global cciuser1
global montotpre1
global indforwid1
global verdmontot1
global usercompar1
verdmontot1=int(0)
indforwid1=str(None)
montotpre1=0
usercompar1 = None

#userlog1=str('Master')
#passw1=str('master6969')

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
app = QApplication(sys.argv)
loginfile = QFile("iniciosesion.ui")
loginfile.open(QFile.ReadOnly)
loader = QUiLoader()
loginwindow = loader.load(loginfile)
USqline1 = loginwindow.findChild(QLineEdit, 'Usuarioline1')
PSqline1 = loginwindow.findChild(QLineEdit, 'passw1')
alerforlog1=loginwindow.findChild(QLabel, 'aviso1')
btn_brow_1 = loginwindow.findChild(QPushButton, 'inisesbut1')
loginwindow.show()
#####     Ventana de Ventas
venfile1 = QFile("ventaventana.ui")
venfile1.open(QFile.ReadOnly)
loader2 = QUiLoader()
venwindow2 = loader2.load(venfile1)
nomqline2 = venwindow2.findChild(QLineEdit, 'busnom1')
codqline2 = venwindow2.findChild(QLineEdit, 'buscod1')
codadd2 = venwindow2.findChild(QLineEdit, 'addcodven1')
canadd2 = venwindow2.findChild(QLineEdit, 'cantprodven1')
btn_nom_1 = venwindow2.findChild(QPushButton, 'busnombut1')
btn_cod_1 = venwindow2.findChild(QPushButton, 'buscodbut1')
btn_addp_1 = venwindow2.findChild(QPushButton, 'addlven1')
btn_execv_1 = venwindow2.findChild(QPushButton, 'execvent1')
btn_cierre_1 = venwindow2.findChild(QPushButton, 'cierredia1')
btn_qfdes_1 = venwindow2.findChild(QPushButton, 'elifrdes1')
Busqlis1 = venwindow2.findChild(QListWidget, 'listBusq1')
Desgloselis1 = venwindow2.findChild(QListWidget, 'listDesglose1')
Desgtab1 = venwindow2.findChild(QTableView, 'tabdes1')
Desgtabwid1 = venwindow2.findChild(QTableWidget, 'tabwiddesg1')
realventtot1=venwindow2.findChild(QLabel, 'ventot1')
columnLabels1 = ["Make", "Model", "Price"]
Desgtab1.setAlternatingRowColors(True)
Desgtabwid1.setColumnWidth(0, 69)
Desgtabwid1.setColumnWidth(1, 650)
Desgtabwid1.setColumnWidth(2, 75)
Desgtabwid1.setColumnWidth(3, 40)
Desgtabwid1.setColumnWidth(4, 90)
#print(Desgtabwid1)


#Desgtab1.setHorizontalHeaderLabels(columnLabels1)
#####      ventana de ejecucion venta
exvenfile1 = QFile("execventa.ui")
exvenfile1.open(QFile.ReadOnly)
loader3 = QUiLoader()
exvenwindow2 = loader2.load(exvenfile1)
exCli1 = exvenwindow2.findChild(QLineEdit, 'nomclie1')
extot1 = exvenwindow2.findChild(QLineEdit, 'tot1')
exefect1 = exvenwindow2.findChild(QLineEdit, 'efect1')
exdebi1 = exvenwindow2.findChild(QLineEdit, 'debi1')
excredi1 = exvenwindow2.findChild(QLineEdit, 'credi1')
execciebut2 = exvenwindow2.findChild(QPushButton, 'regbut1')
alertlab1 = exvenwindow2.findChild(QLabel, 'confirvent1')
commenttab1 = exvenwindow2.findChild(QLineEdit, 'commentv1')
#####        ventana de cierre diario
ccifile1 = QFile("cierrediario.ui")
ccifile1.open(QFile.ReadOnly)
loader4 = QUiLoader()
cciwindow2 = loader2.load(ccifile1)
cciuser1 = cciwindow2.findChild(QLineEdit, 'usercierre')
cciconf1 = cciwindow2.findChild(QPushButton, 'efeccierre1')
ccialert1 = cciwindow2.findChild(QLabel, 'stat1')



####funcion Inicio de sesion
def GetLogin1(userlog1, passw1):
    try:
        connectionUser = MySQLdb.connect(host='xxxxxxxxxxxx',
                                             port=3336,
                                             database='xxxUsuario',
                                             user='xxxxxxxx',
                                             password='xxxxxxxx')

        Querylog1 = """SELECT 
                                    usuario,
                                    contraseña
                                FROM
                                    usuarios
                                WHERE
                                    usuario = '"""+str(userlog1)+"""' AND
                                    contraseña = '"""+str(passw1)+"""';"""
        print("listo")
        cursorVen1 = connectionUser.cursor()
        cursorVen1.execute(Querylog1)
        #print(result)
        connectionUser.commit()
    
        record2 = cursorVen1.fetchall()
        cursorVen1.close()
        #print(record2)
        if len(record2) != 0:
            record3 = record2[0]
            compus1 = record3[0]
            compco1 = record3[1]
            #print(str(record3))
            if compus1 == userlog1:
                if compco1 == passw1:
                    print('pass!')
                    alerforlog1.setText('Conectado!')
                    venwindow2.show()
                    loginwindow.close()
                    return userlog1
                else:
                    print('Contraseña incorrecta!')
                    alerforlog1.setText('Datos incorrectos!')
            else:
                print('Usuario incorrecto!')
        else:
            print('Credenciales incorrectas!')
            alerforlog1.setText('Datos incorrectos!')
    except TypeError or EnvironmentError or IOError or ConnectionError:
        print('Error al cargar!')
####funcion contedo diario
def countplusd1(codprod2, cantprend1):
    try:
        connectionMActs = MySQLdb.connect(host='xxxxxxxxxxxx',
                                         port=3336,
                                         database='xxxxMovi',
                                         user='xxxxxxxx',
                                         password='xxxxxxxx')
        putacts1 = """INSERT INTO lotediarioRC(codigo,
                                              cantidad, 
                                              fecha)
                         VALUES ('"""+str(codprod2)+"""', 
                                 '"""+str(cantprend1)+"""',
                                 '"""+str(datetime.datetime.now())+"""');"""
        cursoracts1 = connectionMActs.cursor()
        cursoracts1.execute(putacts1)
        connectionMActs.commit()
        resqueryVen1 = cursoracts1.fetchall()
        cursoracts1.close()
        print('actualizado')
    except TypeError or EnvironmentError or IOError or ConnectionError:
        print('Error al cargar!')
####funcion ingresar venta al sistema
def PostSale1(NomCli1, fechH1, montot1, userlog1, totefe1, totdeb1, totcred1, comments1):
    try:
        connectionMovi = MySQLdb.connect(host='xxxxxxxxxxxx',
                                         port=3336,
                                         database='xxxxMovi',
                                         user='xxxxxxxx',
                                         password='xxxxxxxx')
        putventonl1 = """INSERT INTO ventas(cliente,
                                              fecha, 
                                              total, 
                                              vendedor,
                                              efectivo,
                                              debito,
                                              credito,
                                              comentarios)
                         VALUES ('"""+str(NomCli1)+"""', 
                                 '"""+str(fechH1)+"""',
                                 '"""+str(float(montot1))+"""', 
                                 '"""+str(userlog1)+"""',
                                 '"""+str(float(totefe1))+"""',
                                 '"""+str(float(totdeb1))+"""',
                                 '"""+str(float(totcred1))+"""',
                                 '"""+str(comments1)+"""');"""
        cursorMovi1 = connectionMovi.cursor()
        cursorMovi1.execute(putventonl1)
        connectionMovi.commit()
        resqueryVen1 = cursorMovi1.fetchall()
        cursorMovi1.close()
        alertlab1.setText('Actualizando Stock...')
        print(resqueryVen1)
        cargapostv1 = Desgtabwid1.rowCount()
        print(str(cargapostv1)+str('  mira'))
        catalogcod1 = []
        catalogcan1 = []
        if  cargapostv1 >= int(1):
            print('cargapostv1 >= int(1)')
            for row in range(0, int(cargapostv1)):
                twi0 = Desgtabwid1.item(row, 0)
                twi1 = Desgtabwid1.item(row, 3)

                # twi1 = self.ui.tableWidget.cellWidget(row,1)
                # twi2 = self.ui.tableWidget.cellWidget(row,2)
                catalogcod1.append(twi0.text())
                catalogcan1.append(twi1.text())
                calfa11=catalogcod1[row]
                calfa22=catalogcan1[row]
                print(catalogcan1)
                print(catalogcod1)
                susprodstock1(calfa11, calfa22)
                countplusd1(calfa11, calfa22)

            print(catalogcan1)
        else:
            print('cargapostv1 == int(0)')
            twi0 = Desgtabwid1.item(0, 0)
            twi1 = Desgtabwid1.item(0, 3)

            # twi1 = self.ui.tableWidget.cellWidget(row,1)
            # twi2 = self.ui.tableWidget.cellWidget(row,2)
            catalogcod1.append(twi0.text())
            catalogcan1.append(twi1.text())
            calfa11 = catalogcod1[0]
            calfa22 = catalogcan1[0]
            print(catalogcan1)
            print(catalogcod1)
            susprodstock1(calfa11, calfa22)
            countplusd1(calfa11, calfa22)


        if int(cargapostv1) != int(0):
            print('si hay')
            for inumb9 in range(0, int(cargapostv1)):
                Desgtabwid1.removeRow(0)

                
            realventtot1.setText('0')
        else:
            print('no hay')
            Desgtabwid1.removeRow(0)
            realventtot1.setText('0')

        alertlab1.setText('Carga de venta exitosa')

    except TypeError or EnvironmentError or IOError or ConnectionError:
        print('Error al cargar!')
        alertlab1.setText('Error al cargar!')
    #cursorMovi1
####funcion arrancar PostSale
def runPostSale(exCli1, extot1, Userlog1, exefect1, exdebi1, excredi1):
    NomCli1 = str(exCli1.text())
    fechH1 = str(datetime.datetime.now())
    montot1 = int(extot1.text())
    userlog1 = Userlog1
    totefe1 = int(exefect1.text())
    totdeb1 =  int(exdebi1.text())
    totcred1 = int(excredi1.text())
    comments1 = str(commenttab1.text())
    PostSale1(NomCli1, fechH1, montot1, userlog1, totefe1, totdeb1, totcred1, comments1)
####funcion venta remueve de stock por separado
def susprodstock1(codprod2, cantprend1):
    connectionStock3 = MySQLdb.connect(host='xxxxxxxxxxxx',
                                       port=3336,
                                       database='xxxxStock',
                                       user='xxxxxxxx',
                                       password='xxxxxxxx')
    putventonl1 = """UPDATE stockRioCuarto 
SET 
    CantidadDisp = CantidadDisp-"""+str(int(cantprend1))+"""
WHERE
    codigo = """+str("'")+str(str(codprod2))+str("'")+""";"""

    cursorStock3 = connectionStock3.cursor()
    cursorStock3.execute(putventonl1)
    connectionStock3.commit()
    resputdel1 = cursorStock3.fetchall()
    cursorStock3.close()
    print("actualizado al mejor")
    print(resputdel1)
####funcion actualizar stock post-venta
def rundrstock1(codsv1, cantsv1):
    for i in range(len(codsv1)):
        codprod3=str("{}".format(codsv1[i]))
        cantv3 = str("{}".format(cantsv1[i]))
        susprodstock1(codprod3,cantv3)
####funcion devolucion de producto
def returnS1(codnum2, prodnom1, valprendev1, cantdev1, fechH1,fall1):
    fechH1=str(datetime.date.today())
    connectionStock2 = MySQLdb.connect(host='xxxxxxxxxxxx',
                                       port=3336,
                                       database='xxxxStock',
                                       user='xxxxxxxx',
                                       password='xxxxxxxx')
    putventonl1 = """INSERT INTO devueltoRioCuarto(codigo,
                                              nombre, 
                                              precioDetal, 
                                              cantidad,
                                              fecha,
                                              fallado)
                         VALUES ('"""+str(codnum2)+"""', 
                                 '"""+str(prodnom1)+"""',
                                 '"""+str(float(valprendev1))+"""', 
                                 '"""+str(cantdev1)+"""',
                                 '"""+str(fechH1)+"""',
                                 '"""+str(int(fall1))+"""');"""
    cursorStock2 = connectionStock2.cursor()
    cursorStock2.execute(putventonl1)
    connectionStock2.commit()
    resputdel1 = cursorStock2.fetchall()
    cursorStock2.close()
    print(resputdel1)
####funcion consultar producto en stock
def getprod1(callval1, codnum1, prodnom1):

    #loginwindow.show()

    connectionStock1 = MySQLdb.connect(host='xxxxxxxxxxxx',
                                     port=3336,
                                     database='xxxxStock',
                                     user='xxxxxxxx',
                                     password='xxxxxxxx')

    QueryprodC1 = """SELECT 
                                    codigo,
                                    nombre,
                                    PrecioDetal
                                    
                                FROM stockRioCuarto WHERE codigo='"""+str(codnum1)+"""';"""
    QueryprodN1 = """SELECT 
                                        codigo,
                                        nombre,
                                        PrecioDetal

                                    FROM stockRioCuarto WHERE 
                                    locate('""" + str(prodnom1) + """', nombre);"""
    cursorQp1 = connectionStock1.cursor()
    if callval1 == int(1):
        Queryprodf1=QueryprodC1
    if callval1 == int(2):
        Queryprodf1=QueryprodN1
    cursorQp1.execute(Queryprodf1)
    # print(result)
    connectionStock1.commit()
    recordst1 = cursorQp1.fetchall()
    recordst2 = recordst1[int(int(len(recordst1))-int(1))]
    cursorQp1.close()

    print(recordst1)

    for i in range(int(len(recordst1))):
        stockwfile = QFile("prodstockwidget.ui")
        stockwfile.open(QFile.ReadOnly)
        stockloader = QUiLoader()
        stockwwindow = stockloader.load(stockwfile)
        tam1=QSize()
        tam1.setHeight(44)
        tam1.setWidth(963)
        itemN1 = QtWidgets.QListWidgetItem()
        itemN1.setSizeHint(tam1)
        Codpros1 = stockwwindow.findChild(QLabel, 'codn1')
        Nombpros1 = stockwwindow.findChild(QLabel, 'nomp1')
        pricest1 = stockwwindow.findChild(QLabel, 'preciow1')
        Codpros1.setText(str(recordst1[int(i)][0]))
        Nombpros1.setText(str(recordst1[int(i)][1]))
        pricest1.setText(str(recordst1[int(i)][2]))
        Busqlis1.addItem(itemN1)
        Busqlis1.setItemWidget(itemN1, stockwwindow)
####funcion cargar data busqueda segun codigo(rungetprod1) o nombre(rungetprod2)
def rungetprod1():
    codnum1 = codqline2.text()
    callval1 = int(1)
    prodnom1 = int(11)
    getprod1(callval1, codnum1, prodnom1)
def rungetprod2():
    codnum1 = int(1)
    callval1 = int(2)
    prodnom1 = nomqline2.text()
    getprod1(callval1, codnum1, prodnom1)
####funcion sellar venta
def startven1(NomCliinv1, fechinvH1, montotinv1, userlog1, totefeinv1, totdebinv1, totcredinv1, commentsinv1, codsinv1, cantsinv1):
    PostSale1(NomCliinv1, fechinvH1, montotinv1, userlog1, totefeinv1, totdebinv1, totcredinv1, commentsinv1)
    rundrstock1(codsinv1, cantsinv1)
####funcion consultar total
def getventt1(userresp1, montopre1):
    connectionCier2 = MySQLdb.connect(host='xxxxxxxxxxxx',
                                     port=3336,
                                     database='xxxxMovi',
                                     user='xxxxxxxx',
                                     password='xxxxxxxx')
    cierquery2 = """SELECT total FROM ventas WHERE fecha >= '"""+str(datetime.date.today())+""" 00:00:00' AND fecha <= '"""+str(datetime.date.today())+""" 23:59:59';"""
    cierquery2ef = """SELECT efectivo FROM ventas WHERE fecha >= '"""+str(datetime.date.today())+""" 00:00:00' AND fecha <= '"""+str(datetime.date.today())+""" 23:59:59';"""
    cierquery2de = """SELECT debito FROM ventas WHERE fecha >= '"""+str(datetime.date.today())+""" 00:00:00' AND fecha <= '"""+str(datetime.date.today())+""" 23:59:59';"""
    cierquery2cr = """SELECT credito FROM ventas WHERE fecha >= '"""+str(datetime.date.today())+""" 00:00:00' AND fecha <= '"""+str(datetime.date.today())+""" 23:59:59';"""

    cursorCie2 = connectionCier2.cursor()
    cursorCie2.execute(cierquery2)
    connectionCier2.commit()
    record8 = cursorCie2.fetchall()
    cursorCie2 = connectionCier2.cursor()
    cursorCie2.execute(cierquery2ef)
    connectionCier2.commit()
    record8ef = cursorCie2.fetchall()
    cursorCie2 = connectionCier2.cursor()
    cursorCie2.execute(cierquery2de)
    connectionCier2.commit()
    record8de = cursorCie2.fetchall()
    cursorCie2 = connectionCier2.cursor()
    cursorCie2.execute(cierquery2cr)
    connectionCier2.commit()
    record8cr = cursorCie2.fetchall()
    cursorCie2.close()

    print(record8)
    print(record8ef)
    print(record8de)
    print(record8cr)
    
    montotpre2 = int(0)
    montotpre2ef = int(0)
    montotpre2de = int(0)
    montotpre2cr = int(0)

    for i in range(len(record8)):
        montotpre2=int(montotpre2)+int(record8[int(int(i)-1)][0])
    for i in range(len(record8ef)):
        montotpre2ef=int(montotpre2)+int(record8ef[int(int(i)-1)][0])
    for i in range(len(record8de)):
        montotpre2de=int(montotpre2)+int(record8de[int(int(i)-1)][0])
    for i in range(len(record8cr)):
        montotpre2cr=int(montotpre2)+int(record8cr[int(int(i)-1)][0])
    print(montotpre2)
    posfinquery="""INSERT INTO cierresRioCuarto ( fecha, total, usuario, total_efectivo, total_debito, total_credito )
    VALUES
    ( '"""+str(datetime.date.today())+"""', '"""+str(montotpre2)+"""', '"""+str(userresp1)+"""', '"""+str(montotpre2ef)+"""', '"""+str(montotpre2de)+"""', '"""+str(montotpre2cr)+"""' );"""
    cursorCie2 = connectionCier2.cursor()
    cursorCie2.execute(posfinquery)
    connectionCier2.commit()
    record9 = cursorCie2.fetchall()
    cursorCie2.close()
    print(record9)
    if record9 == ():
        ccialert1.setText('Cargado!')
    else:
        ccialert1.setText('NO cargado!')
####funcion insertar row en Desglose
def addtoDesl1(codnum2, cannum2):
    indforwid1 = str(None)
    if codnum2 or cannum2 != None:
        connectionStock4 = MySQLdb.connect(host='xxxxxxxxxxxx',
                                           port=3336,
                                           database='xxxxStock',
                                           user='xxxxxxxx',
                                           password='xxxxxxxx')

        QueryprodC4 = """SELECT 
                                                codigo,
                                                nombre,
                                                PrecioDetal
    
                                            FROM stockRioCuarto WHERE codigo = '""" + str(codnum2) + """';"""
        cursorQp4 = connectionStock4.cursor()
        cursorQp4.execute(QueryprodC4)
        # print(result)
        connectionStock4.commit()
        recordst4 = cursorQp4.fetchall()
        recordst5 = recordst4[int(int(len(recordst4)) - int(1))]
        cursorQp4.close()
        print(recordst5)
        Desgtabwid1.setRowCount(Desgtabwid1.rowCount()+int(1))
        Desgtabwid1.setItem(int(Desgtabwid1.rowCount()-1), 0, QTableWidgetItem(str(recordst5[0]),1))
        Desgtabwid1.setItem(int(Desgtabwid1.rowCount() - 1), 1, QTableWidgetItem(str(recordst5[1]), 1))
        Desgtabwid1.setItem(int(Desgtabwid1.rowCount() - 1), 2, QTableWidgetItem(str(recordst5[2]), 1))
        Desgtabwid1.setItem(int(Desgtabwid1.rowCount() - 1), 3, QTableWidgetItem(str(cannum2), 1))
        Desgtabwid1.setItem(int(Desgtabwid1.rowCount() - 1), 4, QTableWidgetItem(str(int(int(cannum2)*int(recordst5[2]))), 1))
        verdmontot2=int(realventtot1.text())+int(int(cannum2)*int(recordst5[2]))
        newmont1=verdmontot2+0

        realventtot1.setText(str(newmont1))

        #print(pruebapajua1)

        print(cannum2)


    else:
        print('error')
####funcion arrancar addtoDesl
def runaddtoDesl1():
    cannum2=canadd2.text()
    codnum2=codadd2.text()
    addtoDesl1(codnum2, cannum2)
####funcio cierre diario
def cierreDia1(userresp1, montopre1):
    connectionCier = MySQLdb.connect(host='xxxxxxxxxxxx',
                                     port=3336,
                                     database='xxxxMovi',
                                     user='xxxxxxxx',
                                     password='xxxxxxxx')
    cierquery1 = """SELECT total FROM ventas WHERE fecha >= '"""+str(datetime.date.today())+""" 00:00:00' AND fecha <= '"""+str(datetime.date.today())+""" 23:59:59';"""
    cierquery1ef = """SELECT efectivo FROM ventas WHERE fecha >= '"""+str(datetime.date.today())+""" 00:00:00' AND fecha <= '"""+str(datetime.date.today())+""" 23:59:59';"""
    cierquery1de = """SELECT debito FROM ventas WHERE fecha >= '"""+str(datetime.date.today())+""" 00:00:00' AND fecha <= '"""+str(datetime.date.today())+""" 23:59:59';"""
    cierquery1cr = """SELECT credito FROM ventas WHERE fecha >= '"""+str(datetime.date.today())+""" 00:00:00' AND fecha <= '"""+str(datetime.date.today())+""" 23:59:59';"""

    cursorCie1 = connectionCier.cursor()
    cursorCie1.execute(cierquery1)
    connectionCier.commit()

    record7 = cursorCie1.fetchall()
    cursorCie1 = connectionCier.cursor()
    cursorCie1.execute(cierquery1ef)
    connectionCier.commit()

    record7ef = cursorCie1.fetchall()
    cursorCie1 = connectionCier.cursor()
    cursorCie1.execute(cierquery1de)
    connectionCier.commit()

    record7de = cursorCie1.fetchall()
    cursorCie1 = connectionCier.cursor()
    cursorCie1.execute(cierquery1cr)
    connectionCier.commit()

    record7cr = cursorCie1.fetchall()
    cursorCie1.close()

    print(record7)
    print(record7ef)
    print(record7de)
    print(record7cr)

    montotpre1 = int(0)
    montotpre1ef = int(0)
    montotpre1de = int(0)
    montotpre1cr = int(0)

    for i in range(len(record7)):
        montotpre1=int(montotpre1)+int(record7[int(int(i)-1)][0])
    for i in range(len(record7ef)):
        montotpre1ef=int(montotpre1ef)+int(record7ef[int(int(i)-1)][0])
    for i in range(len(record7de)):
        montotpre1de=int(montotpre1de)+int(record7de[int(int(i)-1)][0])
    for i in range(len(record7cr)):
        montotpre1cr=int(montotpre1cr)+int(record7cr[int(int(i)-1)][0])
    print(montotpre1)
    print(montotpre1ef)
    print(montotpre1de)
    print(montotpre1cr)
    posfinquery="""INSERT INTO cierresRioCuarto ( fecha, total, usuario, total_efectivo, total_debito, total_credito )
    VALUES
    ( '"""+str(datetime.date.today())+"""', '"""+str(montotpre1)+"""', '"""+str(userresp1)+"""', '"""+str(montotpre1ef)+"""', '"""+str(montotpre1de)+"""', '"""+str(montotpre1cr)+"""' );"""
    
    cursorCie2 = connectionCier.cursor()
    cursorCie2.execute(posfinquery)
    connectionCier.commit()
    record9 = cursorCie2.fetchall()
    cursorCie2.close()
    print(record9)
    if record9 == ():
        ccialert1.setText('Cargado!')
    else:
        ccialert1.setText('NO cargado!')
####funcion abrir ventana de cierre
def runcierwin():
    cciwindow2.show()
    #getventt1(str('Master'), int(111))
####funcion arrancar cierreDia1()
def precierreDia1():

    userresp1 = str(cciuser1.text())
    montotpre1 = 0
    usercompar1 = USqline1.text()
    print(usercompar1)
    if userresp1 == usercompar1:
        cierreDia1(userresp1, montotpre1)
    else:
        ccialert1.setText('Usuario diferente!')

def getcreddat1():

    userlog1=USqline1.text()
    usercompar1 = str(userlog1)
    passw1=PSqline1.text()
    GetLogin1(userlog1, passw1)
    return usercompar1
    
    
####funcion abrir execven
def opexecven1():
    extot1.setText(str(realventtot1.text()))
    exCli1.setText('')
    exefect1.setText('')
    exdebi1.setText('')
    excredi1.setText('')
    commenttab1.setText('')
    alertlab1.setText('')
    exvenwindow2.show()
def rrunPostSale():
    userlog1=str(USqline1.text())
    runPostSale(exCli1, extot1, userlog1, exefect1, exdebi1, excredi1)
####funcion sumar todos productos
def totmont(Desgloselis1, extot1):
    cantcolumprod=int(Desgloselis1.count())

    for i in range(cantcolumprod):
        Desgloselis1.item(int(int(i)-1))
        selectw1 = Desgloselis1.currentItem()
        preprecioTosum1 = selectw1(QLabel, 'preciow2')
        rollcant1 = selectw1(QSpinBox, 'cantidadp2')
        precioTosum1 = int(preprecioTosum1.text())
        cantPrend1 = int(rollcant1.value())
        Sumtotpre1 = int(precioTosum1*cantPrend1)
        Sumfin1 = int(int(Sumfin1)+int(Sumtotpre1))
    print(Sumfin1)
    extot1.setText(Sumfin1)
    exvenwindow2.show()
####funcion arrancar totmont
def pretotmont():
    totmont(Desgloselis1, extot1)
####funcion añadir al carrito
def adtocart1(codnum2):
    connectionStock4 = MySQLdb.connect(host='xxxxxxxxxxxx',
                                       port=3336,
                                       database='xxxxStock',
                                       user='xxxxxxxx',
                                       password='xxxxxxxx')

    QueryprodC4 = """SELECT 
                                        codigo,
                                        nombre,
                                        PrecioDetal

                                    FROM stockRioCuarto WHERE codigo=""" + str(codnum2) + """;"""
    cursorQp4 = connectionStock4.cursor()
    cursorQp4.execute(QueryprodC4)
    # print(result)
    connectionStock4.commit()
    recordst4 = cursorQp4.fetchall()
    recordst5 = recordst4[int(int(len(recordst4)) - int(1))]
    cursorQp4.close()
    print(recordst5)
    for i in range(1):
        cartwfile = QFile("proddesglowidget.ui")
        cartwfile.open(QFile.ReadOnly)
        cartloader = QUiLoader()
        cartwwindow = cartloader.load(cartwfile)
        tam3 = QSize()
        tam3.setHeight(44)
        tam3.setWidth(963)
        itemN3 = QtWidgets.QListWidgetItem()
        itemN3.setSizeHint(tam3)
        Codpros3 = cartwwindow.findChild(QLabel, 'codn2')
        Nombpros3 = cartwwindow.findChild(QLabel, 'nomp2')
        pricest3 = cartwwindow.findChild(QLabel, 'preciow2')
        cantvprod3= cartwwindow.findChild(QSpinBox, 'cantidadp2')
        Codpros3.setText(str(recordst5[0]))
        Nombpros3.setText(str(recordst5[1]))
        pricest3.setText(str(recordst5[2]))
        Desgloselis1.addItem(itemN3)
        print('sfsaf')
        Desgloselis1.setItemWidget(itemN3, cartwwindow)
####funcion eliminar del desglose
def quitfromdes1():
    casaaa=Desgtabwid1.selectedItems()
    print(casaaa)
    ceseee=Desgtabwid1.item(Desgtabwid1.currentRow(), 4)
    twalfa=int(ceseee.text())
    caseee= Desgtabwid1.currentRow()
    Desgtabwid1.removeRow(caseee)
    realventtot1.setText(str(int(realventtot1.text())-int(twalfa)))




btn_brow_1.clicked.connect(getcreddat1)
btn_cod_1.clicked.connect(rungetprod1)
btn_nom_1.clicked.connect(rungetprod2)
btn_addp_1.clicked.connect(runaddtoDesl1)
btn_execv_1.clicked.connect(opexecven1)
execciebut2.clicked.connect(rrunPostSale)
btn_cierre_1.clicked.connect(runcierwin)
cciconf1.clicked.connect(precierreDia1)
btn_qfdes_1.clicked.connect(quitfromdes1)
sys.exit(app.exec_())
loginfile = QFile("ventaventana.ui")
loginfile.open(QFile.ReadOnly)
loader = QUiLoader()
loginwindow = loader.load(loginfile)

loginwindow.show()
